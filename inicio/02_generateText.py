from openai import OpenAI

def main():
    # Inicializamos el cliente de OpenAI
    client = OpenAI()

    print("Bienvenido al asistente interactivo de OpenAI.")
    print("Puedes escribir tu pregunta o mensaje, y te responderé.")
    print("Escribe 'salir' para terminar la sesión.\n")

    while True:
        # Solicitamos un mensaje del usuario
        user_input = input("Tú: ")

        # Condición para salir del bucle
        if user_input.lower() == 'salir':
            print("Adiós, ¡hasta la próxima!")
            break

        # Creamos una solicitud de completado usando el input del usuario
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Eres un asistente útil."},
                {"role": "user", "content": user_input}
            ]
        )

        # Imprimimos la respuesta generada por el modelo
        response = completion.choices[0].message.content
        print(f"Asistente: {response}")

if __name__ == "__main__":
    main()