#!/usr/bin/env python3
"""
Motor de búsqueda para la base de conocimiento de licitaciones mineras.
Permite búsqueda full-text, filtros avanzados y consultas complejas.
"""

import json
import re
from typing import List, Dict, Any, Optional
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SearchEngine:
    """Motor de búsqueda para licitaciones y documentos."""
    
    def __init__(self, database_path: str):
        """Inicializa el motor de búsqueda."""
        self.database_path = database_path
        self.db = self._cargar_database()
        logger.info(f"Base de datos cargada: {len(self.db.get('licitaciones', []))} licitaciones")
    
    def _cargar_database(self) -> Dict[str, Any]:
        """Carga la base de datos desde archivo JSON."""
        try:
            with open(self.database_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Base de datos no encontrada: {self.database_path}")
            return {}
    
    def buscar(self, consulta: str, **filtros) -> List[Dict[str, Any]]:
        """Búsqueda simple con filtros opcionales.
        
        Args:
            consulta: Texto a buscar
            filtros: Filtros adicionales (estado, tipo_licitacion, mina, etc.)
        
        Returns:
            Lista de resultados encontrados
        """
        resultados = []
        licitaciones = self.db.get('licitaciones', [])
        
        # Normalizar consulta
        consulta_normalizada = consulta.lower()
        
        for lic in licitaciones:
            # Aplicar filtros
            if not self._aplicar_filtros(lic, filtros):
                continue
            
            # Búsqueda en campos principales
            if self._coincide_en_campos(lic, consulta_normalizada):
                lic['relevancia'] = self._calcular_relevancia(lic, consulta_normalizada)
                resultados.append(lic)
        
        # Ordenar por relevancia
        resultados.sort(key=lambda x: x.get('relevancia', 0), reverse=True)
        return resultados
    
    def buscar_por_tags(self, tags: List[str]) -> List[Dict[str, Any]]:
        """Búsqueda por tags."""
        resultados = []
        licitaciones = self.db.get('licitaciones', [])
        
        for lic in licitaciones:
            lic_tags = set(lic.get('tags', []))
            if any(tag in lic_tags for tag in tags):
                resultados.append(lic)
        
        return resultados
    
    def buscar_por_mina(self, mina: str) -> List[Dict[str, Any]]:
        """Búsqueda por mina."""
        return self.buscar('', mina=mina)
    
    def buscar_por_estado(self, estado: str) -> List[Dict[str, Any]]:
        """Búsqueda por estado de licitación."""
        return self.buscar('', estado=estado)
    
    def buscar_documentos(self, consulta: str) -> List[Dict[str, Any]]:
        """Búsqueda en documentos."""
        resultados = []
        consulta_normalizada = consulta.lower()
        
        for lic in self.db.get('licitaciones', []):
            for doc in lic.get('documentos', []):
                if (consulta_normalizada in doc.get('nombre', '').lower() or
                    consulta_normalizada in doc.get('tipo', '').lower()):
                    resultados.append({
                        'id_licitacion': lic['id_licitacion'],
                        'documento': doc
                    })
        
        return resultados
    
    def _aplicar_filtros(self, licitacion: Dict[str, Any], filtros: Dict[str, Any]) -> bool:
        """Aplica filtros a una licitación."""
        for clave, valor in filtros.items():
            if valor is not None and licitacion.get(clave) != valor:
                return False
        return True
    
    def _coincide_en_campos(self, licitacion: Dict[str, Any], consulta: str) -> bool:
        """Verifica si la consulta coincide en campos clave."""
        campos_busqueda = ['nombre', 'descripcion', 'mina']
        
        for campo in campos_busqueda:
            if consulta in licitacion.get(campo, '').lower():
                return True
        
        # Búsqueda en tags
        if any(consulta in tag.lower() for tag in licitacion.get('tags', [])):
            return True
        
        return False
    
    def _calcular_relevancia(self, licitacion: Dict[str, Any], consulta: str) -> float:
        """Calcula puntuación de relevancia."""
        puntuacion = 0.0
        
        # Coincidencia exacta en nombre
        if consulta == licitacion.get('nombre', '').lower():
            puntuacion += 100
        # Coincidencia en nombre
        elif consulta in licitacion.get('nombre', '').lower():
            puntuacion += 50
        # Coincidencia en descripción
        elif consulta in licitacion.get('descripcion', '').lower():
            puntuacion += 25
        # Coincidencia en tags
        elif any(consulta in tag.lower() for tag in licitacion.get('tags', [])):
            puntuacion += 10
        
        return puntuacion
    
    def listar_todas(self) -> List[Dict[str, Any]]:
        """Lista todas las licitaciones."""
        return self.db.get('licitaciones', [])
    
    def obtener_estadisticas(self) -> Dict[str, Any]:
        """Obtiene estadísticas de la base de datos."""
        return self.db.get('estadisticas', {})


if __name__ == '__main__':
    # Ejemplo de uso
    se = SearchEngine('database.json')
    
    # Búsqueda simple
    print("\n=== Búsqueda: 'Exploración' ===")
    resultados = se.buscar('Exploración')
    for r in resultados:
        print(f"  {r['id_licitacion']}: {r['nombre']}")
    
    # Búsqueda por estado
    print("\n=== Licitaciones activas ===")
    activas = se.buscar_por_estado('publicada')
    for lic in activas:
        print(f"  {lic['id_licitacion']}: {lic['nombre']}")
    
    # Búsqueda por mina
    print("\n=== Licitaciones - Mina El Dorado ===")
    eldorado = se.buscar_por_mina('El Dorado')
    for lic in eldorado:
        print(f"  {lic['id_licitacion']}: {lic['nombre']}")
    
    # Estadísticas
    print("\n=== Estadísticas ===")
    stats = se.obtener_estadisticas()
    print(f"  Total licitaciones: {stats.get('total_licitaciones')}")
    print(f"  Presupuesto total: ${stats.get('presupuesto_total'):,}")
