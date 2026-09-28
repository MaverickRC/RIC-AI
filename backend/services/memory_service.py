from backend.services.database_service import guardar, obtener
def aprender(mensaje):

    texto = mensaje.lower()
    if texto.startswith("me llamo "):

        nombre = mensaje[9:].strip()

        guardar("nombre", nombre)

        return True
    if texto.startswith("mi color favorito es "):

        color = mensaje[21:].strip()

        guardar("color_favorito", color)

        return True
    return False
def recordar(clave):

    return obtener(clave)
