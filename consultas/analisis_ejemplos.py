#!/usr/bin/env python3
"""
Ejemplos de análisis de licitaciones.
"""

import json
from scripts.analyzer import Analyzer


def ejemplo_resumen_licitacion():
    """Ejemplo: Resumen ejecutivo de licitación."""
    print("\n" + "="*60)
    print("EJEMPLO 1: Resumen de Licitación")
    print("="*60)
    
    analyzer = Analyzer('database.json')
    resumen = analyzer.generar_resumen_licitacion('LIC-2024-001')
    
    print(json.dumps(resumen, indent=2, ensure_ascii=False))


def ejemplo_estadisticas_globales():
    """Ejemplo: Estadísticas globales."""
    print("\n" + "="*60)
    print("EJEMPLO 2: Estadísticas Globales")
    print("="*60)
    
    analyzer = Analyzer('database.json')
    stats = analyzer.obtener_estadisticas_globales()
    
    print(f"Total licitaciones: {stats['total_licitaciones']}")
    print(f"Presupuesto total: ${stats['presupuesto_total']:,}")
    print(f"Propuestas recibidas: {stats['propuestas_recibidas_total']}")
    print(f"\nDistribución por estado:")
    
    for estado, cantidad in stats['distribucion_por_estado'].items():
        print(f"  {estado}: {cantidad}")


def ejemplo_comparativa_propuestas():
    """Ejemplo: Comparativa de propuestas."""
    print("\n" + "="*60)
    print("EJEMPLO 3: Comparativa de Propuestas")
    print("="*60)
    
    analyzer = Analyzer('database.json')
    comparativa = analyzer.comparar_propuestas('LIC-2024-001')
    
    print(json.dumps(comparativa, indent=2, ensure_ascii=False))


def ejemplo_analisis_presupuesto():
    """Ejemplo: Análisis presupuestario."""
    print("\n" + "="*60)
    print("EJEMPLO 4: Análisis de Presupuesto")
    print("="*60)
    
    analyzer = Analyzer('database.json')
    presupuesto = analyzer.analizar_presupuesto('LIC-2024-001')
    
    print(json.dumps(presupuesto, indent=2, ensure_ascii=False))


def ejemplo_evaluacion_cumplimiento():
    """Ejemplo: Evaluación de cumplimiento."""
    print("\n" + "="*60)
    print("EJEMPLO 5: Evaluación de Cumplimiento")
    print("="*60)
    
    analyzer = Analyzer('database.json')
    evaluacion = analyzer.evaluar_cumplimiento('LIC-2024-001', 'PROP-001')
    
    print(json.dumps(evaluacion, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    ejemplo_resumen_licitacion()
    ejemplo_estadisticas_globales()
    ejemplo_comparativa_propuestas()
    ejemplo_analisis_presupuesto()
    ejemplo_evaluacion_cumplimiento()
    
    print("\n" + "="*60)
    print("✓ Ejemplos de análisis completados")
    print("="*60)
