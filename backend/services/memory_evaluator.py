class MemoryEvaluator:

    def __init__(self):

        print("⭐ MemoryEvaluator iniciado")


    # ==========================================
    # EVALUAR MENSAJE
    # ==========================================

    def evaluar(self, mensaje):

        texto = mensaje.lower().strip()


        # ==========================================
        # RESULTADO POR DEFECTO
        # ==========================================

        resultado = {
            "debe_guardar": False,
            "importancia": 1
        }


        # ==========================================
        # MEMORIA EXPLÍCITA
        # ==========================================

        frases_importantes = [

            "recuerda que ",
            "recuerda ",
            "no olvides que ",
            "no olvides ",
            "es importante que ",
            "es importante "

        ]


        for frase in frases_importantes:

            if texto.startswith(frase):

                resultado = {
                    "debe_guardar": True,
                    "importancia": 3
                }

                print(
                    "⭐ Memoria explícita detectada."
                )

                return resultado


        # ==========================================
        # INFORMACIÓN PERSONAL
        # ==========================================

        patrones_personales = [

            "mi ",
            "me gusta ",
            "me encanta ",
            "odio ",
            "prefiero ",
            "estudio ",
            "trabajo en ",
            "vivo en ",
            "soy ",
            "tengo "

        ]


        for patron in patrones_personales:

            if texto.startswith(patron):

                resultado = {
                    "debe_guardar": True,
                    "importancia": 2
                }

                print(
                    "🧠 Posible memoria personal detectada."
                )

                return resultado


        # ==========================================
        # INFORMACIÓN TEMPORAL
        # ==========================================

        frases_temporales = [

            "hoy ",
            "ahora ",
            "esta mañana ",
            "esta tarde ",
            "esta noche ",
            "ayer ",
            "mañana "

        ]


        for frase in frases_temporales:

            if texto.startswith(frase):

                resultado = {
                    "debe_guardar": False,
                    "importancia": 1
                }

                print(
                    "⏳ Información temporal detectada."
                )

                return resultado


        # ==========================================
        # CONVERSACIÓN NORMAL
        # ==========================================

        print(
            "💬 No se detectó una memoria."
        )


        return resultado
