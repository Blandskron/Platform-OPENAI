# Guía Rápida para Desarrolladores

Aprende cómo hacer tu primera solicitud a la API.

La API de OpenAI proporciona una interfaz sencilla para modelos de IA de última generación en procesamiento de lenguaje natural, generación de imágenes, búsqueda semántica y reconocimiento de voz. Sigue esta guía para aprender a generar respuestas similares a las humanas a partir de mensajes en lenguaje natural, crear incrustaciones vectoriales para búsquedas semánticas y generar imágenes a partir de descripciones textuales.

## Crear y Exportar una Clave de API

Crea una clave de API en el panel de control [aquí](#), que usarás para acceder a la API de manera segura. Almacena la clave en un lugar seguro, como un archivo `.zshrc` u otro archivo de texto en tu computadora. Una vez que hayas generado una clave de API, expórtala como una variable de entorno en tu terminal.

### macOS / Linux y Windows

Para exportar una variable de entorno en PowerShell:

```shell
setx OPENAI_API_KEY "tu_clave_de_api_aquí"
```

## Realiza tu Primera Solicitud a la API

Con tu clave de API de OpenAI exportada como una variable de entorno, estás listo para realizar tu primera solicitud a la API. Puedes usar la API REST directamente con el cliente HTTP de tu elección o usar uno de nuestros SDK oficiales, como se muestra a continuación.

### JavaScript / Python / curl

Para usar la API de OpenAI en Python, puedes usar el SDK oficial de OpenAI para Python. Comienza instalando el SDK con pip:

#### Instalar el SDK de OpenAI con pip

```shell
pip install openai
```

Con el SDK de OpenAI instalado, crea un archivo llamado `ejemplo.py` y copia uno de los siguientes ejemplos en él:

### Generar Texto / Generar una Imagen / Crear Incrustaciones Vectoriales

#### Crear una Respuesta Simil-Humana a un Mensaje

```python
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Eres un asistente útil."},
        {"role": "user", "content": "Escribe un haiku sobre la recursión en programación."}
    ]
)

print(completion.choices[0].message)
```

Ejecuta el código con `python ejemplo.py`. ¡En unos momentos, deberías ver el resultado de tu solicitud a la API!

--- 

Esta guía proporciona un enfoque estructurado y claro para comenzar a trabajar con la API de OpenAI, asegurando que puedas integrar rápidamente capacidades de inteligencia artificial avanzadas en tus proyectos.