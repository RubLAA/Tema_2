from typing import List
from Fragmento import Fragmento

class Dialogo:
    def __init__(self, texto_bruto: str):
        self.texto_bruto = texto_bruto
        self.fragmentos: List[Fragmento] = []
    
    def procesar(self, separador: str = '#') -> None:
        """Divide el texto en fragmentos"""
        self.fragmentos = [Fragmento(parte) for parte in self.texto_bruto.split(separador) if parte.strip()]