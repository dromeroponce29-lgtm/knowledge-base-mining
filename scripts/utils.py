#!/usr/bin/env python3
"""
Utilidades para la base de conocimiento.
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def cargar_json(ruta: str) -> Dict[str, Any]:
    """Carga un archivo JSON."""
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"Archivo no encontrado: {ruta}")
        return {}
    except json.JSONDecodeError:
        logger.error(f"Error al decodificar JSON: {ruta}")
        return {}


def guardar_json(datos: Dict[str, Any], ruta: str) -> bool:
    """Guarda datos en archivo JSON."""
    try:
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)
        logger.info(f"Archivo guardado: {ruta}")
        return True
    except Exception as e:
        logger.error(f"Error al guardar JSON: {e}")
        return False


def crear_backup(ruta_original: str) -> str:
    """Crea un backup de un archivo."""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    ruta_backup = f"{ruta_original}.backup_{timestamp}"
    
    try:
        with open(ruta_original, 'r', encoding='utf-8') as f:
            contenido = f.read()
        
        with open(ruta_backup, 'w', encoding='utf-8') as f:
            f.write(contenido)
        
        logger.info(f"Backup creado: {ruta_backup}")
        return ruta_backup
    except Exception as e:
        logger.error(f"Error al crear backup: {e}")
        return ""


def formatear_moneda(monto: float, moneda: str = 'USD') -> str:
    """Formatea un monto como moneda."""
    simbolos = {
        'USD': '$',
        'EUR': '€',
        'CLP': '$',
        'ARS': '$',
        'BRL': 'R$'
    }
    
    simbolo = simbolos.get(moneda, moneda)
    return f"{simbolo} {monto:,.2f}"


def calcular_dias_entre(fecha1: str, fecha2: str) -> int:
    """Calcula días entre dos fechas."""
    try:
        d1 = datetime.fromisoformat(fecha1)
        d2 = datetime.fromisoformat(fecha2)
        return abs((d2 - d1).days)
    except:
        return 0


def estado_a_color(estado: str) -> str:
    """Convierte estado a color."""
    colores = {
        'draft': '#808080',
        'publicada': '#4CAF50',
        'en_evaluacion': '#2196F3',
        'adjudicada': '#FF9800',
        'cancelada': '#f44336',
        'completada': '#9C27B0'
    }
    return colores.get(estado, '#000000')


def estado_a_emoji(estado: str) -> str:
    """Convierte estado a emoji."""
    emojis = {
        'draft': '📝',
        'publicada': '📢',
        'en_evaluacion': '🔍',
        'adjudicada': '🏆',
        'cancelada': '❌',
        'completada': '✅'
    }
    return emojis.get(estado, '•')
