from Dialogo import Dialogo
from Formatear import FormateadorZen

def main():
    texto_original = (
        "un día que el viento soplaba con fuerza#"
        "mira como se mueve aquella banderola -dijo un monje#"
        "lo que se mueve es el viento -respondió otro monje#"
        "ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro#"
    )
    
    # Procesamiento completo
    dialogo = Dialogo(texto_original)
    dialogo.procesar()
    
    formateador = FormateadorZen()
    resultado = formateador.formatear(dialogo.fragmentos)
    
    # Mostrar resultado con formato mejorado
    print("\nDIÁLOGO ZEN\n")
    print(resultado)
    print()

if __name__ == "__main__":
    main()