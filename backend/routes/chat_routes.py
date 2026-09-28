from fastapi import APIRouter

from backend.services.chat_service import responder

router = APIRouter()

@router.get("/chat")
def chat(mensaje: str):

    respuesta = responder(mensaje)

    return {
        "usuario": mensaje,
        "ric_ai": respuesta
    }
