class ConceptManager:

    def __init__(self):

        print(
            "🔗 ConceptManager iniciado"
        )

        # ==========================================
        # MAPA DE CONCEPTOS
        # ==========================================

        self.conceptos = {

            "comida": [
                "comida",
                "comidas",
                "alimentación",
                "alimento",
                "alimentos",
                "comer"
            ],

            "gustos": [
                "gusto",
                "gustos",
                "preferencias",
                "preferencia",
                "cosas que me gustan",
                "lo que me gusta"
            ],

            "color": [
                "color",
                "colores",
                "color favorito"
            ],

            "videojuegos": [
                "videojuego",
                "videojuegos",
                "juego",
                "juegos",
                "gaming"
            ],

            "estudios": [
                "estudio",
                "estudios",
                "universidad",
                "carrera",
                "materia",
                "materias"
            ],

            "trabajo": [
                "trabajo",
                "empleo",
                "ocupación",
                "trabajar"
            ]

        }


    # ==========================================
    # DETECTAR CONCEPTO
    # ==========================================

    def detectar_concepto(
        self,
        texto
    ):

        texto = (
            texto
            .lower()
            .strip()
        )


        # ------------------------------------------
        # BUSCAR COINCIDENCIA
        # ------------------------------------------

        for concepto, palabras in self.conceptos.items():

            for palabra in palabras:

                if palabra in texto:

                    print(
                        f"🔗 Concepto detectado: "
                        f"{concepto}"
                    )

                    return concepto


        # ------------------------------------------
        # SIN CONCEPTO
        # ------------------------------------------

        print(
            "🔗 No se detectó un concepto."
        )

        return None


    # ==========================================
    # OBTENER PALABRAS RELACIONADAS
    # ==========================================

    def obtener_palabras_relacionadas(
        self,
        concepto
    ):

        return self.conceptos.get(
            concepto,
            []
        )


    # ==========================================
    # OBTENER CONCEPTO Y PALABRAS
    # ==========================================

    def analizar(
        self,
        texto
    ):

        concepto = self.detectar_concepto(
            texto
        )


        if not concepto:

            return {
                "concepto": None,
                "palabras": []
            }


        palabras = (
            self.obtener_palabras_relacionadas(
                concepto
            )
        )


        return {
            "concepto": concepto,
            "palabras": palabras
        }
