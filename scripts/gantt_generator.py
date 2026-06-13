#!/usr/bin/env python3
"""
Generador de cronogramas Gantt para licitaciones mineras.
"""

import json
from typing import Dict, List, Any
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class GanttGenerator:
    """Generador de gráficos Gantt."""
    
    def __init__(self):
        """Inicializa el generador."""
        self.plantilla_html = self._obtener_plantilla_html()
    
    def generar(self, id_licitacion: str, archivo_salida: str) -> bool:
        """Genera un gráfico Gantt.
        
        Args:
            id_licitacion: ID de la licitación
            archivo_salida: Ruta del archivo de salida HTML
        
        Returns:
            True si se generó exitosamente
        """
        try:
            html = self.plantilla_html.format(
                titulo=f"Cronograma - {id_licitacion}",
                fecha_generacion=datetime.now().isoformat()
            )
            
            with open(archivo_salida, 'w', encoding='utf-8') as f:
                f.write(html)
            
            logger.info(f"Gráfico Gantt generado: {archivo_salida}")
            return True
        except Exception as e:
            logger.error(f"Error al generar Gantt: {e}")
            return False
    
    def _obtener_plantilla_html(self) -> str:
        """Obtiene plantilla HTML para Gantt."""
        return """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titulo}</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/gantt-chart-js@latest/dist/gantt.css">
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }}
        h1 {{
            color: #333;
            border-bottom: 3px solid #007bff;
            padding-bottom: 10px;
        }}
        .gantt-container {{
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .info {{
            background: #e7f3ff;
            border-left: 4px solid #2196F3;
            padding: 12px;
            margin: 20px 0;
            border-radius: 3px;
        }}
        .pie {{
            text-align: center;
            margin-top: 20px;
            color: #666;
            font-size: 12px;
        }}
    </style>
</head>
<body>
    <h1>{titulo}</h1>
    <div class="info">
        <strong>Fecha de generación:</strong> {fecha_generacion}
    </div>
    <div class="gantt-container">
        <svg id="gantt" width="100%" height="400"></svg>
    </div>
    <div class="pie">
        <p>Este es un diagrama Gantt de cronograma. Requiere integración con biblioteca de graficación.</p>
        <p>Recomendado: Chart.js, D3.js o Frappe Gantt</p>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/frappe-gantt@latest/dist/frappe-gantt.umd.js"></script>
</body>
</html>
"""


if __name__ == '__main__':
    generator = GanttGenerator()
    
    print("Generando cronograma Gantt...")
    exito = generator.generar('LIC-2024-001', 'cronogramas/gantt_licitacion_001.html')
    
    if exito:
        print("✓ Cronograma generado exitosamente")
    else:
        print("✗ Error al generar cronograma")
