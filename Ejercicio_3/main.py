from ListaMagica import ListaMagica
from random import randint

def ejemplo_uso():
    # Ejemplo de uso
    numeros = [randint(0, 20) for _ in range(15)]
    lista_magica = ListaMagica(numeros)
    
    print("\n=== LISTA MÁGICA ===\n")
    print(lista_magica)
    print("\nResultado final:", lista_magica.obtener_resultado(), "\n")

if __name__ == "__main__":
    ejemplo_uso()