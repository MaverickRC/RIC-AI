from backend.services.database_service import (
    guardar,
    obtener_memoria,
    buscar_memorias,
    obtener_todas_las_memorias
)

from backend.services.concept_manager import ConceptManager


class MemoryManager:

    def __init__(self):

        print(
            "💾 MemoryManager iniciado"
        )

        self.concept_manager = (
            ConceptManager()
        )


    # ==========================================
    # GUARDAR MEMORIA
    # ==========================================

    def guardar_memoria(
        self,
        clave,
        valor,
        importancia=1
    ):

        print(
            f"💾 Guardando memoria: "
            f"{clave} = {valor} "
            f"(importancia: {importancia})"
        )


        guardar(
            clave,
            valor,
            importancia
        )


    # ==========================================
    # RECORDAR MEMORIA EXACTA
    # ==========================================

    def recordar(
        self,
        clave
    ):

        print(
            f"🔎 Buscando memoria exacta: "
            f"{clave}"
        )


        return obtener_memoria(
            clave
        )


    # ==========================================
    # BUSCAR MEMORIAS RELACIONADAS
    # ==========================================

    def buscar(
        self,
        texto
    ):

        print(
            f"🔎 MemoryManager buscando: "
            f"{texto}"
        )


        analisis = (
            self.concept_manager.analizar(
                texto
            )
        )


        concepto = (
            analisis["concepto"]
        )

        palabras = (
            analisis["palabras"]
        )


        print(
            f"🔗 Concepto: {concepto}"
        )


        resultados = buscar_memorias(
            texto
        )


        if concepto:

            for palabra in palabras:

                nuevos_resultados = (
                    buscar_memorias(
                        palabra
                    )
                )


                for memoria in nuevos_resultados:

                    if memoria not in resultados:

                        resultados.append(
                            memoria
                        )


        resultados_unicos = []


        for memoria in resultados:

            if memoria not in resultados_unicos:

                resultados_unicos.append(
                    memoria
                )


        resultados_unicos.sort(
            key=lambda memoria: (
                memoria[2],
                memoria[0]
            ),
            reverse=True
        )


        print(
            f"🔎 Resultado final: "
            f"{len(resultados_unicos)} memorias."
        )


        return resultados_unicos


    # ==========================================
    # OBTENER TODAS LAS MEMORIAS
    # ==========================================

    def obtener_todas(self):

        print(
            "📚 Obteniendo todas las memorias..."
        )


        return (
            obtener_todas_las_memorias()
        )


    # ==========================================
    # OBTENER CONTEXTO DE MEMORIA
    # ==========================================

    def obtener_contexto(
        self,
        texto,
        limite=8
    ):

        print(
            f"🧠 Construyendo contexto de memoria "
            f"para: {texto}"
        )


        resultados = self.buscar(
            texto
        )


        if not resultados:

            print(
                "🧠 No se encontraron memorias "
                "relevantes."
            )

            return ""


        resultados = (
            resultados[:limite]
        )


        contexto = (
            "MEMORIAS RELEVANTES DEL USUARIO:\n"
        )


        for memoria in resultados:

            clave = memoria[0]

            valor = memoria[1]

            importancia = memoria[2]


            contexto += (
                f"- {clave}: {valor} "
                f"(importancia {importancia})\n"
            )


        print(
            "🧠 Contexto de memoria generado:"
        )


        print(
            contexto
        )


        return contexto
