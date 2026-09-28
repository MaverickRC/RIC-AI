from backend.tools.tool_manager import ToolManager


print("==========================================")
print("🌐 PRUEBA DE HERRAMIENTAS DE RIC-AI")
print("==========================================")


tools = ToolManager()


resultado = tools.buscar_internet(
    "¿Qué es inteligencia artificial?"
)


print()
print("==========================================")
print("📡 RESULTADO")
print("==========================================")

print(
    "Éxito:",
    resultado["exito"]
)

print(
    "Mensaje:",
    resultado["resultado"]
)

print(
    "Contenido recibido:",
    len(
        resultado.get(
            "contenido",
            ""
        )
    ),
    "caracteres"
)
