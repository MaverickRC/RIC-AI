from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from backend.services.database_service import (
    guardar,
    obtener,
    obtener_todas_las_memorias,
    obtener_ultimas_conversaciones
)

from backend.routes.chat_routes import router as chat_router


# ==========================================
# RIC-AI
# APLICACIÓN PRINCIPAL
# VERSION 0.3
# ==========================================

app = FastAPI(
    title="RIC-AI",
    description="La inteligencia artificial creada por Ricardo",
    version="0.3"
)


# ==========================================
# RUTAS DEL CHAT
# ==========================================

app.include_router(
    chat_router
)


# ==========================================
# ARCHIVOS DEL FRONTEND
# ==========================================

app.mount(
    "/frontend",
    StaticFiles(
        directory="frontend"
    ),
    name="frontend"
)


# ==========================================
# PAGINA PRINCIPAL
# ==========================================

@app.get("/")
def inicio():

    return {
        "mensaje": "Hola! Soy RIC-AI 🤖",
        "estado": "Funcionando correctamente",
        "version": "0.3"
    }


# ==========================================
# INTERFAZ DE RIC-AI
# ==========================================

@app.get("/ric-ai")
def ric_ai():

    return FileResponse(
        "frontend/index.html"
    )


# ==========================================
# GUARDAR DATO
# ==========================================

@app.get("/guardar")
def guardar_dato(
    clave: str,
    valor: str
):

    guardar(
        clave,
        valor
    )

    return {
        "mensaje": "Dato guardado correctamente.",
        "clave": clave,
        "valor": valor
    }


# ==========================================
# LEER DATO
# ==========================================

@app.get("/leer")
def leer_dato(
    clave: str
):

    valor = obtener(
        clave
    )

    return {
        "clave": clave,
        "valor": valor
    }


# ==========================================
# MEMORIA
# ==========================================
# Devuelve todas las memorias guardadas
# para mostrarlas en la interfaz.

@app.get("/memoria")
def obtener_memoria():

    memorias = (
        obtener_todas_las_memorias()
    )

    resultado = []

    for memoria in memorias:

        resultado.append({

            "clave": memoria[0],

            "valor": memoria[1],

            "importancia": memoria[2]

        })

    return {
        "exito": True,
        "memorias": resultado
    }


# ==========================================
# MEMORIA — API
# ==========================================
# Alias para que el frontend pueda utilizar
# una ruta más organizada.

@app.get("/api/memoria")
def obtener_memoria_api():

    memorias = (
        obtener_todas_las_memorias()
    )

    resultado = []

    for memoria in memorias:

        resultado.append({

            "clave": memoria[0],

            "valor": memoria[1],

            "importancia": memoria[2]

        })

    return {
        "exito": True,
        "memorias": resultado
    }


# ==========================================
# HISTORIAL
# ==========================================
# Devuelve las conversaciones almacenadas.

@app.get("/historial")
def obtener_historial(
    limite: int = 50
):

    # Evitamos valores absurdos.

    if limite < 1:

        limite = 1

    if limite > 200:

        limite = 200


    conversaciones = (
        obtener_ultimas_conversaciones(
            limite
        )
    )


    resultado = []


    for conversacion in conversaciones:

        usuario, ric_ai, fecha = (
            conversacion
        )


        resultado.append({

            "usuario": usuario,

            "ric_ai": ric_ai,

            "fecha": fecha

        })


    return {

        "exito": True,

        "historial": resultado

    }


# ==========================================
# HISTORIAL — API
# ==========================================

@app.get("/api/historial")
def obtener_historial_api(
    limite: int = 50
):

    if limite < 1:

        limite = 1

    if limite > 200:

        limite = 200


    conversaciones = (
        obtener_ultimas_conversaciones(
            limite
        )
    )


    resultado = []


    for conversacion in conversaciones:

        usuario, ric_ai, fecha = (
            conversacion
        )


        resultado.append({

            "usuario": usuario,

            "ric_ai": ric_ai,

            "fecha": fecha

        })


    return {

        "exito": True,

        "historial": resultado

    }


# ==========================================
# CONFIGURACION
# ==========================================
# Información básica que puede mostrar
# la página de configuración.
#
# IMPORTANTE:
# Nunca devolvemos la API KEY.

@app.get("/configuracion")
def configuracion():

    return {

        "exito": True,

        "ric_ai": {

            "nombre": "RIC-AI",

            "version": "0.3",

            "estado": "En desarrollo"

        },

        "servicios": {

            "chat": "Activo",

            "memoria": "Activo",

            "historial": "Activo",

            "internet": "Disponible según configuración"

        }

    }


# ==========================================
# CONFIGURACION — API
# ==========================================

@app.get("/api/configuracion")
def configuracion_api():

    return {

        "exito": True,

        "ric_ai": {

            "nombre": "RIC-AI",

            "version": "0.3",

            "estado": "En desarrollo"

        },

        "servicios": {

            "chat": "Activo",

            "memoria": "Activo",

            "historial": "Activo",

            "internet": "Disponible según configuración"

        }

    }


# ==========================================
# ESTADO DEL SISTEMA
# ==========================================
# Endpoint para comprobar rápidamente si
# RIC-AI está funcionando.

@app.get("/api/estado")
def estado():

    return {

        "exito": True,

        "nombre": "RIC-AI",

        "estado": "online",

        "version": "0.3"

    }
