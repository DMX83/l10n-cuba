# Resumen Rápido - Proyecto l10n-cuba

## ¿Qué es este proyecto?

**l10n-cuba** es una **localización de Odoo** (sistema ERP) adaptada a las **normativas cubanas**. Es como tener un "paquete de Cuba" para Odoo que hace que el sistema entienda:
- Las leyes contables cubanas
- El sistema de nóminas del país
- Los reportes financieros oficiales
- La geografía (provincias, municipios)
- Los bancos cubanos

## Componentes Principales

### 🏦 Contabilidad (l10n_cu)
- **493 cuentas contables** adaptadas a Res. 494/2016 y 407/2019
- 4 planes de cuentas para diferentes sectores:
  - Empresas privadas
  - Empresas estatales
  - Cooperativas
  - Unidades presupuestadas

### 👥 Recursos Humanos (l10n_cu_hr_*)
- Contratos de trabajo
- Control de asistencia
- Vacaciones y ausencias
- **Nóminas automáticas** con:
  - Cálculo automático de vacaciones (9.09%)
  - Integración con contabilidad
  - Proyecciones de nómina

### 📊 Reportes Financieros (l10n_cu_reports)
- Estado de Situación (Balance)
- Estado de Resultado
- Estado de Ganancias Emergentes
- Estado de Valor Agregado Bruto
- Exportación a PDF y Excel

### 🗺️ Datos Geográficos (l10n_cu_address)
- 15 provincias + Isla de la Juventud
- ~168 municipios
- Integración con direcciones

### 💰 Punto de Venta (l10n_cu_pos)
- POS adaptado a Cuba
- Integración con contabilidad cubana

## Tecnología

- **Lenguaje:** Python 3.x + XML + JavaScript
- **Framework:** Odoo (v16-18)
- **Base de datos:** PostgreSQL
- **Arquitectura:** Modular (12 módulos)
- **Licencia:** GPL-3.0

## Estado Actual

⚠️ **EN DESARROLLO** - No liberado oficialmente  
✅ Funcional para uso interno  
🔄 Migración a Odoo 18 en progreso  

## ¿Cómo Funciona?

```
1. Instalar Odoo
2. Añadir módulos l10n_cu*
3. Seleccionar tipo de empresa
4. ¡El sistema ya habla "cubano"!
```

## Cifras Clave

- 📁 **12 módulos**
- 🐍 **73 archivos Python**
- 📄 **65 archivos XML**
- 📊 **493 cuentas contables**
- 🏛️ **168 municipios**
- 👤 **~10 contribuidores**
- ⭐ **4.2/5 calidad de código**

## Mantenedores

- **Comunidad Cubana de Odoo (CCO)**
- **Idola Odoo Team**
- Entidades estatales cubanas

## Para Desarrolladores

### Instalar
```bash
git clone https://github.com/DMX83/l10n-cuba.git
# Configurar Odoo para usar estos addons
```

### Estructura
```
l10n-cuba/
├── l10n_cu/              # Base contable
├── l10n_cu_hr*/          # RRHH y nóminas
├── l10n_cu_reports/      # Reportes
├── l10n_cu_address/      # Geografía
└── ...
```

### Dependencias Externas
- Odoo Mates (nóminas)
- OCA reporting-engine (reportes)
- lxml, xlrd, xlsxwriter

## Próximos Desarrollos

🔜 **Activos Fijos**  
🔜 **Tesorería**  
🔜 **Control de presupuesto**  
🔜 **Costo de ventas en POS**  

## Contacto

🌐 https://cco-web.odoo.com  
📧 Comunidad Cubana de Odoo  

---

**Generado:** 2026-02-06  
**Por:** Análisis de Ingeniería Inversa Automatizado
