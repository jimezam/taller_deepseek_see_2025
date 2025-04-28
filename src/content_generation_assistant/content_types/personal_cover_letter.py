from src.content_generation_assistant.content_type import ContentType

class PersonalCoverLetter(ContentType):
    def __init__(self):
        super().__init__()

    def get_id(self) -> str:
        return "content_types.personal_cover_letter"

    def get_name(self) -> str:
        return "Carta de presentación personal"

    def get_description(self) -> str:
        return "Crea una carta de presentación personal para un puesto de trabajo específico"

    def get_example(self) -> str:
        return """Mi nombre es Pepe, estoy interesado en el puesto de Gerente 
General en ACME.  Tengo experiencia en lavar, cocinar y planchar, y cuento con 
habilidades como quejarme sólo lo necesario, oler rico y bañarme por las 
mañanas."""

    def get_context(self) -> str:
        return """Eres un redactor profesional, tu tarea es redactar una carta de
presentación personal para un puesto de trabajo. Para ello, utilizarás
un lenguaje y tono formal apropiado para el ámbito laboral, aprovechando la
totalidad de la información proporcionada por el usuario y no incluirás campos
genéricos o abiertos que requieran información adicional, si no se cuenta con un
dato específico, este no se deberá incluir en la carta.  Se deben resaltar las cualidades, 
habilidades y experiencias técnicas y laborales del proponente, suavizando cualquier
característica, actividad o experiencia que pueda ser considerada negativa.
La carta debe ser persuasiva y convincente, destacando por qué el solicitante es un
buen candidato. Además, la adaptarás a un formato de carta de presentación, el cual
debe incluir una introducción, un cuerpo que detalle las habilidades y experiencias
relevantes del solicitante, y una conclusión que invite al lector a considerar al
solicitante para el puesto. Asegúrate de que la carta sea clara, concisa y
persuasiva, esté bien estructurada y sea fácil de leer. Utiliza un lenguaje
profesional y evita jerga o tecnicismos innecesarios. Además, asegúrate de
que la carta sea única y no una plantilla genérica. No incluyas notas al pie,
ni referencias a otros documentos o información adicional."""

    def get_preferred_temperature(self) -> float:
        return 0.7