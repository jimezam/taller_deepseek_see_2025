# Actividad práctica

Esta aplicación de demostración se desarrolló como parte del curso de "Crear Soluciones con Inteligencia Artificial usando el API de DeepSeek" hecho con la Sociedad Ecuatoriana de Estadística.

## Descripción

El software le permite al usuario elegir el proveedor de IA deseado (este incluye el modelo en su configuración), el tipo de contenido a utilizarse y proveer información adicional en un texto abierto.

Los proveedores implementados por ahora son:

- Anthropic
- DeepSeek
- Mistral

Y los tipos de contenido existentes por ahora son:

- Carta de presentación personal (`PersonalCoverLetter`)
- Poema corto de amor (`ShortLovePoem`)
- Código fuente (`SourceCode`)
- Guion de un TikTok (`TiktokScript`)

## Instalación

Clonar el proyecto de este repositorio.

```
$ git clone https://github.com/jimezam/taller_deepseek_see_2025.git
```

Acceder al directorio de trabajo.

```
$ cd taller_deepseek_see_2025
```

Crear el ambiente virtual.

```
$ python -m venv venv
```

Activar el ambiente virtual.

```
$ source venv/bin/activate
```

Debe tenerse en cuenta que esta acción se realiza de la siguiente manera en Windows.

```
> .\venv\Scripts\activate
```

Instalar las librerías requeridas.

```
$ pip install -r requirements.txt
```

Crear el archivo de configuración.

```
$ cp .env.example .env
```

Editar el archivo `.env` y complementar la siguiente información.

- DEEPSEEK_API_KEY  
  DEEPSEEK_BASE_URL  
  DEEPSEEK_MODEL

- MISTRAL_API_KEY  
  MISTRAL_MODEL

- ANTHROPIC_API_KEY  
  ANTHROPIC_MODEL

Ejecutar la aplicación a través de la interfaz web (Streamlit).

```
$ streamlit run main.py
```

Abrir un navegador y acceder a la URL `http://localhost:8501` o la que indique el servicio.

## Interfaz de usuario

La interfaz de usuario se encuentra dividida en dos partes, la barra lateral (izquierda) y el contenido (centro).

En la barra lateral, el usuario puede elegir el proveedor de IA y el tipo de contenido que desea utilizar para la generación del contenido.

En la parte central, el usuario puede **proveer del contexto** necesario para complementar la generación del tipo de contenido solicitado.  **No es necesario escribir el prompt**, este viene definido por el tipo de contenido elegido.

![Imagen #1](/docs/images/screenshot-1.png)

En la parte central inferior se puede apreciar la descripción y un ejemplo del tipo de contenido elegido.

Una vez se solicita la generación de contenido, esta es mostrada en la interfaz como se muestra a continuación.

![Imagen #1](/docs/images/screenshot-2.png)

## Diseño

se utilizaron los siguientes patrones de diseño para el desarrollo de esta aplicación.

- **Factory Method**: para la gestión de los IA `providers` y los `content_types`.
- **Strategy**: para la selección dinámica del `content_type` a utilizar por parte del `provider` elegido.
- **Template Method**: en las clases abstractas de `provider` y `content_type` que determinan la estructura conocida de estas clases.
- **MVC**: se utiliza una estructura similar a este patrón, en la cual el Modelo corresponde con `provider` y `content_type`, la Vista con el archivo `ui.py` (basado en Streamlit) y el controlador es la clase `Assistant`, la cual termina actuando como Frontal ya que es el camino obligado para cualquier interacción del usuario.

En general, se aprovechan los siguientes patrones SOLID.

- **Single Responsibility Principle (SRP):**  
  Cada módulo tiene una responsabilidad única.
- **Open/Closed Principle (OCP):**  
  Es posible agregar nuevos proveedores o tipos de contenido sin modificar el código existente.  (Aún es mejorable este aspecto).
- **Dependency Inversion Principle (DIP):**  
  Las funciones y clases dependen de abstracciones (interfaces) en lugar de implementaciones concretas.

## Herramientas

- Python
- Streamlit
- APIs
    - Anthropic
    - DeepSeek
    - Mistral

## Implementación

Es posible agregar nuevos proveedores de IA creando clases nuevas para ellos que hereden de `src.ia.providers.Provider` y se ubiquen en directorios bajo el paquete `src.ia.providers.providers`.

De manera similar, es posible agregar nuevos tipos de contenido creando nuevas clases que hereden de `src.content_generation_assistant.ContentType` y se ubiquen en directorios bajo el paquete `src.content_generation_assistant.content_types`.

```
├── main.py -- función principal
├── README.md  -- este documento
├── requirements.txt  -- listado de librerías requeridas
└── src
    ├── config.py -- lector de valores de configuración
    ├── content_generation_assistant
    │   ├── assistant.py -- clase controladora del asistente
    │   ├── content_type.py -- clase base para los tipos de contenido
    │   ├── content_types
    │       ├── personal_cover_letter.py
    │       ├── short_love_poem.py
    │       ├── source_code.py
    │       └── tiktok_script.py
    ├── ia
    │   └── providers
    │       ├── anthropic
    │       │   └── anthropic_provider.py
    │       ├── deepseek
    │       │   └── deepseek_provider.py
    │       ├── mistral
    │       │   └── mistral_provider.py
    │       └── provider.py - clase base para los proveedores de IA
    └── ui.py - interfaz de usuario web
```

