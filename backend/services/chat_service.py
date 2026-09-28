from backend.services.database_service import (
    guardar_conversacion,
    obtener_ultimas_conversaciones
)

from backend.services.brain import Brain
from backend.services.language_engine import LanguageEngine
from backend.services.memory_manager import MemoryManager
from backend.services.memory_evaluator import MemoryEvaluator
from backend.tools.tool_manager import ToolManager
from backend.services.response_interpreter import ResponseInterpreter


# ==========================================
# COMPONENTES DE RIC-AI
# ==========================================

brain = Brain()
language = LanguageEngine()
memory = MemoryManager()
evaluator = MemoryEvaluator()
tools = ToolManager()
interpreter = ResponseInterpreter()


# ==========================================
# CONSTRUIR CONTEXTO DEL HISTORIAL
# ==========================================

def construir_contexto(historial):

    if not historial:

        return (
            "No existen conversaciones "
            "anteriores."
        )


    contexto = ""


    for conversacion in reversed(
        historial
    ):

        usuario, ric_ai, fecha = (
            conversacion
        )


        contexto += (
            f"[{fecha}]\n"
            f"Tú: {usuario}\n"
            f"RIC-AI: {ric_ai}\n\n"
        )


    return contexto


# ==========================================
# CONSTRUIR CONTEXTO COMPLETO
# ==========================================

def construir_contexto_completo(
    historial,
    contexto_memoria
):

    contexto = ""


    # ======================================
    # HISTORIAL
    # ======================================

    if historial:

        contexto += (
            "HISTORIAL RECIENTE:\n"
        )

        contexto += (
            construir_contexto(
                historial
            )
        )


    # ======================================
    # MEMORIA
    # ======================================

    if contexto_memoria:

        contexto += (
            "\n"
            "MEMORIA RELEVANTE DEL USUARIO:\n"
        )

        contexto += (
            contexto_memoria
        )


    # ======================================
    # SIN CONTEXTO
    # ======================================

    if not contexto:

        contexto = (
            "No existe contexto previo "
            "relevante."
        )


    return contexto


# ==========================================
# RESPONDER
# ==========================================

def responder(mensaje):

    # ==========================================
    # 1. OBTENER HISTORIAL
    # ==========================================

    historial = (
        obtener_ultimas_conversaciones(5)
    )


    print(
        "📚 Contexto reciente:"
    )


    if historial:

        for conversacion in reversed(
            historial
        ):

            usuario, ric_ai, fecha = (
                conversacion
            )


            print(
                f"   [{fecha}] "
                f"Tú: {usuario} | "
                f"RIC-AI: {ric_ai}"
            )


    else:

        print(
            "   No hay conversaciones "
            "anteriores."
        )


    # ==========================================
    # 2. OBTENER MEMORIA RELEVANTE
    # ==========================================

    contexto_memoria = (
        memory.obtener_contexto(
            mensaje
        )
    )


    # ==========================================
    # 3. CONSTRUIR CONTEXTO COMPLETO
    # ==========================================

    contexto = (
        construir_contexto_completo(
            historial,
            contexto_memoria
        )
    )


    print(
        "🧠 Contexto completo preparado "
        "para RIC-AI."
    )


    print(
        contexto
    )


    # ==========================================
    # 4. ANALIZAR MENSAJE CON BRAIN
    # ==========================================

    decision = brain.pensar(
        mensaje,
        historial
    )


    print(
        f"🧠 Decisión: {decision}"
    )


    # ==========================================
    # 5. RESPUESTA POR DEFECTO
    # ==========================================

    respuesta = (
        "Todavía estoy aprendiendo."
    )


    # ==========================================
    # 6. APRENDER
    # ==========================================

    if decision["accion"] == "aprender":

        dato = (
            language.extraer_memoria(
                mensaje
            )
        )


        if dato:

            importancia = (
                decision.get(
                    "importancia",
                    1
                )
            )


            memory.guardar_memoria(
                dato["clave"],
                dato["valor"],
                importancia
            )


            respuesta = (
                f"He aprendido que tu "
                f"{dato['clave']} es "
                f"{dato['valor']}."
            )


        else:

            respuesta = (
                "Entiendo que quieres "
                "que recuerde eso, pero "
                "todavía no sé extraer "
                "esa información."
            )


    # ==========================================
    # 7. RECORDAR
    # ==========================================

    elif decision["accion"] == "recordar":

        consulta = (
            language.extraer_consulta(
                mensaje
            )
        )


        if consulta:

            dato = memory.recordar(
                consulta
            )


            if dato:

                respuesta = (
                    f"Tu {consulta} "
                    f"es {dato}."
                )


            else:

                respuesta = (
                    f"No recuerdo cuál "
                    f"es tu {consulta}."
                )


        else:

            nombre = memory.recordar(
                "nombre"
            )


            if nombre:

                respuesta = (
                    f"Te llamas "
                    f"{nombre}."
                )


            else:

                respuesta = (
                    "Todavía no me has "
                    "dicho tu nombre."
                )


    # ==========================================
    # 8. BUSCAR CONTEXTO / MEMORIA
    # ==========================================

    elif (
        decision["accion"]
        == "buscar_contexto"
    ):

        resultados = memory.buscar(
            mensaje
        )


        if resultados:

            respuesta = (
                "Esto es lo que recuerdo "
                "relacionado con ese tema:\n"
            )


            for memoria_guardada in (
                resultados
            ):

                clave = (
                    memoria_guardada[0]
                )

                valor = (
                    memoria_guardada[1]
                )


                respuesta += (
                    f"• {clave}: "
                    f"{valor}\n"
                )


        else:

            respuesta = (
                "No tengo memorias "
                "relacionadas con ese tema."
            )


    # ==========================================
    # 9. CONTEXTO GENERAL
    # ==========================================

    elif (
        decision["accion"]
        == "contexto"
    ):

        if historial:

            respuesta = (
                "Esto es parte de lo que "
                "recuerdo de nuestras "
                "conversaciones:\n"
            )


            for conversacion in reversed(
                historial
            ):

                usuario = (
                    conversacion[0]
                )


                respuesta += (
                    f"• Tú dijiste: "
                    f"{usuario}\n"
                )


        else:

            respuesta = (
                "Todavía no tengo "
                "conversaciones anteriores."
            )


    # ==========================================
    # 10. BUSCAR EN INTERNET
    # ==========================================

    elif (
        decision["accion"]
        == "buscar_internet"
    ):

        consulta = decision.get(
            "consulta",
            mensaje
        )


        print(
            "🌐 RIC-AI utilizará Internet."
        )


        resultado = (
            tools.buscar_internet(
                consulta
            )
        )


        if resultado["exito"]:

            contenido = (
                resultado.get(
                    "contenido",
                    ""
                )
            )


            if contenido:

                print(
                    "🧠 Enviando información "
                    "al ResponseInterpreter..."
                )


                respuesta = (
                    interpreter.interpretar_internet(
                        consulta,
                        contenido
                    )
                )


            else:

                respuesta = (
                    "Pude conectarme a Internet, "
                    "pero no encontré información "
                    "útil."
                )


        else:

            respuesta = (
                "No pude obtener información "
                "de Internet en este momento."
            )


    # ==========================================
    # 11. CONVERSACIÓN NORMAL CON LLM
    # ==========================================

    elif (
        decision["accion"]
        == "conversar"
    ):

        print(
            "🤖 Enviando conversación "
            "al LLMEngine..."
        )


        respuesta = (
            interpreter.interpretar_conversacion(
                mensaje,
                contexto
            )
        )


    # ==========================================
    # 12. GUARDAR CONVERSACIÓN
    # ==========================================

    guardar_conversacion(
        mensaje,
        respuesta
    )


    # ==========================================
    # 13. MOSTRAR HISTORIAL ACTUALIZADO
    # ==========================================

    historial_actualizado = (
        obtener_ultimas_conversaciones(5)
    )


    print(
        "📚 Historial actualizado:"
    )


    for conversacion in reversed(
        historial_actualizado
    ):

        usuario, ric_ai, fecha = (
            conversacion
        )


        print(
            f"   [{fecha}] "
            f"Tú: {usuario} | "
            f"RIC-AI: {ric_ai}"
        )


    # ==========================================
    # 14. DEVOLVER RESPUESTA
    # ==========================================

    return respuesta
