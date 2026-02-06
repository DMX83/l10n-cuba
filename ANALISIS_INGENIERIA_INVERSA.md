# Análisis de Ingeniería Inversa - Proyecto l10n-cuba

## Resumen Ejecutivo

**Proyecto:** Localización Cubana para Odoo v18  
**Autor:** Comunidad Cubana de Odoo (CCO)  
**Estado:** En desarrollo y pruebas (rama no liberada)  
**Licencia:** GPL-3.0  
**Propósito:** Sistema de gestión integral adaptado a las normativas y regulaciones cubanas

---

## 1. Visión General del Proyecto

### 1.1 Descripción
Este es un proyecto de **localización** para el sistema ERP Odoo, específicamente diseñado para cumplir con las normativas, regulaciones contables, laborales y operativas de Cuba. El proyecto está mantenido por la Comunidad Cubana de Odoo (CCO) con participación de entidades estatales.

### 1.2 Alcance del Proyecto
El proyecto proporciona:
- **Plan de cuentas contables** conforme a normativas cubanas (Resolución 494/2016 modificada por 407/2019)
- **Sistema de nóminas y recursos humanos** adaptado a la legislación laboral cubana
- **Reportes financieros** según Normas Cubanas de Información Financiera
- **Datos geográficos** (topónimos, municipios, bancos)
- **Módulos específicos** para POS, ventas web y documentación

---

## 2. Arquitectura del Sistema

### 2.1 Estructura Modular

El proyecto sigue la arquitectura modular de Odoo con **12 módulos principales**:

```
l10n-cuba/
├── l10n_cu                      # Módulo base de contabilidad
├── l10n_cu_address              # Topónimos y geografía cubana
├── l10n_cu_banks                # Sucursales bancarias
├── l10n_cu_hr                   # Recursos Humanos base
├── l10n_cu_hr_contract          # Contratos de empleados
├── l10n_cu_hr_holidays          # Control de ausencias
├── l10n_cu_hr_payroll           # Sistema de nóminas
├── l10n_cu_hr_payroll_account   # Nóminas con integración contable
├── l10n_cu_pos                  # Punto de venta
├── l10n_cu_reports              # Reportes financieros
├── l10n_cu_website_sale         # eCommerce
└── web_documentation            # Documentación funcional
```

### 2.2 Patrón de Diseño
- **Framework:** Odoo (OpenERP)
- **Patrón:** Modelo-Vista-Controlador (MVC)
- **Lenguajes:** Python (backend), XML (vistas), JavaScript (frontend)
- **Base de datos:** PostgreSQL (implícito en Odoo)

### 2.3 Estadísticas del Código
- **Archivos Python:** 73
- **Archivos XML:** 65
- **Módulos:** 12
- **Manifiestos:** 12 (`__manifest__.py`)

---

## 3. Análisis Detallado por Módulo

### 3.1 Módulo Base: l10n_cu (Contabilidad)

**Versión:** 16.0  
**Dependencias:** `account` (módulo estándar de Odoo)

#### Características Principales:
1. **Plan de Cuentas Múltiple:**
   - Cuentas comunes (393 cuentas)
   - Sector privado (38 cuentas)
   - Unidades presupuestadas (35 cuentas)
   - Sector cooperativo (19 cuentas)

2. **Tipos de Empresas Soportadas:**
   - Actividad Empresarial
   - Unidades Presupuestadas de Tratamiento Especial
   - Sector Cooperativo Agropecuario y no Agropecuario

3. **Extensiones Personalizadas:**
   ```python
   # Hereda modelos de Odoo y añade funcionalidad cubana
   class AccountAccount(models.Model):
       _inherit = 'account.account'
       expense_element_detailed = fields.Boolean()
   ```

4. **Diarios Predefinidos:**
   - Fondo para cambios (FCAMB)
   - Fondo para pagos menores (FPMEN)
   - Extraído para nómina (FNOM)
   - Sellos (FSELL)
   - Tarjetas prepagadas (FPREP)
   - Otros valores en caja (FOTROS)

#### Normativas Implementadas:
- Resolución 494/2016 (Plan de Cuentas)
- Resolución 407/2019 (Modificaciones)

---

### 3.2 Módulo de Nóminas: l10n_cu_hr_payroll

**Versión:** 17.0  
**Dependencias:** `l10n_cu_hr`, `om_hr_payroll` (Odoo Mates)

#### Funcionalidades:
1. **Cálculo de Nóminas:**
   - Reglas salariales configurables
   - Cálculo automático de vacaciones (9.09% de días trabajados)
   - Soporte para otros inputs (bonos, deducciones)

2. **Código Destacado:**
   ```python
   def action_payslip_done(self):
       # Asigna vacaciones automáticamente al finalizar nómina
       salary_rule_09 = self.env.ref('l10n_cu_hr_payroll.hr_payroll_rules_09_dias')
       for line in self.line_ids:
           if line.code == salary_rule_09.code:
               # Crea asignación de vacaciones
               allocation = self.env["hr.leave.allocation"].create(res)
   ```

3. **Campos Personalizados:**
   - `total`: Valor neto a pagar
   - `total_on_payable`: Indicador de nóminas no pagables (≤ 0)

4. **Proyecciones:**
   - Módulo `hr_projection.py` para proyecciones de nómina

---

### 3.3 Módulo de Reportes: l10n_cu_reports

**Versión:** 17.0  
**Dependencias:** `accounting_pdf_reports`, `report_xlsx`, `l10n_cu`

#### Reportes Financieros Implementados:
1. **Estado de Situación (ES)** - Proforma 5924-00
2. **Estado de Resultado (ER)** - Proforma 5925-00
3. **Estado de Ganancias Emergentes (EGE)** - Proforma (sin código)
4. **Estado de Valor Agregado Bruto (EVAB)** - Proforma 5926-04
5. **Reporte General** - Proforma 5927-00

#### Formato de Reportes:
- PDF (usando `accounting_pdf_reports`)
- Excel (usando `report_xlsx`)

#### Características:
- Configuración de plan anual por línea
- Apertura de ejercicio fiscal
- Agrupación de cuentas por prefijos
- Balance de socios

---

### 3.4 Módulo de Direcciones: l10n_cu_address

**Versión:** 20.0.1  
**Datos Incluidos:**
- **Provincias:** 15 provincias + 1 municipio especial (Isla de la Juventud)
- **Municipios:** Aproximadamente 168 municipios (archivo de ~49KB)

---

### 3.5 Módulo de Bancos: l10n_cu_banks

**Versión:** 16.0  
**Propósito:** Define sucursales bancarias cubanas para integración con pagos y transferencias

---

### 3.6 Módulo de Contratos: l10n_cu_hr_contract

**Versión:** 16.0  
**Dependencias:** `hr_contract`, `l10n_cu_hr_payroll`  
**Propósito:** Gestión de contratos laborales según legislación cubana

---

### 3.7 Módulo de Ausencias: l10n_cu_hr_holidays

**Versión:** 17.0  
**Dependencias:** `hr_holidays`, `l10n_cu_hr_payroll`  
**Funcionalidad:** Control de vacaciones, licencias y ausencias conforme a normativas

---

### 3.8 Módulo POS: l10n_cu_pos

**Versión:** 17.0  
**Dependencias:** `point_of_sale`, `l10n_cu`  
**Propósito:** Adaptación del punto de venta a requisitos cubanos

---

### 3.9 Módulo Website Sale: l10n_cu_website_sale

**Versión:** 2.0  
**Dependencias:** `base`, `website_sale`, `l10n_cu_address`  
**Propósito:** Soporte de eCommerce con direcciones y municipios cubanos

---

### 3.10 Módulo de Documentación: web_documentation

**Versión:** 17.0  
**Propósito:** Documentación funcional embebida en el sistema

---

## 4. Análisis Técnico

### 4.1 Patrones de Programación Identificados

#### Herencia de Modelos
```python
class AccountAccount(models.Model):
    _inherit = 'account.account'
    # Extiende funcionalidad sin modificar el núcleo
```

#### Computed Fields
```python
@api.depends('code','group_id','group_id.account_type')
def _compute_account_type(self):
    # Cálculos automáticos basados en dependencias
```

#### Sobrescritura de Métodos
```python
def _create_records_with_xmlid(self, model, template_vals, company):
    # Personaliza creación de registros
    res = super()._create_records_with_xmlid(model, template_vals, company)
    return res
```

### 4.2 Tecnologías y Dependencias Externas

**Dependencias OCA (Odoo Community Association):**
- `intrastat-extrastat`
- `reporting-engine` (para reportes financieros)

**Dependencias Python:**
- `lxml` (procesamiento XML)
- `xlrd` (lectura de Excel)
- `xlsxwriter` (escritura de Excel)

**Dependencias Odoo Mates:**
- `om_hr_payroll` (base de nóminas)
- `om_hr_payroll_account` (nóminas contables)
- `accounting_pdf_reports` (reportes PDF)

### 4.3 Gestión de Datos

**Archivos CSV:**
- Cuentas contables por sector
- Reglas salariales

**Archivos XML:**
- Grupos de cuentas
- Templates de reportes
- Vistas de usuario
- Datos de provincias, municipios y bancos

---

## 5. Flujo de Trabajo del Sistema

### 5.1 Configuración Inicial
1. Instalación de módulo base `l10n_cu`
2. Selección de tipo de empresa (empresarial/presupuestada/cooperativa)
3. Configuración de plan de cuentas correspondiente
4. Instalación de módulos complementarios según necesidades

### 5.2 Proceso de Nómina
```
1. Registro de empleados (l10n_cu_hr)
   ↓
2. Creación de contratos (l10n_cu_hr_contract)
   ↓
3. Registro de asistencia y ausencias (l10n_cu_hr_holidays)
   ↓
4. Generación de nómina (l10n_cu_hr_payroll)
   ↓
5. Cálculo automático (reglas salariales + inputs)
   ↓
6. Asignación automática de vacaciones (9.09%)
   ↓
7. Integración contable (l10n_cu_hr_payroll_account)
```

### 5.3 Reportes Financieros
```
1. Registro de operaciones contables
   ↓
2. Asignación a cuentas del plan cubano
   ↓
3. Configuración de reportes (plan anual, apertura)
   ↓
4. Generación de estados financieros (ES, ER, EGE, EVAB)
   ↓
5. Exportación en PDF o Excel
```

---

## 6. Fortalezas y Debilidades

### 6.1 Fortalezas
✅ **Cumplimiento Normativo:** Totalmente alineado con regulaciones cubanas  
✅ **Modularidad:** Permite instalar solo lo necesario  
✅ **Comunidad Activa:** Respaldado por CCO y entidades estatales  
✅ **Documentación:** Incluye README en cada módulo  
✅ **Automatización:** Cálculos automáticos de nómina y vacaciones  
✅ **Flexibilidad:** Soporta múltiples tipos de entidades  

### 6.2 Debilidades
⚠️ **Versiones Mixtas:** Módulos en versiones 16.0, 17.0 y 20.0  
⚠️ **Estado Beta:** Aún no liberado oficialmente  
⚠️ **Dependencias Externas:** Requiere módulos de terceros (Odoo Mates, OCA)  
⚠️ **Código Comentado:** Presencia de código comentado en producción  
⚠️ **Falta de Tests:** No se identificaron tests unitarios  
⚠️ **Documentación Incompleta:** Algunos módulos sin README  

---

## 7. Análisis de Seguridad

### 7.1 Control de Acceso
- Archivos `security/ir.model.access.csv` en cada módulo
- Define permisos por grupo de usuarios

### 7.2 Validaciones
```python
@api.constrains('code_prefix_start', 'code_prefix_end')   
def _constraint_prefix_overlap(self):
    pass  # ⚠️ Validación sin implementar
```

---

## 8. Oportunidades de Mejora

### 8.1 Técnicas
1. **Unificación de versiones** a Odoo 18
2. **Implementación de tests** unitarios e integración
3. **Eliminación de código comentado**
4. **Completar validaciones** pendientes
5. **Optimización de consultas SQL**

### 8.2 Funcionales
1. **Módulo de Activos Fijos** (mencionado en roadmap)
2. **Tesorería y Presupuesto** según normas MFP
3. **Costo de ventas en POS**
4. **Estado de Valor Agregado Bruto** (5926-04) - pendiente

---

## 9. Dependencias del Sistema

### 9.1 Grafo de Dependencias

```
                    l10n_cu (base)
                         |
        +----------------+----------------+
        |                |                |
   l10n_cu_hr    l10n_cu_reports    l10n_cu_address
        |                                 |
   +----+----+                    l10n_cu_website_sale
   |         |
hr_contract hr_payroll
   |         |
hr_contract payroll_account
hr_holidays
```

### 9.2 Dependencias Críticas
- **Odoo Core:** account, hr, point_of_sale, website_sale
- **OCA:** reporting-engine
- **Odoo Mates:** om_hr_payroll, om_hr_payroll_account

---

## 10. Recomendaciones para Programador Senior

### 10.1 Para Mantenimiento
1. **Prioridad Alta:**
   - Migrar todos los módulos a versión 18.0
   - Implementar suite de tests
   - Completar validaciones pendientes

2. **Prioridad Media:**
   - Refactorizar código duplicado
   - Mejorar documentación inline
   - Estandarizar nomenclatura

3. **Prioridad Baja:**
   - Optimizar consultas de base de datos
   - Añadir logging para auditoría

### 10.2 Para Desarrollo
1. **Nuevas Características:**
   - Implementar módulo de Activos Fijos
   - Desarrollar módulo de Tesorería
   - Completar reportes faltantes (EVAB)

2. **Integraciones:**
   - API para sistemas de terceros
   - Conectores con bancos cubanos
   - Integración con facturación electrónica

---

## 11. Conclusiones

### 11.1 Alcance como Programador Senior

Como programador senior, con este proyecto puedo:

✅ **Análisis Completo:** Entender toda la arquitectura y lógica de negocio  
✅ **Mantenimiento:** Corregir bugs, optimizar código, actualizar versiones  
✅ **Extensión:** Añadir nuevos módulos y funcionalidades  
✅ **Refactorización:** Mejorar la estructura y patrones de código  
✅ **Documentación:** Crear documentación técnica y funcional  
✅ **Testing:** Implementar suite completa de tests  
✅ **Consultoría:** Asesorar sobre mejores prácticas y arquitectura  
✅ **Migración:** Actualizar a nuevas versiones de Odoo  

### 11.2 Limitaciones

❌ **Regulaciones:** No puedo modificar normativas legales cubanas  
❌ **Aprobación:** Cambios críticos requieren validación de CCO  
❌ **Infraestructura:** Despliegue y hosting fuera del alcance del código  

### 11.3 Valoración General

**Calidad del Código:** ⭐⭐⭐⭐☆ (4/5)  
**Arquitectura:** ⭐⭐⭐⭐⭐ (5/5)  
**Documentación:** ⭐⭐⭐☆☆ (3/5)  
**Mantenibilidad:** ⭐⭐⭐⭐☆ (4/5)  
**Cumplimiento:** ⭐⭐⭐⭐⭐ (5/5)  

**Puntuación Global:** ⭐⭐⭐⭐☆ (4.2/5)

---

## 12. Próximos Pasos Sugeridos

1. ✅ **Completar este análisis** de ingeniería inversa
2. 🔄 **Migrar a Odoo 18.0** todos los módulos
3. 🔄 **Implementar tests** unitarios e integración
4. 🔄 **Desarrollar módulos pendientes** (Activos, Tesorería)
5. 🔄 **Crear documentación** de usuario final
6. 🔄 **Establecer CI/CD** para pruebas automáticas
7. 🔄 **Preparar release** de versión estable

---

## Anexos

### A. Comandos Útiles para Análisis

```bash
# Contar líneas de código Python
find . -name "*.py" -not -path "./.git/*" | xargs wc -l

# Encontrar todos los modelos
grep -r "class.*models.Model" --include="*.py"

# Listar todas las vistas
find . -name "*.xml" -path "*/views/*"

# Ver dependencias de un módulo
cat */*/manifest__.py | grep "depends"
```

### B. Referencias

- **Odoo Documentation:** https://www.odoo.com/documentation/
- **OCA:** https://github.com/OCA/
- **Odoo Mates:** https://github.com/odoomates/
- **CCO:** https://cco-web.odoo.com

---

**Documento generado por:** Análisis de Ingeniería Inversa  
**Fecha:** 2026-02-06  
**Versión:** 1.0  
**Confidencialidad:** Público (GPL-3.0)
