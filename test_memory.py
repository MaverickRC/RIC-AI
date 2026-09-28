from backend.services.memory_evaluator import MemoryEvaluator


# ==========================================
# INICIAR EVALUADOR
# ==========================================

evaluator = MemoryEvaluator()


# ==========================================
# MENSAJES DE PRUEBA
# ==========================================

mensajes = [

    "Recuerda que mi comida favorita es la chuleta",

    "Me gusta jugar videojuegos",

    "Hoy fui al trabajo",

    "¿Qué hora es?"

]


# ==========================================
# ANALIZAR MENSAJES
# ==========================================

for mensaje in mensajes:

    print("\n==========================================")

    print(
        f"📝 Mensaje: {mensaje}"
    )

    resultado = evaluator.evaluar(
        mensaje
    )

    print(
        f"📊 Resultado: {resultado}"
    )
