from src.content_generation_assistant.content_type import ContentType
from src.ia.providers.provider import Provider

class ShortLovePoem(ContentType):
    def __init__(self):
        super().__init__()

    def get_id(self) -> str:
        return "content_types.short_love_poem"

    def get_name(self) -> str:
        return "Poema corto de amor"

    def get_description(self) -> str:
        return "Genera un poema corto de amor"

    def get_example(self) -> str:
        return """
        """

    def get_context(self) -> str:
        return """
            Escribe una poesía breve, romántica, creativa y original para enamorar
            a mi pareja.
            La poesía para dedicar a alguien especial, debe ser corta (4–6 versos),
            fácil de compartir por mensaje, en redes sociales o decir en voz alta,
            y debe transmitir amor genuino. Si es posible, incluye una metáfora
            bonita o una imagen visual que la haga aún más especial.
            Usa un estilo tierno y sincero. Inspírate en los detalles provistos por
            el usuario.
        """

    def get_preferred_temperature(self) -> float:
        return Provider.MAX_TEMPERATURE