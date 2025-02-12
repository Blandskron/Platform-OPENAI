# Introducción al Proyecto de Análisis de Documentación de OpenAI

En este proyecto, nos dedicaremos al análisis exhaustivo de la documentación proporcionada por OpenAI con el fin de explorar y ejecutar las múltiples posibilidades de uso que ofrece su plataforma para desarrolladores. El objetivo principal es familiarizarnos con la API de OpenAI, conocida como "OpenAI Developer Platform", y comprender cómo podemos integrarla en diversas aplicaciones.

## OpenAI Developer Platform

OpenAI ofrece una API poderosa y flexible que permite a los desarrolladores crear aplicaciones inteligentes utilizando los modelos avanzados de inteligencia artificial desarrollados por la organización. Este proyecto se centrará en cómo configurar el entorno de desarrollo y realizar la primera solicitud a la API de OpenAI en cuestión de minutos, lo cual es abordado en la sección "Developer Quickstart" de la documentación.

## Primeros Pasos: Configuración del Entorno

Para comenzar a interactuar con la API de OpenAI utilizando Python, es crucial configurar adecuadamente el entorno de desarrollo. Recomendamos usar `venv`, el entorno virtual de Python, para gestionar mejor las dependencias del proyecto. A continuación, se describe el proceso paso a paso:

1. **Crear un Entorno Virtual:**

   ```bash
   python -m venv myenv
   source myenv/bin/activate  # En sistemas Unix
   # .\myenv\Scripts\activate  # En Windows
   ```

2. **Instalar las Dependencias Necesarias:**
   Asegúrate de tener el paquete `openai` instalado dentro del entorno virtual:

   ```bash
   pip install openai
   ```

3. **Configurar la API Key:**
   La clave de API es necesaria para autenticar las solicitudes. Es una práctica recomendada almacenarla en una variable de entorno para evitar exponerla dentro del código. Puedes hacerlo de la siguiente manera:

   - **GNU/Linux y macOS:**

     ```bash
     export OPENAI_API_KEY='tu_clave_api_aqui'
     ```

   - **Windows:**
     ```cmd
     set OPENAI_API_KEY=tu_clave_api_aqui
     ```

## Ejemplo de Uso de la API

El siguiente fragmento de código muestra cómo realizar una consulta básica utilizando el modelo GPT-4o de OpenAI. En este ejemplo, solicitamos la creación de un haiku sobre inteligencia artificial:

```python
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
completion = client.chat.completions.create(
    model="gpt-4o",
    store=True,
    messages=[
        {"role": "user", "content": "write a haiku about ai"}
    ]
)

print(completion.choices[0].message.content)
```

Con este proyecto, se espera que los desarrolladores ganen la confianza necesaria para aprovechar al máximo las capacidades de OpenAI, integrando estas herramientas avanzadas en sus aplicaciones innovadoras. A medida que avancemos, nos sumergiremos en diferentes casos de uso y exploraremos las mejores prácticas para el desarrollo con OpenAI.
