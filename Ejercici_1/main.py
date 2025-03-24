from lanzador import crear_estrellas, mostrar_info_estrellas, calcular_distancias, encontrar_mas_lejana


def main():
    print("=== SIMULACIÓN DEL UNIVERSO ===")
    estrellas = crear_estrellas()
    
    print("\n=== INFORMACIÓN DE ESTRELLAS ===")
    mostrar_info_estrellas(estrellas)
    
    print("\n=== DISTANCIAS ENTRE ESTRELLAS ===")
    calcular_distancias(estrellas)
    
    print("\n=== ESTRELLA MÁS LEJANA ===")
    encontrar_mas_lejana(estrellas)

if __name__ == "__main__":
    main()