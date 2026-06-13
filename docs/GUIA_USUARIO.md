# Guía de Usuario - Base de Conocimiento Licitaciones Mineras

## Índice

1. [Introducción](#introducción)
2. [Requisitos](#requisitos)
3. [Instalación](#instalación)
4. [Uso Básico](#uso-básico)
5. [Búsqueda Avanzada](#búsqueda-avanzada)
6. [Análisis](#análisis)
7. [Preguntas Frecuentes](#preguntas-frecuentes)

## Introducción

La base de conocimiento de licitaciones mineras es un sistema centralizado para:

- ✅ Gestionar documentos de licitaciones
- ✅ Buscar información rápidamente
- ✅ Analizar propuestas y presupuestos
- ✅ Generar reportes y cronogramas
- ✅ Evaluar cumplimiento de criterios

## Requisitos

- Python 3.8+
- pip (gestor de paquetes Python)
- 100 MB de espacio en disco

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/dromeroponce29-lgtm/knowledge-base-mining.git
cd knowledge-base-mining
```

### 2. Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\\Scripts\\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Uso Básico

### Búsqueda Simple

```python
from scripts.search_engine import SearchEngine

# Inicializar
se = SearchEngine('database.json')

# Búsqueda por palabra clave
resultados = se.buscar('exploración')

for lic in resultados:
    print(f"{lic['id_licitacion']}: {lic['nombre']}")
```

### Listar Todas las Licitaciones

```python
todaslas = se.listar_todas()
for lic in todas:
    print(f"{lic['id_licitacion']} - {lic['estado']}")
```

### Obtener Estadísticas

```python
stats = se.obtener_estadisticas()
print(f"Total: {stats['total_licitaciones']} licitaciones")
print(f"Presupuesto: ${stats['presupuesto_total']:,}")
```

## Búsqueda Avanzada

### Por Estado

```python
# Licitaciones publicadas
publicadas = se.buscar_por_estado('publicada')

# Estados disponibles:
# - draft: Borrador
# - publicada: Activa
# - en_evaluacion: En evaluación
# - adjudicada: Adjudicada
# - cancelada: Cancelada
# - completada: Completada
```

### Por Mina

```python
# Todas las licitaciones de una mina
eldorado = se.buscar_por_mina('El Dorado')
```

### Por Tags

```python
# Búsqueda múltiple con tags
resultados = se.buscar_por_tags(['mineria', '2024'])
```

### Búsqueda Combinada

```python
# Combinar búsqueda con filtros
resultados = se.buscar(
    'equipos',
    estado='en_evaluacion',
    mina='La Esperanza',
    tipo_licitacion='Abierta'
)
```

## Análisis

### Análisis General

```python
from scripts.analyzer import Analyzer

analyzer = Analyzer('database.json')

# Estadísticas globales
stats = analyzer.obtener_estadisticas_globales()
print(stats)
```

### Resumen de Licitación

```python
resumen = analyzer.generar_resumen_licitacion('LIC-2024-001')
print(resumen)
```

### Comparativa de Propuestas

```python
comparativa = analyzer.comparar_propuestas('LIC-2024-001')
print(f"Total propuestas: {comparativa['total_propuestas']}")
```

### Análisis Presupuestario

```python
presupuesto = analyzer.analizar_presupuesto('LIC-2024-001')
print(f"Presupuesto: {presupuesto['presupuesto_asignado']} {presupuesto['moneda']}")
```

## Cronogramas Gantt

### Generar Gráfico Gantt

```python
from scripts.gantt_generator import GanttGenerator

gantt = GanttGenerator()
gantt.generar('LIC-2024-001', 'cronogramas/gantt_001.html')
```

### Ver Resultado

Abre el archivo HTML generado en tu navegador.

## Preguntas Frecuentes

### ¿Cómo agrego una nueva licitación?

1. Crea una carpeta `licitacion_XXX` en `/licitaciones/`
2. Agrega un archivo `meta.json` con metadatos
3. Organiza los documentos por tipo
4. Actualiza `database.json`
5. Haz commit y push

### ¿Dónde guardo los documentos PDF?

Organiza los documentos en subcarpetas dentro de cada licitación:
- `/bases/` - Bases técnicas
- `/propuestas/` - Propuestas recibidas
- `/evaluacion/` - Evaluaciones
- `/cronograma/` - Cronogramas

### ¿Puedo buscar dentro de archivos PDF?

Actualmente la búsqueda es por metadatos. Para búsqueda en PDF necesitas extraer texto usando bibliotecas como `pdfplumber` o `PyPDF2`.

### ¿Cómo genero reportes?

```python
from scripts.report_generator import ReportGenerator

reporter = ReportGenerator()
reporte = reporter.generar_reporte('LIC-2024-001')
reporte.exportar_pdf('reporte.pdf')
```

---

**¿Necesitas ayuda?** Consulta la documentación completa o crea un issue en GitHub.
