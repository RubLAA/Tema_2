class Fragmento:
    """Representa un fragmento de texto que puede ser narración o diálogo.
    
    Atributos:
        texto_original (str): Texto bruto del fragmento
        es_dialogo (bool): Indica si el fragmento es un diálogo
    """
    def __init__(self, texto: str):
        self.texto_original = texto.strip()
        self.es_dialogo = self._es_dialogo()
    
    def _es_dialogo(self) -> bool:
        """Determina si es diálogo por guión inicial"""
        # Busca patrones como "-dijo", "-respondió", etc.
        return self.texto_original.startswith(('-dijo', '-respondió', '-preguntó', '-exclamó')) or \
               (self.texto_original.find(' -') > 0 and self.texto_original.find(' -') < len(self.texto_original)-3)
    
    @property
    def texto_formateado(self) -> str:
        """Aplica formato según el tipo de fragmento"""
        texto = self.texto_original.capitalize()
        
        if self.es_dialogo:
            if not texto.endswith('.'):
                texto += '.'
            return texto
        else:
            return texto.rstrip('.') + '...'