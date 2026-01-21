from odoo import models, _
from odoo.addons.account.models.chart_template import template


class AccountChartTemplate(models.AbstractModel):
    _inherit = "account.chart.template"

    @template("cu_common")
    def _get_cu_common_template_data(self):
        return {
            "name": _("Cuba - Plan Contable Comun (494/2016 mod. 407/2019)"),
            "country": "cu",
            "code_digits": "3",
            "sequence": 1,
            "visible": False,
            "property_account_receivable_id": "account_common_1350020",
            "property_account_payable_id": "account_common_4050020",
            "property_account_expense_categ_id": "account_common_826",
            "property_account_income_categ_id": "account_common_900",
            "account_journal_suspense_account_id": "account_common_6993",
            "account_journal_payment_debit_account_id": "account_common_106",
            "account_journal_payment_credit_account_id": "account_common_107",
            "default_cash_difference_expense_account_id": "account_common_839",
            "default_cash_difference_income_account_id": "account_common_924",
            "account_journal_early_pay_discount_loss_account_id": "account_common_835",
            "account_journal_early_pay_discount_gain_account_id": "account_common_920",
        }

    @template("cu_common", "res.company")
    def _get_cu_common_res_company(self):
        return {
            self.env.company.id: {
                "account_fiscal_country_id": "base.cu",
                "bank_account_code_prefix": "109",
                "cash_account_code_prefix": "101",
                "transfer_account_code_prefix": "108",
                "account_default_pos_receivable_account_id": "account_common_1300020",
                "income_currency_exchange_account_id": "account_common_924",
                "expense_currency_exchange_account_id": "account_common_839",
            }
        }

    @template("cu_freelance")
    def _get_cu_freelance_template_data(self):
        return {
            "name": _("Cuba - Plan Contable TCP"),
            "country": "cu",
            "parent": "cu_common",
            "sequence": 2,
            "property_account_receivable_id": "account_tcp_135",
            "property_account_payable_id": "account_common_4050020",
            "property_account_expense_categ_id": "account_common_800",
            "property_account_income_categ_id": "account_common_900",
            "account_journal_payment_debit_account_id": "account_common_106",
            "account_journal_payment_credit_account_id": "account_common_107",
            "default_cash_difference_expense_account_id": "account_common_839",
            "default_cash_difference_income_account_id": "account_common_924",
            "account_journal_early_pay_discount_loss_account_id": "account_common_835",
            "account_journal_early_pay_discount_gain_account_id": "account_common_920",
        }

    @template("cu_freelance", "res.company")
    def _get_cu_freelance_res_company(self):
        return {
            self.env.company.id: {
                "account_default_pos_receivable_account_id": "account_tcp_135",
            }
        }

    @template("cu_public")
    def _get_cu_public_template_data(self):
        return {
            "name": _("Cuba - Plan Contable Empresas Publicas"),
            "country": "cu",
            "parent": "cu_common",
            "sequence": 3,
        }

    @template("cu_private")
    def _get_cu_private_template_data(self):
        return {
            "name": _("Cuba - Plan Contable Sector Privado y Cooperativo"),
            "country": "cu",
            "parent": "cu_common",
            "sequence": 4,
        }
