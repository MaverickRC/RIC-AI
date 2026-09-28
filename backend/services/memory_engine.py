class MemoryEngine:

    def __init__(self):

        self.patrones = [
            "me llamo",
            "mi",
            "soy"
        ]

    def analizar(self, mensaje):

        return mensaje.lower()
