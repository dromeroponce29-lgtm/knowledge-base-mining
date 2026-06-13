#!/usr/bin/env python3
"""
Analizador de licitaciones y propuestas.
Realiza comparativas, análisis presupuestarios y evaluación de cumplimiento.
"""

import json
from typing import Dict, List, Any, Optional
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Analyzer:
    """Analizador de licitaciones."""
    
    def __init__(self, database_path: str):
        """Inicializa el analizador."""
        self.database_path = database_path
        self.db = self._cargar_database()
    
    def _cargar_database(self) -> Dict[str, Any]:
        """Carga la base de datos."""
        try:
            with open(self.database_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Base de datos no encontrada")
            return {}
    
    def obtener_licitacion(self, id_licitacion: str) -> Optional[Dict[str, Any]]:
        """Obtiene una licitación por ID."""
        for lic in self.db.get('licitaciones', []):
            if lic['id_licitacion'] == id_licitacion:
                return lic
        return None
    
    def comparar_propuestas(self, id_licitacion: str) -> Dict[str, Any]:
        """Compara propuestas de una licitación.
        
        Args:
            id_licitacion: ID de la licitación
        
        Returns:
            Análisis comparativo
        """
        lic = self.obtener_licitacion(id_licitacion)
        if not lic:
            return {'error': 'Licitación no encontrada'}
        
        return {
            'id_licitacion': id_licitacion,
            'nombre': lic.get('nombre'),
            'total_propuestas': lic.get('propuestas_recibidas', 0),
            'fecha_analisis': datetime.now().isoformat(),
            'resumen': 'Análisis de propuestas recibidas',
            'notas': 'Implementar análisis detallado según evaluaciones'
        }
    
    def analizar_presupuesto(self, id_licitacion: str) -> Dict[str, Any]:
        """Analiza el presupuesto de una licitación."""
        lic = self.obtener_licitacion(id_licitacion)
        if not lic:
            return {'error': 'Licitación no encontrada'}
        
        return {
            'id_licitacion': id_licitacion,
            'presupuesto_asignado': lic.get('presupuesto_asignado'),
            'moneda': lic.get('moneda'),
            'estado': lic.get('estado'),
            'fecha_analisis': datetime.now().isoformat(),
            'analisis': 'Análisis presupuestario disponible'
        }
    
    def evaluar_cumplimiento(self, id_licitacion: str, 
                            id_propuesta: str) -> Dict[str, Any]:
        """Evalúa el cumplimiento de requisitos de una propuesta."""
        lic = self.obtener_licitacion(id_licitacion)
        if not lic:
            return {'error': 'Licitación no encontrada'}
        
        return {
            'id_licitacion': id_licitacion,
            'id_propuesta': id_propuesta,
            'criterios_evaluacion': lic.get('criterios_evaluacion', []),
            'fecha_evaluacion': datetime.now().isoformat(),
            'estado': 'Evaluación pendiente',
            'cumplimiento': 'Por determinar'
        }
    
    def generar_resumen_licitacion(self, id_licitacion: str) -> Dict[str, Any]:
        """Genera un resumen ejecutivo de una licitación."""
        lic = self.obtener_licitacion(id_licitacion)
        if not lic:
            return {'error': 'Licitación no encontrada'}
        
        dias_transcurridos = self._calcular_dias_desde(lic.get('fecha_publicacion'))
        
        return {
            'id_licitacion': lic['id_licitacion'],
            'nombre': lic.get('nombre'),
            'mina': lic.get('mina'),
            'tipo': lic.get('tipo_licitacion'),
            'estado': lic.get('estado'),
            'presupuesto': {
                'monto': lic.get('presupuesto_asignado'),
                'moneda': lic.get('moneda')
            },
            'fechas': {
                'publicacion': lic.get('fecha_publicacion'),
                'cierre': lic.get('fecha_cierre'),
                'adjudicacion': lic.get('fecha_adjudicacion')
            },
            'propuestas': lic.get('propuestas_recibidas', 0),
            'ganador': lic.get('ganador'),
            'dias_transcurridos': dias_transcurridos,
            'criterios': lic.get('criterios_evaluacion', [])
        }
    
    def _calcular_dias_desde(self, fecha_str: str) -> int:
        """Calcula días desde una fecha."""
        try:
            fecha = datetime.fromisoformat(fecha_str.replace('Z', '+00:00'))
            dias = (datetime.now(fecha.tzinfo) - fecha).days
            return dias
        except:
            return 0
    
    def obtener_estadisticas_globales(self) -> Dict[str, Any]:
        """Obtiene estadísticas globales."""
        licitaciones = self.db.get('licitaciones', [])
        
        presupuesto_total = sum(l.get('presupuesto_asignado', 0) for l in licitaciones)
        propuestas_total = sum(l.get('propuestas_recibidas', 0) for l in licitaciones)
        
        estados = {}
        for lic in licitaciones:
            estado = lic.get('estado')
            estados[estado] = estados.get(estado, 0) + 1
        
        return {
            'total_licitaciones': len(licitaciones),
            'presupuesto_total': presupuesto_total,
            'propuestas_recibidas_total': propuestas_total,
            'distribucion_por_estado': estados,
            'fecha_analisis': datetime.now().isoformat()
        }


if __name__ == '__main__':
    analyzer = Analyzer('database.json')
    
    print("\n=== Estadísticas Globales ===")
    stats = analyzer.obtener_estadisticas_globales()
    print(json.dumps(stats, indent=2, ensure_ascii=False))
    
    print("\n=== Resumen Licitación LIC-2024-001 ===")
    resumen = analyzer.generar_resumen_licitacion('LIC-2024-001')
    print(json.dumps(resumen, indent=2, ensure_ascii=False))
