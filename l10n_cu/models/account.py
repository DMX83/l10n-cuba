# -*- coding: utf-8 -*-
from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError



class AccountAccount(models.Model):
    _inherit = 'account.account'
    
    account_type = fields.Selection(readonly=False, compute='_compute_account_type')
    expense_element_detailed = fields.Boolean(string='Expense element detailed?', 
        compute='_compute_expense_element_detailed',readonly=False )
    
    @api.depends('code','group_id','group_id.account_type','group_id.expense_element_detailed')
    def _compute_expense_element_detailed(self):
        for record in self:
            record.expense_element_detailed=record.group_id.expense_element_detailed   
    
    @api.depends('code','group_id','group_id.account_type','group_id.expense_element_detailed')
    def _compute_account_type(self):
        for record in self:
            super(AccountAccount, record)._compute_account_type()
            if record.group_id.account_type:
                record.account_type = record.group_id.account_type  
                record.reconcile= record.group_id.reconcile 
                record.expense_element_detailed=record.group_id.expense_element_detailed


class AccountAccountTag(models.Model):
    _inherit = 'account.account.tag'

    nature = fields.Selection([
        ('D', 'Debitable Account'), ('A', 'Creditable Account')])

class AccountGroup(models.Model):
    _inherit = "account.group"

    parent_id = fields.Many2one('account.group', compute='_compute_parent', index=True, ondelete='set null', readonly=False, store=True)
    reconcile = fields.Boolean(string='Allow Reconciliation', help="Check this box if accounts belonging this account group allows invoices & payments matching of journal items.")
    expense_element_detailed = fields.Boolean(string='Expense element detailed?')
    active = fields.Boolean(default=True)
    account_type = fields.Selection(
        selection=[
            ("asset_receivable", "Receivable"),
            ("asset_cash", "Bank and Cash"),
            ("asset_current", "Current Assets"),
            ("asset_non_current", "Non-current Assets"),
            ("asset_prepayments", "Prepayments"),
            ("asset_fixed", "Fixed Assets"),
            ("liability_payable", "Payable"),
            ("liability_credit_card", "Credit Card"),
            ("liability_current", "Current Liabilities"),
            ("liability_non_current", "Non-current Liabilities"),
            ("equity", "Equity"),
            ("equity_unaffected", "Current Year Earnings"),
            ("income", "Income"),
            ("income_other", "Other Income"),
            ("expense", "Expenses"),
            ("expense_depreciation", "Depreciation"),
            ("expense_direct_cost", "Cost of Revenue"),
            ("off_balance", "Off-Balance Sheet"),
        ],
        string="Type", required=False, help="Account Type is used for information purpose, to generate country-specific legal reports, and set the rules to close a fiscal year and generate opening entries."
    )
    note = fields.Text("Content and Usage")
    group_template_id = fields.Char()
    group_template_parent_id = fields.Char()

    @api.constrains('code_prefix_start', 'code_prefix_end')   
    def _constraint_prefix_overlap(self):
        pass


    @api.depends('group_template_parent_id')
    def _compute_parent(self):
        record_parents=self.search([])
        for record in self.filtered('group_template_parent_id'):
            parent=record_parents.filtered(lambda it: it.group_template_id==record.group_template_parent_id and it.company_id == self.env.company)
            if parent:
                record.parent_id= parent.id

    @api.depends('account_type')
    def _compute_reconcile(self):
        for group in self:
            group.reconcile = group.account_type in ('asset_receivable', 'liability_payable')

    def unlink(self):
        for record in self:
            record.parent_id = False
        result = super(AccountGroup, self).unlink()        
        return result

    def _adapt_parent_account_group(self):
       pass

    def _adapt_accounts_for_account_groups(self, account_ids=None):
        """Ensure consistency between accounts and account groups.
        Find and set the most specific group matching the code of the account.
        The most specific is the one with the longest prefixes and with the starting
        prefix being smaller than the account code and the ending prefix being greater.
        """
        company_ids = account_ids.company_id.ids if account_ids else self.company_id.ids
        account_ids = account_ids.ids if account_ids else []
        if not company_ids and not account_ids:
            return
        self.flush_model()
        self.env['account.account'].flush_model()

        account_where_clause = ''
        where_params = [tuple(company_ids)]
        if account_ids:
            account_where_clause = 'AND account.id IN %s'
            where_params.append(tuple(account_ids))

        self._cr.execute(f'''
            WITH candidates_account_groups AS (
                                SELECT
                    account.id AS account_id,
					account.code,
					ARRAY_AGG(agroup.id ORDER BY cast(agroup.code_prefix_end as int)- cast(agroup.code_prefix_start as int), agroup.id) AS group_ids
                FROM account_account account
                LEFT JOIN account_group agroup
                    ON agroup.code_prefix_start <= LEFT(account.code, char_length(agroup.code_prefix_start))
                    AND agroup.code_prefix_end >= LEFT(account.code, char_length(agroup.code_prefix_end))
                    AND agroup.company_id = account.company_id
                WHERE account.company_id IN %s {account_where_clause}
                GROUP BY account.id
            )
            UPDATE account_account
            SET group_id = rel.group_ids[1]
            FROM candidates_account_groups rel
            WHERE account_account.id = rel.account_id
        ''', where_params)
        self.env['account.account'].invalidate_model(['group_id'])    
