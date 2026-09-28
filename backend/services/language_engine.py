class LanguageEngine:


    # ==========================================
    # EXTRAER MEMORIA
    # ==========================================

    def extraer_memoria(
        self,
        mensaje
    ):

        texto = mensaje.lower().strip()


        # ==========================================
        # LIMPIAR PETICIONES EXPLÍCITAS DE MEMORIA
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


        mensaje_limpio = mensaje.strip()
        texto_limpio = texto


        for frase in frases_memoria:

            if texto_limpio.startswith(frase):

                mensaje_limpio = mensaje_limpio[
                    len(frase):
                ].strip()

                texto_limpio = (
                    mensaje_limpio
                    .lower()
                    .strip()
                )

                print(
                    f"🧠 Instrucción de memoria "
                    f"eliminada: {frase}"
                )

                break


        # ==========================================
        # NOMBRE
        # ==========================================

        frases_nombre = [

            "me llamo ",
            "mi nombre es ",
            "puedes llamarme ",
            "llámame ",
            "llamame ",
            "quiero que me llames "

        ]


        for frase in frases_nombre:

            if texto_limpio.startswith(frase):

                nombre = mensaje_limpio[
                    len(frase):
                ].strip()


                if nombre:

                    return {
                        "clave": "nombre",
                        "valor": nombre
                    }


        # ==========================================
        # MI ... ES ...
        # ==========================================

        if (
            texto_limpio.startswith("mi ")
            and " es " in texto_limpio
        ):

            partes = mensaje_limpio.split(
                " es ",
                1
            )


            clave = (
                partes[0][3:]
                .strip()
                .lower()
            )


            valor = (
                partes[1]
                .strip()
            )


            return {
                "clave": clave,
                "valor": valor
            }


        # ==========================================
        # MI ... SON ...
        # ==========================================

        if (
            texto_limpio.startswith("mi ")
            and " son " in texto_limpio
        ):

            partes = mensaje_limpio.split(
                " son ",
                1
            )


            clave = (
                partes[0][3:]
                .strip()
                .lower()
            )


            valor = (
                partes[1]
                .strip()
            )


            return {
                "clave": clave,
                "valor": valor
            }


        # ==========================================
        # ME GUSTA
        # ==========================================

        if texto_limpio.startswith(
            "me gusta "
        ):

            return {
                "clave": "cosas que te gustan",
                "valor": mensaje_limpio[9:].strip()
            }


        # ==========================================
        # ME ENCANTA
        # ==========================================

        if texto_limpio.startswith(
            "me encanta "
        ):

            return {
                "clave": "cosas que te encantan",
                "valor": mensaje_limpio[11:].strip()
            }


        # ==========================================
        # PREFIERO
        # ==========================================

        if texto_limpio.startswith(
            "prefiero "
        ):

            return {
                "clave": "preferencias",
                "valor": mensaje_limpio[9:].strip()
            }


        # ==========================================
        # ODIO
        # ==========================================

        if texto_limpio.startswith(
            "odio "
        ):

            return {
                "clave": "cosas que odias",
                "valor": mensaje_limpio[5:].strip()
            }


        # ==========================================
        # ESTUDIO
        # ==========================================

        if texto_limpio.startswith(
            "estudio "
        ):

            return {
                "clave": "estudios",
                "valor": mensaje_limpio[8:].strip()
            }


        # ==========================================
        # TRABAJO
        # ==========================================

        if texto_limpio.startswith(
            "trabajo en "
        ):

            return {
                "clave": "trabajo",
                "valor": mensaje_limpio[11:].strip()
            }


        # ==========================================
        # VIVO EN
        # ==========================================

        if texto_limpio.startswith(
            "vivo en "
        ):

            return {
                "clave": "lugar donde vives",
                "valor": mensaje_limpio[8:].strip()
            }


        # ==========================================
        # SOY
        # ==========================================

        if texto_limpio.startswith(
            "soy "
        ):

            return {
                "clave": "información personal",
                "valor": mensaje_limpio[4:].strip()
            }


        # ==========================================
        # TENGO
        # ==========================================

        if texto_limpio.startswith(
            "tengo "
        ):

            return {
                "clave": "información personal",
                "valor": mensaje_limpio[6:].strip()
            }


        # ==========================================
        # NO SE PUDO EXTRAER
        # ==========================================

        return None


    # ==========================================
    # EXTRAER CONSULTA EXACTA
    # ==========================================

    def extraer_consulta(
        self,
        mensaje
    ):

        texto = mensaje.lower()


        texto = (
            texto
            .replace("¿", "")
            .replace("?", "")
        )


        if texto.startswith(
            "cual es mi "
        ):

            return texto.replace(
                "cual es mi ",
                ""
            ).strip()


        if texto.startswith(
            "cuál es mi "
        ):

            return texto.replace(
                "cuál es mi ",
                ""
            ).strip()


        return None


    # ==========================================
    # EXTRAER TEMA DE MEMORIA
    # ==========================================

    def extraer_tema_memoria(
        self,
        mensaje
    ):

        texto = (
            mensaje
            .lower()
            .strip()
            .replace("¿", "")
            .replace("?", "")
        )


        frases = [

            "que recuerdas sobre ",
            "qué recuerdas sobre ",

            "que sabes sobre ",
            "qué sabes sobre ",

            "que recuerdas de ",
            "qué recuerdas de ",

            "que sabes de ",
            "qué sabes de ",

            "dime lo que recuerdas sobre ",
            "dime qué recuerdas sobre ",

            "que cosas recuerdas de ",
            "qué cosas recuerdas de "

        ]


        for frase in frases:

            if texto.startswith(frase):

                tema = texto[
                    len(frase):
                ].strip()


                return tema


        return None


    # ==========================================
    # EXTRAER TEMA DE CONVERSACIÓN
    # ==========================================

    def extraer_tema(
        self,
        mensaje
    ):

        texto = (
            mensaje
            .lower()
            .strip()
        )


        frases = [

            "que te dije sobre ",
            "qué te dije sobre ",

            "que hablamos sobre ",
            "qué hablamos sobre ",

            "recuerdas lo de ",
            "recuerdas cuando hablamos de "

        ]


        for frase in frases:

            if texto.startswith(frase):

                return texto[
                    len(frase):
                ].strip()


        return None
