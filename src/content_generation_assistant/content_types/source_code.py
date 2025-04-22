from src.content_generation_assistant.content_type import ContentType

class SourceCode(ContentType):
    def __init__(self):
        super().__init__()

    def get_id(self) -> str:
        return "content_types.source_code"

    def get_name(self) -> str:
        return "Código fuente"

    def get_description(self) -> str:
        return "Código fuente de un programa o script en un lenguaje de programación específico"

    def get_example(self) -> str:
        return """
            Crear un programa en Python que le pida al usuario un valor entero y a partir
            de el, calcule la suma de todos los números pares y la multiplicatoria de
            todos los numeros impares, desde 0 hasta el número ingresado.
            El programa debe mostrar el resultado en pantalla.
        """

    def get_context(self) -> str:
        return """
            Crear un código fuente completo, funcional y bien comentado en el lenguaje
            indicado por el usuario que resuelva los requerimientos indicados. El código
            debe ser claro, eficiente y fácil de entender, además debe estar comentado,
            ser modular y seguir las buenas prácticas del lenguaje y del paradigma.
            No incluyas notas al pie, ni referencias a otros documentos o información
            adicional, solo el código fuente que pueda ser copiado y pegado en un editor
            y que compile y ejecute sin errores.
        """

    def get_preferred_temperature(self) -> float:
        return 0