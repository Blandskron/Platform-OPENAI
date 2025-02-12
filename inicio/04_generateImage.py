from openai import OpenAI

def main():
    # Inicializamos el cliente de OpenAI
    client = OpenAI()

    print("Bienvenido al generador de imágenes de OpenAI.")
    print("Describe la imagen que deseas generar.")
    print("Escribe 'salir' para terminar la sesión.\n")

    while True:
        # Solicitamos un prompt al usuario
        user_prompt = input("Describe la imagen que deseas: ")

        # Condición para salir del bucle
        if user_prompt.lower() == 'salir':
            print("Adiós, ¡hasta la próxima!")
            break

        try:
            # Generamos imágenes a partir del prompt del usuario
            response = client.images.generate(
                prompt=user_prompt,
                n=2,  # Número de imágenes a generar
                size="1024x1024"  # Tamaño de las imágenes
            )

            # Imprimimos las URLs de las imágenes generadas
            for idx, image in enumerate(response.data):
                print(f"Imagen {idx + 1}: {image.url}")

        except Exception as e:
            print(f"Ha ocurrido un error al generar la imagen: {e}")

if __name__ == "__main__":
    main()