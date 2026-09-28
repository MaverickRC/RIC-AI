class Brain:

    def __init__(self):

        print(
            "🧠 Cerebro de RIC-AI iniciado"
        )


    def pensar(
        self,
        mensaje,
        historial=None
    ):

        texto = mensaje.lower().strip()

        print(
            "🧠 Analizando mensaje..."
        )


        # ==========================================
        # CONTEXTO DISPONIBLE
        # ==========================================

        if historial:

            print(
                "🔎 Brain tiene contexto disponible."
            )

        else:

            print(
                "🔎 Brain no tiene contexto."
            )


        # ==========================================
        # APRENDER NOMBRE
        # ==========================================
        #
        # Ejemplos:
        #
        # "me llamo Ricardo"
        # "mi nombre es Ricardo"
        # "puedes llamarme Ricardo"
        # "llámame Ricardo"
        # "puedes decirme Ricardo"
        #
        # ==========================================

        if texto.startswith(
            "me llamo "
        ):

            return {
                "accion": "aprender",
                "tipo": "nombre",
                "importancia": 3
            }


        if texto.startswith(
            "mi nombre es "
        ):

            return {
                "accion": "aprender",
                "tipo": "nombre",
                "importancia": 3
            }


        if texto.startswith(
            "puedes llamarme "
        ):

            return {
                "accion": "aprender",
                "tipo": "nombre",
                "importancia": 3
            }


        if texto.startswith(
            "puedes decirme "
        ):

            return {
                "accion": "aprender",
                "tipo": "nombre",
                "importancia": 3
            }


        if texto.startswith(
            "llámame "
        ):

            return {
                "accion": "aprender",
                "tipo": "nombre",
                "importancia": 3
            }


        if texto.startswith(
            "llamame "
        ):

            return {
                "accion": "aprender",
                "tipo": "nombre",
                "importancia": 3
            }


        # ==========================================
        # MEMORIA EXPLÍCITA
        # ==========================================
        #
        # Ejemplos:
        #
        # "recuerda que mi comida favorita es pizza"
        # "recuerda mi color favorito es blanco"
        # "no olvides que estudio Ingeniería en TICS"
        # "para que no se te olvide, mi color favorito es blanco"
        #
        # ==========================================

        frases_memoria = [

            "recuerda que ",
            "recuerda ",

            "no olvides que ",
            "no olvides ",

            "para que no se te olvide, ",
            "para que no se te olvide ",

            "para que no olvides, ",
            "para que no olvides ",

            "ten presente que ",
            "ten presente ",

            "quiero que recuerdes que ",
            "quiero que recuerdes ",

            "guarda que ",
            "guarda ",

            "memoriza que ",
            "memoriza "

        ]


        for frase in frases_memoria:

            if texto.startswith(frase):

                print(
                    f"🧠 Memoria explícita detectada: "
                    f"{frase}"
                )

                return {
                    "accion": "aprender",
                    "tipo": "memoria_explicita",
                    "importancia": 3
                }


        # ==========================================
        # APRENDER DATO PERSONAL
        # ==========================================

        if texto.startswith("mi "):

            if (
                " es " in texto
                or " son " in texto
            ):

                return {
                    "accion": "aprender",
                    "tipo": "dato",
                    "importancia": 3
                }


        # ==========================================
        # APRENDER PREFERENCIAS
        # ==========================================

        if (
            texto.startswith("me gusta ")
            or texto.startswith("me encanta ")
            or texto.startswith("prefiero ")
            or texto.startswith("odio ")
        ):

            return {
                "accion": "aprender",
                "tipo": "preferencia",
                "importancia": 2
            }


        # ==========================================
        # RECORDAR NOMBRE
        # ==========================================

        if (
            "como me llamo" in texto
            or "cómo me llamo" in texto
            or "cual es mi nombre" in texto
            or "cuál es mi nombre" in texto
        ):

            return {
                "accion": "recordar",
                "tipo": "nombre"
            }


        # ==========================================
        # RECORDAR DATO
        # ==========================================

        if (
            texto.startswith("cual es mi ")
            or texto.startswith("cuál es mi ")
        ):

            return {
                "accion": "recordar",
                "tipo": "dato"
            }


        # ==========================================
        # BUSCAR CONTEXTO / MEMORIA RELACIONADA
        # ==========================================

        if (
            "que te dije sobre " in texto
            or "qué te dije sobre " in texto

            or "que hablamos sobre " in texto
            or "qué hablamos sobre " in texto

            or "recuerdas lo de " in texto
            or "recuerdas cuando hablamos de " in texto

            or "que recuerdas sobre " in texto
            or "qué recuerdas sobre " in texto

            or "que recuerdas de " in texto
            or "qué recuerdas de " in texto

            or "que sabes sobre " in texto
            or "qué sabes sobre " in texto

            or "que sabes de " in texto
            or "qué sabes de " in texto
        ):

            return {
                "accion": "buscar_contexto",
                "tipo": "tema"
            }


        # ==========================================
        # RECORDAR CONTEXTO GENERAL
        # ==========================================

        if (
            "lo que te dije" in texto
            or "eso que te dije" in texto
            or "que te dije antes" in texto
            or "de que hablamos" in texto
            or "de qué hablamos" in texto
        ):

            return {
                "accion": "contexto",
                "tipo": "historial"
            }


        # ==========================================
        # BUSCAR EN INTERNET
        # ==========================================

        if (
            "busca en internet" in texto
            or "buscar en internet" in texto
            or "busca en la web" in texto
            or "busca en google" in texto
            or "investiga en internet" in texto
        ):

            consulta = texto


            consulta = consulta.replace(
                "busca en internet",
                ""
            )


            consulta = consulta.replace(
                "buscar en internet",
                ""
            )


            consulta = consulta.replace(
                "busca en la web",
                ""
            )


            consulta = consulta.replace(
                "busca en google",
                ""
            )


            consulta = consulta.replace(
                "investiga en internet",
                ""
            )


            consulta = consulta.strip()


            return {
                "accion": "buscar_internet",
                "consulta": consulta
            }


        # ==========================================
        # CONVERSACIÓN NORMAL
        # ==========================================

        return {
            "accion": "conversar"
        }
