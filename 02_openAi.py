import os
from openai import OpenAI

# Inicializar el cliente de OpenAI con la clave de API
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def interact_with_gpt():
    print("Bienvenido al chat con GPT-4o de OpenAI!")
    while True:
        # Pedir al usuario que escriba un mensaje
        user_message = input("Escribe tu mensaje (o 'salir' para terminar): ")
        
        # Verificar si el usuario desea salir
        if user_message.lower() == 'salir':
            print("Gracias por usar el chat de OpenAI. ¡Hasta luego!")
            break
        
        # Crear una nueva solicitud de completado al modelo
        completion = client.chat.completions.create(
            model="gpt-4o",
            store=True,
            messages=[
                {"role": "user", "content": user_message}
            ]
        )
        
        # Imprimir la respuesta del modelo
        print("Modelo GPT-4o:", completion.choices[0].message.content)

# Llamar la función para empezar la interacción
if __name__ == "__main__":
    interact_with_gpt()