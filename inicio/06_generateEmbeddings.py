from openai import OpenAI

def main():
    # Inicializamos el cliente de OpenAI
    client = OpenAI()

    print("Bienvenido al generador de incrustaciones de texto de OpenAI.")
    print("Puedes ingresar texto para generar su representación vectorial.")
    print("Escribe 'salir' para terminar la sesión.\n")

    while True:
        # Solicitamos un texto al usuario
        user_input = input("Ingresa el texto para generar su incrustación: ")

        # Condición para salir del bucle
        if user_input.lower() == 'salir':
            print("Adiós, ¡hasta la próxima!")
            break

        try:
            # Generamos incrustación a partir del texto del usuario
            response = client.embeddings.create(
                model="text-embedding-3-large",
                input=user_input
            )

            # Imprimimos la incrustación generada
            print("Incrustación generada:", response)

        except Exception as e:
            print(f"Ha ocurrido un error al generar la incrustación: {e}")

if __name__ == "__main__":
    main()