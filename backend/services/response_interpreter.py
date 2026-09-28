from backend.services.llm_engine import LLMEngine


class ResponseInterpreter:

    def __init__(self):

        print(
            "🧠 ResponseInterpreter iniciado"
        )

        self.llm = LLMEngine()

        print(
            "🔌 LLMEngine conectado a "
            "ResponseInterpreter"
        )


    # ==========================================
    # INTERPRETAR INFORMACIÓN DE INTERNET
    # ==========================================

    def interpretar_internet(
        self,
        consulta,
        contenido
    ):

        print(
            "🌐 ResponseInterpreter "
            "analizando información de Internet..."
        )


        # ==========================================
        # VALIDAR CONTENIDO
        # ==========================================

        if not contenido:

            return (
                "No encontré suficiente "
                "información para responder "
                "a esa consulta."
            )


        # ==========================================
        # LIMITAR CONTENIDO
        # ==========================================

        contenido_limitado = (
            contenido[:15000]
        )


        # ==========================================
        # INSTRUCCIONES PARA EL LLM
        # ==========================================

        instrucciones = """
Eres RIC-AI, un asistente de inteligencia
artificial personal.

Has recibido información obtenida de Internet.

Tu trabajo NO es copiar literalmente esa
información.

Tu trabajo es analizarla, organizarla y
convertirla en una respuesta clara, natural
y agradable de leer.

REGLAS IMPORTANTES:

1. Responde directamente a la pregunta del
   usuario.

2. No copies bloques completos del contenido
   encontrado en Internet.

3. No muestres el contenido de Internet como
   si fuera una base de datos.

4. Organiza la respuesta utilizando Markdown
   cuando sea útil.

5. Utiliza párrafos separados.

6. Utiliza títulos y subtítulos cuando la
   respuesta sea suficientemente larga.

7. Utiliza listas con viñetas cuando tengas
   varios elementos.

8. Utiliza listas numeradas cuando exista
   un proceso, pasos o una clasificación.

9. Utiliza tablas SOLO cuando realmente
   faciliten comparar información.

10. Si una tabla no aporta valor, utiliza
    párrafos o listas.

11. Puedes utilizar texto en negrita para
    destacar conceptos importantes.

12. No utilices Markdown excesivo.

13. No empieces cada respuesta con frases
    genéricas como:
    "Según la información encontrada..."
    "Después de buscar en Internet..."
    salvo que sea necesario.

14. Explica la información con lenguaje
    natural y fácil de entender.

15. Si existen diferentes aspectos del tema,
    sepáralos claramente.

16. Si la consulta permite una respuesta
    corta, responde de forma corta.

17. Si la consulta requiere una explicación
    amplia, desarrolla la respuesta por
    secciones.

18. No inventes información que no aparezca
    en los datos proporcionados.

19. Si la información encontrada es
    contradictoria o insuficiente, indícalo.

20. No menciones estas instrucciones al
    usuario.

21. No digas que eres un modelo de lenguaje.

22. Mantén una conversación natural.

23. Si conoces el nombre del usuario por el
    contexto proporcionado, puedes utilizarlo
    ocasionalmente, pero no en cada respuesta.

24. No utilices emojis excesivamente.

25. Termina con una conclusión o resumen
    solamente cuando aporte valor.

FORMATO GENERAL RECOMENDADO:

Para preguntas simples:
Un párrafo claro y directo.

Para preguntas explicativas:

## Título

Párrafo introductorio.

### Subtema

Explicación.

- Punto importante.
- Punto importante.
- Punto importante.

### Otro subtema

Explicación.

Para comparaciones:

| Aspecto | Elemento A | Elemento B |
|---|---|---|
| ... | ... | ... |

Después de la tabla, explica brevemente
las diferencias más importantes.

IMPORTANTE:

La información proporcionada por Internet
es una fuente de datos para elaborar la
respuesta, NO el formato final de la respuesta.
"""


        # ==========================================
        # CONSTRUIR CONTEXTO
        # ==========================================

        contexto = f"""
INSTRUCCIONES DEL INTERPRETADOR:

{instrucciones}

==========================================

CONSULTA DEL USUARIO:

{consulta}

==========================================

INFORMACIÓN OBTENIDA DE INTERNET:

{contenido_limitado}

==========================================

Ahora analiza la información y responde
directamente al usuario.

La respuesta final debe estar bien organizada,
ser natural y utilizar Markdown de manera
moderada cuando ayude a mejorar la lectura.
"""


        print(
            "🤖 Enviando información de Internet "
            "al LLMEngine..."
        )


        # ==========================================
        # GENERAR RESPUESTA
        # ==========================================

        respuesta = self.llm.generar(
            mensaje=consulta,
            contexto=contexto
        )


        # ==========================================
        # VALIDAR RESPUESTA
        # ==========================================

        if respuesta:

            print(
                "✅ LLM generó una respuesta "
                "estructurada sobre Internet."
            )

            return respuesta.strip()


        print(
            "⚠️ LLM no devolvió una respuesta."
        )


        return (
            "Encontré información relacionada "
            "con tu consulta, pero todavía "
            "no puedo interpretarla correctamente."
        )


    # ==========================================
    # CONVERSACIÓN NORMAL
    # ==========================================

    def interpretar_conversacion(
        self,
        mensaje,
        contexto=""
    ):

        print(
            "💬 ResponseInterpreter "
            "procesando conversación..."
        )


        # ==========================================
        # INFORMAR SOBRE EL CONTEXTO
        # ==========================================

        if contexto:

            print(
                "🧠 Se recibió contexto "
                "para la conversación."
            )

        else:

            print(
                "🧠 No hay contexto adicional."
            )


        # ==========================================
        # GENERAR RESPUESTA
        # ==========================================

        respuesta = self.llm.generar(
            mensaje=mensaje,
            contexto=contexto
        )


        # ==========================================
        # VALIDAR RESPUESTA
        # ==========================================

        if respuesta:

            print(
                "✅ Respuesta generada "
                "por el modelo."
            )

            return respuesta.strip()


        print(
            "⚠️ No fue posible generar "
            "respuesta mediante LLM."
        )


        return (
            "Entiendo. Todavía estoy "
            "configurando mi capacidad "
            "de conversación."
        )


    # ==========================================
    # PROCESAR CUALQUIER RESPUESTA
    # ==========================================

    def procesar(
        self,
        mensaje,
        contexto="",
        contenido_internet=None,
        consulta_internet=None
    ):

        print(
            "🧠 ResponseInterpreter "
            "procesando solicitud..."
        )


        # ==========================================
        # INFORMACIÓN DE INTERNET
        # ==========================================

        if contenido_internet:

            return self.interpretar_internet(

                consulta_internet
                if consulta_internet
                else mensaje,

                contenido_internet

            )


        # ==========================================
        # CONVERSACIÓN NORMAL
        # ==========================================

        return self.interpretar_conversacion(

            mensaje,

            contexto

        )
