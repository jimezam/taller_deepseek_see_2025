from src.content_generation_assistant.assistant import Assistant
import streamlit as st

def show() -> None:
    st.set_page_config(page_title="Asistente IA",
                       page_icon=":robot:",
                       layout="wide",
                       initial_sidebar_state="expanded",
    )

    providers = Assistant.get_provider_list()
    content_types = Assistant.get_content_types()

    st.title("Asistente de generación de contenido")
    st.sidebar.title("Opciones")
    st.sidebar.write("Configura aquí al asistente.")

    ai_provider = st.sidebar.selectbox(
        "Selecciona el proveedor IA",
        get_provider_names(providers),
        index=0
    )

    content_type = st.sidebar.selectbox(
        "Selecciona el tipo de contenido",
        get_content_types_names(content_types),
        index=0
    )

    st.write(f"Vamos a crear **{content_type}** con **{ai_provider}**.")

    context:str = st.text_area(
        "Escribe aquí el contexto de lo que deseas generar",
        "",
        height=200
    )

    generated_content:bool = False

    if(st.button("Generar contenido")):
        if(context):
            generated_content = True

            with st.spinner("Generando ..."):
                result:str = None

                try:
                    result = generate(providers, ai_provider, content_types, content_type, context)
                except Exception as e:
                    st.error(f"Ha ocurrido un error al generar el contenido: {e}")

                if(result):
                    show_result(result)
        else:
            st.warning("Debes especificar un contexto para generar el contenido")

    if not generated_content:
        show_content_type_info(content_types, content_type)

#######################################################################################

def generate(providers, ai_provider, content_types, content_type, context) -> str:
    provider_index = list(get_provider_names(providers)).index(ai_provider)
    content_type_index = list(get_content_types_names(content_types)).index(content_type)

    the_provider = providers[provider_index]()
    the_content_type = content_types[content_type_index]()

    return Assistant.generate(
        the_provider,
        the_content_type,
        context
    )

def show_result(result:str) -> None:
    st.success("Contenido generado exitosamente")
    st.header("Resultado")
    st.markdown(result)

def show_content_type_info(content_types, content_type) -> None:
    content_type_index = list(get_content_types_names(content_types)).index(content_type)
    the_content_type = content_types[content_type_index]()

    st.header(f"Tipo de contenido: \"{the_content_type.get_name()}\"")
    st.subheader("Descripción")
    st.markdown(the_content_type.get_description())
    st.subheader("Ejemplo")
    st.markdown(the_content_type.get_example())

def get_provider_names(providers:list) -> list:
    return (provider().get_provider_name().capitalize() for provider in providers)

def get_content_types_names(content_types:list) -> list:
    return (content_type().get_name().capitalize() for content_type in content_types)
