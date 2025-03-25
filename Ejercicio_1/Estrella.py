import math

class Estrella:
    def __init__(self, x=0, y=0, z=0):
        """Constructor que inicializa una estrella con coordenadas (x, y, z)
        
        Args:
            x (float): Coordenada en el eje X (default 0)
            y (float): Coordenada en el eje Y (default 0)
            z (float): Coordenada en el eje Z (default 0)
        """
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        """Representación en string como (x, y, z)"""
        return f"({self.x}, {self.y}, {self.z})"
    
    def galaxia(self):
        """Determina la galaxia basada en coordenadas según especificación
        
        Returns:
            str: Nombre de la galaxia:
                - "Andrómeda" si x>0, y>0, z>0
                - "Sombrero" si x<0, y<0, z<0
                - "Vía Láctea" en otros casos
        """
        if self.x > 0 and self.y > 0 and self.z > 0:
            return "Andrómeda"
        elif self.x < 0 and self.y < 0 and self.z < 0:
            return "Sombrero"
        return "Vía Láctea"
    
    def distancia(self, otra_estrella):
        """Calcula distancia entre esta estrella y otra
        
        Args:
            otra_estrella (Estrella): Otra instancia de Estrella
            
        Returns:
            float: Distancia euclidiana en unidades espaciales
            
        Raises:
            TypeError: Si otra_estrella no es instancia de Estrella
        """
        if not isinstance(otra_estrella, Estrella):
            raise TypeError("Se requiere un objeto Estrella para calcular distancia")
        dx = self.x - otra_estrella.x
        dy = self.y - otra_estrella.y
        dz = self.z - otra_estrella.z
        return math.sqrt(dx**2 + dy**2 + dz**2)