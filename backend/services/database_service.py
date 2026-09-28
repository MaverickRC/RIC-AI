import sqlite3

from backend.config.settings import DATABASE


# ==========================================
# CONEXIÓN CON LA BASE DE DATOS
# ==========================================

conexion = sqlite3.connect(
    DATABASE,
    check_same_thread=False
)

cursor = conexion.cursor()


# ==========================================
# TABLA DE MEMORIA
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS memoria(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    clave TEXT UNIQUE,

    valor TEXT,

    importancia INTEGER DEFAULT 1

)
""")

conexion.commit()


# ==========================================
# MIGRACIÓN DE BASE DE DATOS
# ==========================================

cursor.execute("""
PRAGMA table_info(memoria)
""")

columnas = cursor.fetchall()

nombres_columnas = [
    columna[1]
    for columna in columnas
]

if "importancia" not in nombres_columnas:

    cursor.execute("""
    ALTER TABLE memoria
    ADD COLUMN importancia INTEGER DEFAULT 1
    """)

    conexion.commit()

    print(
        "🔄 Columna 'importancia' agregada a memoria."
    )


# ==========================================
# TABLA DE CONVERSACIONES
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS conversaciones(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    usuario TEXT,

    ric_ai TEXT,

    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

conexion.commit()


# ==========================================
# GUARDAR MEMORIA
# ==========================================

def guardar(
    clave,
    valor,
    importancia=1
):

    cursor.execute(
        """
        INSERT INTO memoria
        (clave, valor, importancia)

        VALUES (?, ?, ?)

        ON CONFLICT(clave)
        DO UPDATE SET
            valor = excluded.valor,
            importancia = excluded.importancia
        """,

        (
            clave,
            valor,
            importancia
        )
    )

    conexion.commit()

    print(
        f"💾 Memoria guardada: "
        f"{clave} = {valor} "
        f"(importancia: {importancia})"
    )


# ==========================================
# OBTENER MEMORIA EXACTA
# ==========================================

def obtener(clave):

    cursor.execute(
        """
        SELECT valor
        FROM memoria
        WHERE LOWER(clave) = LOWER(?)
        """,

        (clave,)
    )

    dato = cursor.fetchone()

    if dato:

        return dato[0]

    return None


# ==========================================
# COMPATIBILIDAD CON MEMORY MANAGER
# ==========================================

def obtener_memoria(clave):

    return obtener(clave)


# ==========================================
# BUSCAR MEMORIAS RELACIONADAS
# ==========================================

def buscar_memorias(texto):

    texto = (
        texto
        .lower()
        .strip()
    )

    print(
        f"🔎 Database buscando: {texto}"
    )


    # ------------------------------------------
    # BÚSQUEDA DIRECTA
    # ------------------------------------------

    cursor.execute(
        """
        SELECT clave, valor, importancia
        FROM memoria

        WHERE LOWER(clave) LIKE ?
           OR LOWER(valor) LIKE ?

        ORDER BY importancia DESC, id DESC
        """,

        (
            f"%{texto}%",
            f"%{texto}%"
        )
    )

    resultados = cursor.fetchall()


    # ------------------------------------------
    # BÚSQUEDA POR PALABRAS
    # ------------------------------------------

    palabras = texto.split()


    for palabra in palabras:

        # Ignorar palabras demasiado pequeñas
        # o palabras que no aportan significado.

        if len(palabra) < 3:

            continue


        cursor.execute(
            """
            SELECT clave, valor, importancia
            FROM memoria

            WHERE LOWER(clave) LIKE ?
               OR LOWER(valor) LIKE ?

            ORDER BY importancia DESC, id DESC
            """,

            (
                f"%{palabra}%",
                f"%{palabra}%"
            )
        )


        nuevos = cursor.fetchall()


        for memoria in nuevos:

            if memoria not in resultados:

                resultados.append(
                    memoria
                )


    # ------------------------------------------
    # ORDENAR RESULTADOS
    # ------------------------------------------

    resultados.sort(
        key=lambda memoria: (
            memoria[2],
            memoria[0]
        ),
        reverse=True
    )


    print(
        f"🔎 Memorias encontradas: "
        f"{len(resultados)}"
    )


    return resultados


# ==========================================
# OBTENER TODAS LAS MEMORIAS
# ==========================================

def obtener_todas_las_memorias():

    cursor.execute(
        """
        SELECT clave, valor, importancia
        FROM memoria

        ORDER BY importancia DESC, id DESC
        """
    )

    return cursor.fetchall()


# ==========================================
# GUARDAR CONVERSACIÓN
# ==========================================

def guardar_conversacion(
    usuario,
    respuesta
):

    cursor.execute(
        """
        INSERT INTO conversaciones
        (usuario, ric_ai)

        VALUES (?, ?)
        """,

        (
            usuario,
            respuesta
        )
    )

    conexion.commit()


# ==========================================
# OBTENER ÚLTIMAS CONVERSACIONES
# ==========================================

def obtener_ultimas_conversaciones(
    limite=10
):

    cursor.execute(
        """
        SELECT usuario, ric_ai, fecha
        FROM conversaciones

        ORDER BY id DESC

        LIMIT ?
        """,

        (limite,)
    )

    return cursor.fetchall()


# ==========================================
# OBTENER ÚLTIMA CONVERSACIÓN
# ==========================================

def obtener_ultima_conversacion():

    cursor.execute(
        """
        SELECT usuario, ric_ai
        FROM conversaciones

        ORDER BY id DESC

        LIMIT 1
        """
    )

    dato = cursor.fetchone()

    if dato:

        return {

            "usuario": dato[0],

            "ric_ai": dato[1]

        }

    return None
