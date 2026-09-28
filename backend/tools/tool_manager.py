from backend.tools.internet_tool import InternetTool


class ToolManager:

    def __init__(self):

        print("🛠️ ToolManager iniciado")

        # ==========================================
        # HERRAMIENTA DE INTERNET
        # ==========================================

        self.internet = InternetTool()


    # ==========================================
    # BUSCAR EN INTERNET
    # ==========================================

    def buscar_internet(self, consulta):

        print(
            f"🛠️ ToolManager → InternetTool"
        )

        return self.internet.buscar(
            consulta
        )
