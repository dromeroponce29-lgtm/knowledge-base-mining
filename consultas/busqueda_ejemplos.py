#!/usr/bin/env python3
"""
Ejemplos de búsquedas en la base de conocimiento.
"""

from scripts.search_engine import SearchEngine


def ejemplo_busqueda_simple():
    """Ejemplo: Búsqueda simple."""
    print("\n" + "="*60)
    print("EJEMPLO 1: Búsqueda Simple")
    print("="*60)
    
    se = SearchEngine('database.json')
    
    # Buscar licitaciones que contengan 'exploración'
    resultados = se.buscar('exploración')
    
    print(f"Encontrados: {len(resultados)} resultados\n")
    for lic in resultados:
        print(f"  ID: {lic['id_licitacion']}")
        print(f"  Nombre: {lic['nombre']}")
        print(f"  Estado: {lic['estado']}")
        print()


def ejemplo_busqueda_por_estado():
    """Ejemplo: Búsqueda por estado."""
    print("\n" + "="*60)
    print("EJEMPLO 2: Búsqueda por Estado")
    print("="*60)
    
    se = SearchEngine('database.json')
    
    # Buscar licitaciones publicadas
    publicadas = se.buscar_por_estado('publicada')
    
    print(f"Licitaciones publicadas: {len(publicadas)}\n")
    for lic in publicadas:
        print(f"  • {lic['id_licitacion']}: {lic['nombre']}")


def ejemplo_busqueda_por_mina():
    """Ejemplo: Búsqueda por mina."""
    print("\n" + "="*60)
    print("EJEMPLO 3: Búsqueda por Mina")
    print("="*60)
    
    se = SearchEngine('database.json')
    
    minas = ['El Dorado', 'La Esperanza', 'San José']
    
    for mina in minas:
        resultados = se.buscar_por_mina(mina)
        print(f"\nMina: {mina}")
        print(f"Licitaciones: {len(resultados)}")
        for lic in resultados:
            print(f"  • {lic['id_licitacion']}: {lic['nombre']}")


def ejemplo_busqueda_por_tags():
    """Ejemplo: Búsqueda por tags."""
    print("\n" + "="*60)
    print("EJEMPLO 4: Búsqueda por Tags")
    print("="*60)
    
    se = SearchEngine('database.json')
    
    tags = ['mineria', '2024']
    resultados = se.buscar_por_tags(tags)
    
    print(f"Tags: {', '.join(tags)}")
    print(f"Resultados: {len(resultados)}\n")
    
    for lic in resultados:
        print(f"  • {lic['id_licitacion']}: {lic['nombre']}")
        print(f"    Tags: {', '.join(lic['tags'])}")


def ejemplo_busqueda_combinada():
    """Ejemplo: Búsqueda combinada con filtros."""
    print("\n" + "="*60)
    print("EJEMPLO 5: Búsqueda Combinada")
    print("="*60)
    
    se = SearchEngine('database.json')
    
    # Buscar en mina específica con estado específico
    resultados = se.buscar(
        'servicios',
        estado='en_evaluacion',
        mina='El Dorado'
    )
    
    print(f"Búsqueda: 'servicios'")
    print(f"Filtros: estado='en_evaluacion', mina='El Dorado'")
    print(f"Resultados: {len(resultados)}\n")
    
    for lic in resultados:
        print(f"  • {lic['id_licitacion']}: {lic['nombre']}")


def ejemplo_estadisticas():
    """Ejemplo: Obtener estadísticas."""
    print("\n" + "="*60)
    print("EJEMPLO 6: Estadísticas")
    print("="*60)
    
    se = SearchEngine('database.json')
    
    stats = se.obtener_estadisticas()
    
    print(f"Total licitaciones: {stats.get('total_licitaciones')}")
    print(f"Licitaciones activas: {stats.get('licitaciones_activas')}")
    print(f"Licitaciones adjudicadas: {stats.get('licitaciones_adjudicadas')}")
    print(f"Presupuesto total: ${stats.get('presupuesto_total'):,}")
    print(f"Propuestas recibidas: {stats.get('propuestas_totales_recibidas')}")


def ejemplo_busqueda_documentos():
    """Ejemplo: Buscar documentos."""
    print("\n" + "="*60)
    print("EJEMPLO 7: Búsqueda de Documentos")
    print("="*60)
    
    se = SearchEngine('database.json')
    
    # Buscar documentos por tipo
    resultados = se.buscar_documentos('bases_tecnicas')
    
    print(f"Documentos encontrados: {len(resultados)}\n")
    
    for item in resultados:
        doc = item['documento']
        print(f"  Licitación: {item['id_licitacion']}")
        print(f"  Documento: {doc['nombre']}")
        print(f"  Tipo: {doc['tipo']}")
        print()


if __name__ == '__main__':
    # Ejecutar todos los ejemplos
    ejemplo_busqueda_simple()
    ejemplo_busqueda_por_estado()
    ejemplo_busqueda_por_mina()
    ejemplo_busqueda_por_tags()
    ejemplo_busqueda_combinada()
    ejemplo_estadisticas()
    ejemplo_busqueda_documentos()
    
    print("\n" + "="*60)
    print("✓ Todos los ejemplos ejecutados")
    print("="*60)
