from Estrella import Estrella

def main():
    print("=== EXPERIMENTACIÓN REQUERIDA ===")
    
    # Crear estrellas como en el ejercicio
    estrella_A = Estrella(2, 3, 1)
    estrella_B = Estrella(4, 4, 4)
    estrella_C = Estrella(-3, -1, 0)
    
    # 1. Imprimir estrellas
    print("\n1. Estrellas creadas:")
    print(f"A: {estrella_A}")
    print(f"B: {estrella_B}")
    print(f"C: {estrella_C}")
    
    # 2. Determinar galaxias
    print("\n2. Galaxias determinadas:")
    print(f"A: {estrella_A.galaxia()}")
    print(f"B: {estrella_B.galaxia()}")
    print(f"C: {estrella_C.galaxia()}")
    
    # 3. Calcular distancias
    print("\n3. Distancias calculadas:")
    print(f"A-B: {estrella_A.distancia(estrella_B):.2f}")
    print(f"B-C: {estrella_B.distancia(estrella_C):.2f}")
    
    # 4. Estrella más lejana del origen (adicional)
    print("\n4. Distancia al origen:")
    estrellas = [estrella_A, estrella_B, estrella_C]
    mas_lejana = max(estrellas, key=lambda e: e.distancia(Estrella(0, 0, 0)))
    print(f"Estrella más lejana: {mas_lejana} (Distancia: {mas_lejana.distancia(Estrella(0,0,0)):.2f})")

if __name__ == "__main__":
    main()