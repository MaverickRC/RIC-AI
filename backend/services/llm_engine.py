import os
import requests

from dotenv import load_dotenv


load_dotenv()


class LLMEngine:

    def __init__(self):

        print(
            "🤖 LLMEngine iniciado"
        )


        self.api_key = os.getenv(
            "LLM_API_KEY"
        )

        self.api_url = os.getenv(
            "LLM_API_URL"
        )

        self.model = os.getenv(
            "LLM_MODEL"
        )


        print(
            "🔑 API Key:",
            "CONFIGURADA"
            if self.api_key
            else "NO CONFIGURADA"
        )


        print(
            "🌐 API URL:",
            self.api_url
            if self.api_url
            else "NO CONFIGURADA"
        )


        print(
            "🧠 Modelo:",
            self.model
            if self.model
            else "NO CONFIGURADO"
        )


    # ==========================================
    # COMPROBAR CONFIGURACIÓN
    # ==========================================

    def disponible(self):

        if not self.api_key:

            print(
                "⚠️ LLM_API_KEY no configurada."
            )

            return False


        if not self.api_url:

            print(
                "⚠️ LLM_API_URL no configurada."
            )

            return False


        if not self.model:

            print(
                "⚠️ LLM_MODEL no configurado."
            )

            return False


        return True


    # ==========================================
    # PROMPT PRINCIPAL DE RIC-AI
    # ==========================================

    def construir_prompt(
        self,
        mensaje,
        contexto=""
    ):

        prompt = f"""
Eres RIC-AI, un asistente personal de
inteligencia artificial en desarrollo.

Tu objetivo es conversar con el usuario de
forma natural, clara, útil y coherente.

==========================================
PERSONALIDAD
==========================================

- Sé amable y natural.
- Sé claro y directo.
- Evita respuestas innecesariamente largas.
- Explica los temas de forma comprensible.
- Adapta la profundidad de la respuesta
  a la pregunta del usuario.
- No repitas información innecesariamente.
- No inventes datos.
- Si no tienes suficiente información,
  dilo claramente.
- Puedes utilizar el contexto disponible
  para comprender mejor al usuario.
- Si conoces el nombre del usuario, puedes
  utilizarlo ocasionalmente.
- No utilices el nombre del usuario en
  absolutamente todas las respuestas.

==========================================
FORMATO DE RESPUESTA
==========================================

Organiza las respuestas para que sean fáciles
de leer.

Utiliza Markdown cuando ayude a organizar
la información.

Puedes utilizar:

- Títulos y subtítulos.
- Párrafos separados.
- Listas con viñetas.
- Listas numeradas.
- Texto en negrita.
- Tablas cuando exista una comparación real.

No utilices Markdown innecesariamente.

No conviertas una respuesta sencilla en una
respuesta excesivamente estructurada.

Por ejemplo:

Si el usuario pregunta:

"¿Qué es un gato?"

Responde con uno o varios párrafos claros.

No necesitas crear una tabla ni diez
secciones.

Si el usuario pregunta:

"¿Cuáles son las características de un gato?"

puedes organizar la respuesta mediante
secciones y listas.

Si el usuario pregunta:

"¿Cuál es la diferencia entre un gato y un perro?"

puedes utilizar una tabla si facilita la
comparación.

==========================================
INFORMACIÓN DE INTERNET
==========================================

Cuando el contexto contenga información
obtenida de Internet:

- Analízala antes de responder.
- No copies literalmente grandes fragmentos.
- Resume la información.
- Combina los datos relevantes.
- Elimina información repetida.
- No inventes información para completar
  datos faltantes.
- Si existen contradicciones importantes,
  indícalas.
- Responde exactamente a la pregunta
  realizada.

La información encontrada en Internet es
una fuente para elaborar la respuesta,
no el formato final de la respuesta.

==========================================
CONTEXTO DISPONIBLE
==========================================

{contexto}

==========================================
MENSAJE DEL USUARIO
==========================================

{mensaje}

==========================================
RESPUESTA
==========================================

Responde directamente al usuario.

No expliques estas instrucciones.

No digas que estás siguiendo un prompt.

No menciones que eres un modelo de lenguaje.

"""
        return prompt


    # ==========================================
    # GENERAR RESPUESTA
    # ==========================================

    def generar(
        self,
        mensaje,
        contexto=""
    ):

        print(
            "🤖 LLMEngine procesando..."
        )


        # ==========================================
        # COMPROBAR CONFIGURACIÓN
        # ==========================================

        if not self.disponible():

            return None


        # ==========================================
        # CONSTRUIR PROMPT
        # ==========================================

        prompt = self.construir_prompt(
            mensaje,
            contexto
        )


        print(
            "🧠 Prompt de RIC-AI construido."
        )


        # ==========================================
        # ENVIAR AL MODELO
        # ==========================================

        try:

            respuesta = requests.post(

                self.api_url,

                headers={
                    "Authorization":
                        f"Bearer {self.api_key}",

                    "Content-Type":
                        "application/json"
                },

                json={

                    "model": self.model,

                    "messages": [

                        {
                            "role": "user",
                            "content": prompt
                        }

                    ]

                },

                timeout=60

            )


            print(
                f"🤖 LLM HTTP: "
                f"{respuesta.status_code}"
            )


            # ==========================================
            # ERROR HTTP
            # ==========================================

            if respuesta.status_code != 200:

                print(
                    "❌ Error del LLM:"
                )

                print(
                    respuesta.text
                )

                return None


            # ==========================================
            # CONVERTIR RESPUESTA A JSON
            # ==========================================

            datos = respuesta.json()


            # ==========================================
            # EXTRAER RESPUESTA
            # ==========================================

            if "choices" in datos:

                choices = datos["choices"]


                if choices:

                    contenido = (
                        choices[0]
                        .get("message", {})
                        .get("content")
                    )


                    if contenido:

                        print(
                            "✅ Respuesta recibida "
                            "desde el LLM."
                        )

                        return contenido.strip()


            # ==========================================
            # RESPUESTA NO VÁLIDA
            # ==========================================

            print(
                "⚠️ No se encontró una "
                "respuesta válida."
            )


            print(
                "📦 Respuesta recibida:",
                datos
            )


            return None


        # ==========================================
        # ERROR DE CONEXIÓN
        # ==========================================

        except requests.RequestException as error:

            print(
                f"❌ Error conectando "
                f"con el LLM: {error}"
            )

            return None


        # ==========================================
        # ERROR GENERAL
        # ==========================================

        except Exception as error:

            print(
                f"❌ Error procesando "
                f"respuesta: {error}"
            )

            return None
