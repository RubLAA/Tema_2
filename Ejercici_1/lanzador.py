from Estrella import Estrella
from Galaxia import Galaxia

def crear_estrellas():
    return [
        Estrella(2, 3, 1), 
        Estrella(4, 4, 4), 
        Estrella(-3, -1, 0)
        ]

def mostrar_info_estrellas(estrellas):
    for i, estrella in enumerate(estrellas, start=1):
        print(f'Estrella {chr(64 + i)}: {estrella}')
        print(f'Galaxia: {Galaxia.determinar_galaxia(estrella)}\n')

def calcular_distancias(estrellas):
    print(f'Distancia entre A y B: {estrellas[0].distancia(estrellas[1]):.2f}')
    print(f'Distancia entre B y C: {estrellas[1].distancia(estrellas[2]):.2f}')

def encontrar_mas_lejana(estrellas):
    mas_lejana = max(estrellas, key=lambda e: e.distancia_origen())
    print(f'\nLa estrella más lejana del origen es {mas_lejana} con distancia {mas_lejana.distancia_origen():.2f}')