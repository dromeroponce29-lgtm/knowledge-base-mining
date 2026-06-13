# Base de Conocimiento - Licitaciones Mineras 🏔️⛏️

## Descripción

Base de conocimiento centralizada para gestionar, organizar y analizar documentos relacionados con procesos de licitación en el sector minero. Incluye búsqueda avanzada, análisis de propuestas, generación de reportes y visualización de cronogramas Gantt.

## Características Principales

✅ **Gestión de Documentos**
- Organización jerárquica de licitaciones
- Clasificación por tipo de documento
- Metadatos completos y rastreabilidad

✅ **Búsqueda y Recuperación**
- Búsqueda full-text en documentos
- Filtros por tipo, estado, fecha, mina
- Consultas avanzadas por tags y categorías

✅ **Análisis**
- Extracción de información clave
- Análisis de propuestas técnicas
- Comparativa de presupuestos

✅ **Reportes**
- Generación automática de reportes
- Estadísticas por licitación
- Evaluación de cumplimiento

✅ **Cronogramas**
- Visualización Gantt de actividades
- Seguimiento de hitos
- Timeline de licitaciones

## Estructura de Carpetas

```
knowledge-base-mining/
├── README.md
├── docs/                          # Documentación general
│   ├── GUIA_USUARIO.md
│   ├── ESTRUCTURA_DATOS.md
│   └── API_REFERENCE.md
├── licitaciones/                  # Datos de licitaciones
│   ├── licitacion_001/
│   │   ├── meta.json             # Metadatos de licitación
│   │   ├── bases/
│   │   │   ├── bases_tecnicas.pdf
│   │   │   └── terminos_referencia.pdf
│   │   ├── propuestas/
│   │   │   ├── propuesta_empresa_a.pdf
│   │   │   └── propuesta_empresa_b.pdf
│   │   ├── evaluacion/
│   │   │   └── evaluacion_propuestas.json
│   │   └── cronograma/
│   │       └── gantt.json
│   └── licitacion_002/
├── esquemas/                      # Esquemas de datos
│   ├── licitacion_schema.json
│   ├── documento_schema.json
│   ├── evaluacion_schema.json
│   └── cronograma_schema.json
├── scripts/                       # Scripts Python
│   ├── search_engine.py           # Motor de búsqueda
│   ├── analyzer.py                # Análisis de licitaciones
│   ├── gantt_generator.py         # Generador de Gantt
│   ├── report_generator.py        # Generador de reportes
│   └── utils.py                   # Utilidades
├── templates/                     # Plantillas
│   ├── licitacion_template.json
│   ├── documento_template.json
│   └── evaluacion_template.json
├── consultas/                     # Ejemplos de consultas
│   ├── busqueda_ejemplos.py
│   ├── analisis_ejemplos.py
│   └── reportes_ejemplos.py
├── database.json                  # Base de datos central
├── config.yaml                    # Configuración
└── .gitignore
```

## Instalación y Uso Rápido

### 1. Clonar el repositorio

```bash
git clone https://github.com/dromeroponce29-lgtm/knowledge-base-mining.git
cd knowledge-base-mining
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Búsqueda de documentos

```python
from scripts.search_engine import SearchEngine

se = SearchEngine('database.json')
resultados = se.buscar('bases técnicas', tipo='licitacion')
for resultado in resultados:
    print(resultado)
```

### 4. Análisis de propuestas

```python
from scripts.analyzer import Analyzer

analyzer = Analyzer('database.json')
analisis = analyzer.comparar_propuestas('licitacion_001')
print(analisis)
```

### 5. Generar Gantt

```python
from scripts.gantt_generator import GanttGenerator

gantt = GanttGenerator()
gantt.generar('licitacion_001', 'cronograma_001.html')
```

## Tipos de Documentos Soportados

| Tipo | Descripción | Ejemplo |
|------|-------------|----------|
| **Bases Técnicas** | Especificaciones técnicas del proyecto | bases_tecnicas.pdf |
| **Términos de Referencia** | TdR con alcance y requisitos | terminos_referencia.pdf |
| **Presupuesto** | Desglose de costos y presupuestos | presupuesto.xlsx |
| **Propuestas** | Respuestas de proveedores/contratistas | propuesta_empresa.pdf |
| **Evaluación** | Criterios y matriz de evaluación | evaluacion.json |
| **Cronograma** | Actividades y hitos del proyecto | cronograma.json |
| **Contrato** | Documentos contractuales | contrato_adjudicacion.pdf |

## Esquema de Metadatos (meta.json)

```json
{
  "id_licitacion": "LIC-2024-001",
  "nombre": "Servicios de Exploración - Mina El Dorado",
  "mina": "El Dorado",
  "tipo_licitacion": "Abierta",
  "estado": "en_evaluacion",
  "fecha_publicacion": "2024-01-15",
  "fecha_cierre": "2024-02-28",
  "fecha_adjudicacion": null,
  "presupuesto_asignado": 500000,
  "moneda": "USD",
  "criterios_evaluacion": [
    "Experiencia técnica",
    "Precio",
    "Propuesta técnica"
  ],
  "documentos": [
    {
      "nombre": "bases_tecnicas.pdf",
      "tipo": "bases_tecnicas",
      "fecha_carga": "2024-01-15",
      "url": "licitaciones/licitacion_001/bases/bases_tecnicas.pdf"
    }
  ],
  "propuestas_recibidas": 3,
  "ganador": null,
  "tags": ["exploracion", "mineria", "2024"]
}
```

## Funciones Principales

### 🔍 Motor de Búsqueda

- Búsqueda por palabras clave
- Búsqueda por tipo de documento
- Filtros: estado, fecha, mina, tags
- Búsqueda combinada avanzada

### 📊 Análisis

- Comparativa de propuestas técnicas
- Análisis de presupuestos
- Evaluación de cumplimiento de requisitos
- Extracción de información clave

### 📈 Reportes

- Reporte general de licitaciones
- Resumen ejecutivo por licitación
- Análisis comparativo de propuestas
- Informe de evaluación

### 📅 Cronogramas Gantt

- Visualización de actividades
- Timeline de hitos
- Seguimiento de fases
- Exportación HTML/PNG

## API y Consultas

### Búsqueda

```python
# Búsqueda simple
resultados = se.buscar('bases técnicas')

# Búsqueda con filtros
resultados = se.buscar(
    'exploración',
    estado='en_evaluacion',
    mina='El Dorado',
    tipo_documento='bases_tecnicas'
)

# Búsqueda con tags
resultados = se.buscar_por_tags(['mineria', '2024'])
```

### Análisis

```python
# Comparar propuestas
comparativa = analyzer.comparar_propuestas('licitacion_001')

# Analizar presupuesto
presupuesto = analyzer.analizar_presupuesto('licitacion_001')

# Evaluar cumplimiento
evaluacion = analyzer.evaluar_cumplimiento('licitacion_001', 'propuesta_1')
```

### Reportes

```python
# Generar reportes
reporte = reporter.generar_reporte('licitacion_001')
reporte.exportar_pdf('reporte_licitacion_001.pdf')
reporte.exportar_excel('reporte_licitacion_001.xlsx')
```

## Configuración (config.yaml)

```yaml
base_datos:
  archivo: 'database.json'
  encoding: 'utf-8'

busqueda:
  indice_completo: true
  similitud_minima: 0.7

reportes:
  formato_default: 'pdf'
  incluir_graficos: true

gantt:
  formato: 'html'
  temas: ['default', 'dark', 'light']
```

## Contribución

Para agregar nuevas licitaciones:

1. Crear carpeta `licitacion_XXX` en `/licitaciones/`
2. Agregar `meta.json` con metadatos
3. Organizar documentos en subcarpetas por tipo
4. Actualizar `database.json`
5. Hacer commit y push

## Licencia

MIT License - Libre para usar y modificar

## Contacto

Para consultas o sugerencias: dromeroponce29-lgtm@github.com

---

**Última actualización:** 2024
