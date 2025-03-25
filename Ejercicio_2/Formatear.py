from typing import List
from Fragmento import Fragmento

class FormateadorZen:
    @staticmethod
    def formatear(fragmentos: List[Fragmento]) -> str:
        """Genera el texto con formato mejorado"""
        if not fragmentos:
            return ""
        
        lineas = []
        anterior_era_narracion = False
        
        for fragmento in fragmentos:
            texto = fragmento.texto_formateado
            
            if fragmento.es_dialogo:
                # Formatear diálogos con guión
                if ' -' in texto:
                    parte, accion = texto.split(' -', 1)
                    lineas.append(f"  • {parte} -{accion}")
                else:
                    lineas.append(f"  • {texto}")
                anterior_era_narracion = False
            else:
                # Formatear narraciones con salto de línea
                if anterior_era_narracion:
                    lineas.append(f"\n {texto}")
                else:
                    lineas.append(f"\n {texto}")
                anterior_era_narracion = True
        
        if ' -' in texto:
            try:
                parte, accion = texto.split(' -', 1)
            except ValueError:
                # Manejar casos donde el split falle
                parte, accion = texto, ""
            
        # Unir y asegurar que no haya espacios iniciales/finales no deseados
        return '\n'.join(lineas).strip()