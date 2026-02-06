# l10n-cuba Technical Summary
## Quick Reference for Developers

*Last Updated: February 6, 2026*

---

## Overview

**l10n-cuba** is a comprehensive Odoo localization suite for Cuba (v16-v18), providing accounting, HR, payroll, and e-commerce modules compliant with Cuban regulations (NCIF - Normas Cubanas de Información Financiera).

**Maintained by**: Cuban Odoo Community (CCO) - https://cco-web.odoo.com  
**License**: GPL-3.0  
**Status**: Development/Testing (not yet released for v18)

---

## Module Architecture (3 Layers)

### Foundation Layer
- **l10n_cu**: Base accounting module with 4 Chart of Accounts variants (Decree 494/2016, modified by 407/2019)
- **l10n_cu_address**: Cuban geographic hierarchy (15 provinces, 168 municipalities)
- **l10n_cu_hr**: HR foundation with attendance management

### Business Logic Layer
- **l10n_cu_banks**: Cuban bank branches registry
- **l10n_cu_reports**: 5 NCIF-compliant financial reports
- **l10n_cu_website_sale**: E-commerce with Cuban address support
- **l10n_cu_pos**: Point of Sale localization

### HR Specialized Layer
- **l10n_cu_hr_payroll**: Payroll processing with projections
- **l10n_cu_hr_contract**: Employment contracts with contribution regimens
- **l10n_cu_hr_holidays**: Leave management
- **l10n_cu_hr_payroll_account**: Payroll accounting integration

---

## Key Features

### Accounting
- ✅ 4 Chart of Accounts templates for different entity types
- ✅ Cuban National Economic Activities Classifier (CNAE)
- ✅ Hierarchical account groups with auto-assignment
- ✅ Expense element trees with analytic account sync
- ✅ 6 auto-created Cuban-specific cash accounts

### HR & Payroll
- ✅ Cuban social security contribution regimens (2000, 2500, 2700, 3000)
- ✅ Annual salary projections with monthly breakdown
- ✅ Multi-employment tracking (pluriempleo)
- ✅ Automatic vacation accrual from payroll
- ✅ Custom payroll inputs (vacations, bonuses, deductions)

### Geographic Data
- ✅ 15 Cuban provinces pre-loaded
- ✅ 168 municipalities with codes and province links
- ✅ Address validation ensuring municipality-province consistency

### Financial Reporting
- ✅ 5 standardized report types (ES, ER, EGE, EVAB, 5927-00)
- ✅ PDF and XLSX export formats
- ✅ NCIF compliance

---

## Dependencies

### External Modules (OCA)
```
accounting_pdf_reports  → Financial PDF reports
report_xlsx            → Excel export
intrastat-extrastat    → Trade statistics
```

### Odoo Mates
```
om_hr_payroll          → Base payroll engine
om_hr_payroll_account  → Payroll accounting
```

### Python Libraries
```
lxml, xlrd, xlsxwriter
```

---

## Technical Architecture

### Design Patterns
1. **Hierarchical Account Structures**: Prefix-based auto-assignment
2. **Parent-Store Trees**: Expense elements with analytic sync
3. **Template-Based Configuration**: Chart of accounts migration
4. **Custom Input Tracking**: Date-scoped payroll adjustments
5. **Geographic Cascades**: Country → State → Municipality

### Performance Optimizations
- Raw SQL for bulk account group assignment
- Computed fields with proper dependencies
- Database-level unique constraints

### Extensibility
- Model inheritance (`_inherit` pattern)
- Wizard-based workflows
- CSV/XML hybrid data configuration

---

## Regulatory Compliance

### Accounting Standards
- **Decree 494/2016** (modified 407/2019): Chart of Accounts
- **NCIF**: Cuban Financial Information Standards
- **CNAE**: Economic Activities Classification

### HR/Payroll Compliance
- Cuban social security regimens
- Cuban labor law for leave management
- Multi-employment regulations for retirees

---

## Quick Start for Developers

### 1. Installation
```bash
# Install dependencies
pip install lxml xlrd xlsxwriter

# Install base module
./odoo-bin -i l10n_cu -d mydb

# Install full suite
./odoo-bin -i l10n_cu,l10n_cu_address,l10n_cu_banks,l10n_cu_hr,l10n_cu_hr_payroll -d mydb
```

### 2. Module Update
```bash
./odoo-bin -u l10n_cu -d mydb --stop-after-init
```

### 3. Typical Module Structure
```
l10n_cu_<module>/
├── __manifest__.py          # Module metadata
├── models/                  # Python models
├── data/                    # Master data (XML/CSV)
├── views/                   # UI views
├── security/                # Access rights
├── static/                  # JS/CSS/images
└── wizards/                 # Transactional wizards
```

---

## Roadmap

### Planned Modules
- ⏳ **Fixed Assets**: Tangible/intangible asset management
- ⏳ **Treasury**: Cash flow control
- ⏳ **Budget Control**: Ministry of Finance standards for public entities

### Planned Improvements
- Cost of sales reports for POS
- Government system integrations
- Enhanced financial reporting

---

## Code Quality

### Strengths ✅
- Well-structured modular architecture
- Comprehensive regulatory compliance
- Efficient data organization
- Proper Odoo patterns

### Areas for Improvement ⚠️
- Limited documentation
- No unit tests
- Version inconsistencies
- Mixed Spanish/English code

---

## Project Metrics

```
Modules:              12 (11 functional + 1 docs)
Python Models:        ~40+
Data Files:           ~50+ XML/CSV
Lines of Code:        ~15,000+ (estimated)
Account Templates:    ~1,000+
Municipalities:       168
Provinces:            15
Salary Rules:         ~100+
```

---

## Contributing

### For New Contributors
1. Start with `l10n_cu` and `l10n_cu_address` (foundation modules)
2. Study Decree 494/2016 and 407/2019
3. Review Odoo localization documentation
4. Set up dev environment with OCA and Odoo Mates dependencies

### For Extending Functionality
1. Follow layered architecture: Foundation → Logic → Specialized
2. Use model inheritance (don't modify core)
3. Add data in CSV/XML files
4. Document in Spanish/English

---

## Resources

- **Odoo Mates**: https://github.com/odoomates/odooapps
- **OCA Reporting**: https://github.com/OCA/reporting-engine
- **Cuban Odoo Community**: https://cco-web.odoo.com

---

## Contact

For questions or contributions, contact the Cuban Odoo Community.

*For detailed technical analysis, see [PROJECT_ANALYSIS.md](PROJECT_ANALYSIS.md) (Spanish)*
