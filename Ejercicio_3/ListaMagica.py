class ListaMagica:

    def __init__(self, numeros_originales):
        self.original = list(numeros_originales)
        self.transformada = []
        self._procesar()

    def _procesar(self):
        """Realiza todas las transformaciones requeridas"""
        unicos = list(set(self.original))
        ordenados = sorted(unicos, reverse=True)
        pares = [num for num in ordenados if num % 2 == 0]
        suma = sum(pares)
        self.transformada = [suma] + pares
        self._verificar()

    def _verificar(self):
        """Verifica que la suma coincida"""
        suma_verificacion = sum(self.transformada[1:])
        assert self.transformada[0] == suma_verificacion, f'Error: La suma {suma_verificacion} no coincide con {self.transformada[0]}'

    def obtener_resultado(self):
        """Devuelve la lista transformada"""
        return self.transformada

    def __str__(self):
        return f'Original: {self.original}\nTransformada: {self.transformada}'