import requests

from bs4 import BeautifulSoup


class InternetTool:

    def __init__(self):

        print(
            "🌐 InternetTool iniciado"
        )


    # ==========================================
    # BUSCAR EN INTERNET
    # ==========================================

    def buscar(
        self,
        consulta
    ):

        print(
            f"🌐 Buscando en Internet: "
            f"{consulta}"
        )


        # ==========================================
        # VALIDAR CONSULTA
        # ==========================================

        if not consulta:

            return {
                "exito": False,
                "resultado":
                    "No se recibió ninguna consulta.",
                "contenido": ""
            }


        try:

            # ======================================
            # PETICIÓN WEB
            # ======================================

            respuesta = requests.get(

                "https://www.google.com/search",

                params={
                    "q": consulta
                },

                headers={
                    "User-Agent":
                        "Mozilla/5.0"
                },

                timeout=10
            )


            print(
                f"🌐 HTTP Status: "
                f"{respuesta.status_code}"
            )


            # ======================================
            # COMPROBAR RESPUESTA
            # ======================================

            if respuesta.status_code != 200:

                return {
                    "exito": False,
                    "resultado":
                        "No se pudo acceder "
                        "a Internet.",
                    "contenido": ""
                }


            # ======================================
            # ANALIZAR HTML
            # ======================================

            soup = BeautifulSoup(
                respuesta.text,
                "html.parser"
            )


            # ======================================
            # ELIMINAR ELEMENTOS INNECESARIOS
            # ======================================

            for elemento in soup(
                [
                    "script",
                    "style",
                    "noscript"
                ]
            ):

                elemento.decompose()


            # ======================================
            # EXTRAER TEXTO
            # ======================================

            texto = soup.get_text(
                separator=" ",
                strip=True
            )


            # ======================================
            # LIMPIAR ESPACIOS
            # ======================================

            texto = " ".join(
                texto.split()
            )


            print(
                f"🧹 Texto limpio: "
                f"{len(texto)} caracteres."
            )


            # ======================================
            # LIMITAR INFORMACIÓN
            # ======================================

            texto_util = texto[:15000]


            return {

                "exito": True,

                "resultado":
                    "Información obtenida "
                    "correctamente.",

                "contenido":
                    texto_util
            }


        except requests.RequestException as error:

            print(
                f"❌ Error de Internet: "
                f"{error}"
            )


            return {

                "exito": False,

                "resultado":
                    "Ocurrió un error al "
                    "conectarse a Internet.",

                "contenido": ""
            }


        except Exception as error:

            print(
                f"❌ Error procesando "
                f"la página: {error}"
            )


            return {

                "exito": False,

                "resultado":
                    "Ocurrió un error "
                    "procesando la información.",

                "contenido": ""
            }
