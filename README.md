# Ejercicio práctico

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