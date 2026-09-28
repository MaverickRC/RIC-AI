console.log("🤖 RIC-AI v0.4 iniciado");


// ==========================================
// ELEMENTOS PRINCIPALES
// ==========================================

const boton =
    document.getElementById("enviar");

const caja =
    document.getElementById("mensaje");

const chat =
    document.getElementById("chat");

const bienvenida =
    document.getElementById("bienvenida");

const sidebar =
    document.getElementById("sidebar");

const menuMovil =
    document.getElementById("menuMovil");

const nuevoChat =
    document.getElementById("nuevoChat");

const cambiarTema =
    document.getElementById("cambiarTema");

const menuItems =
    document.querySelectorAll(".menu-item");

const sugerencias =
    document.querySelectorAll(".sugerencia");


// ==========================================
// SECCIONES
// ==========================================

const secciones = {

    chat:
        document.getElementById(
            "seccion-chat"
        ),

    memoria:
        document.getElementById(
            "seccion-memoria"
        ),

    historial:
        document.getElementById(
            "seccion-historial"
        ),

    configuracion:
        document.getElementById(
            "seccion-configuracion"
        )

};


// ==========================================
// TEMA
// ==========================================

function aplicarTema(tema) {

    if (tema === "claro") {

        document.body.classList.add(
            "modo-claro"
        );

        cambiarTema.innerHTML =
            "☀️ Modo blanco";

    } else {

        document.body.classList.remove(
            "modo-claro"
        );

        cambiarTema.innerHTML =
            "🌑 Modo oscuro";

    }

    localStorage.setItem(
        "ric-ai-tema",
        tema
    );

}


// ==========================================
// CARGAR TEMA GUARDADO
// ==========================================

function cargarTema() {

    const temaGuardado =
        localStorage.getItem(
            "ric-ai-tema"
        );

    if (temaGuardado) {

        aplicarTema(
            temaGuardado
        );

        return;

    }

    aplicarTema(
        "oscuro"
    );

}


// ==========================================
// CAMBIAR TEMA
// ==========================================

cambiarTema.addEventListener(
    "click",
    function () {

        const estaClaro =
            document.body.classList.contains(
                "modo-claro"
            );

        if (estaClaro) {

            aplicarTema(
                "oscuro"
            );

        } else {

            aplicarTema(
                "claro"
            );

        }

    }
);


// Cargar inmediatamente

cargarTema();


// ==========================================
// CAMBIAR SECCIÓN
// ==========================================

function cambiarSeccion(nombre) {

    console.log(
        "📂 Cambiando sección:",
        nombre
    );


    Object.keys(secciones).forEach(
        function (seccion) {

            secciones[seccion].style.display =
                "none";

        }
    );


    if (secciones[nombre]) {

        secciones[nombre].style.display =
            "block";

    }


    menuItems.forEach(
        function (item) {

            item.classList.remove(
                "activo"
            );


            if (
                item.dataset.seccion
                === nombre
            ) {

                item.classList.add(
                    "activo"
                );

            }

        }
    );


    if (
        window.innerWidth <= 850
    ) {

        sidebar.classList.remove(
            "abierto"
        );

    }


    if (
        nombre === "memoria"
    ) {

        cargarMemoria();

    }


    if (
        nombre === "historial"
    ) {

        cargarHistorial();

    }

}


// ==========================================
// EVENTOS DEL MENÚ
// ==========================================

menuItems.forEach(
    function (item) {

        item.addEventListener(
            "click",
            function () {

                cambiarSeccion(
                    item.dataset.seccion
                );

            }
        );

    }
);


// ==========================================
// MENÚ MÓVIL
// ==========================================

menuMovil.addEventListener(
    "click",
    function () {

        sidebar.classList.toggle(
            "abierto"
        );

    }
);


// ==========================================
// NUEVO CHAT
// ==========================================

nuevoChat.addEventListener(
    "click",
    function () {

        console.log(
            "➕ Nuevo chat"
        );


        chat.innerHTML =
            "";


        bienvenida.style.display =
            "flex";


        caja.value =
            "";


        caja.style.height =
            "auto";


        caja.focus();


        cambiarSeccion(
            "chat"
        );

    }
);


// ==========================================
// SUGERENCIAS
// ==========================================

sugerencias.forEach(
    function (botonSugerencia) {

        botonSugerencia.addEventListener(
            "click",
            function () {

                const texto =
                    botonSugerencia.dataset.mensaje;


                caja.value =
                    texto;


                caja.focus();

            }
        );

    }
);


// ==========================================
// ESCAPAR HTML
// ==========================================

function escaparHTML(texto) {

    const div =
        document.createElement(
            "div"
        );


    div.textContent =
        texto;


    return div.innerHTML;

}


// ==========================================
// INDICADOR DE ESCRITURA
// ==========================================

function mostrarIndicadorEscritura() {

    ocultarIndicadorEscritura();


    const indicador =
        document.createElement(
            "div"
        );


    indicador.id =
        "indicadorEscritura";


    indicador.className =
        "mensaje indicador-escritura";


    indicador.innerHTML = `

        <div class="mensaje-nombre">

            RIC-AI

        </div>


        <div class="indicador-contenido">

            <span class="indicador-texto">

                Escribiendo

            </span>


            <span class="puntos-escritura">

                <span></span>

                <span></span>

                <span></span>

            </span>

        </div>

    `;


    chat.appendChild(
        indicador
    );


    chat.scrollTop =
        chat.scrollHeight;

}


function ocultarIndicadorEscritura() {

    const indicador =
        document.getElementById(
            "indicadorEscritura"
        );


    if (indicador) {

        indicador.remove();

    }

}


// ==========================================
// MARKDOWN + TARJETAS COMPARATIVAS
// ==========================================

function convertirMarkdown(texto) {

    // ======================================
    // EXTRAER TABLAS COMPARATIVAS
    // ======================================

    const tablas = [];

    const marcadorBase = "___RIC_AI_TABLA_";

    const textoConMarcadores = texto.replace(
        /(^|\n)(\|.+\|)\n(\|[\s:|-]+\|)\n((?:\|.+\|\n?)+)/g,
        function (coincidencia, inicio, encabezado, separador, filas) {

            const convertirFila = function (fila) {

                return fila
                    .trim()
                    .replace(/^\|/, "")
                    .replace(/\|$/, "")
                    .split("|")
                    .map(function (celda) {
                        return celda.trim();
                    });

            };


            const columnas = convertirFila(
                encabezado
            );


            const filasDatos = filas
                .trim()
                .split("\n")
                .map(function (fila) {
                    return convertirFila(fila);
                })
                .filter(function (fila) {
                    return fila.length >= 3;
                });


            // ==================================
            // COMPROBAR SI ES COMPARACIÓN
            // ==================================

            if (
                columnas.length < 3
                ||
                filasDatos.length === 0
            ) {

                return coincidencia;

            }


            const indice =
                tablas.length;


            tablas.push({

                encabezado: columnas,

                filas: filasDatos

            });


            return "\n" +
                marcadorBase +
                indice +
                "\n";

        }
    );


    // ======================================
    // ESCAPAR HTML
    // ======================================

    let html =
        escaparHTML(
            textoConMarcadores
        );


    // ======================================
    // CÓDIGO EN BLOQUE
    // ======================================

    html =
        html.replace(
            /```([\s\S]*?)```/g,
            "<pre><code>$1</code></pre>"
        );


    // ======================================
    // TÍTULOS
    // ======================================

    html =
        html.replace(
            /^#### (.*)$/gm,
            "<h4>$1</h4>"
        );


    html =
        html.replace(
            /^### (.*)$/gm,
            "<h3>$1</h3>"
        );


    html =
        html.replace(
            /^## (.*)$/gm,
            "<h2>$1</h2>"
        );


    html =
        html.replace(
            /^# (.*)$/gm,
            "<h1>$1</h1>"
        );


    // ======================================
    // NEGRITA
    // ======================================

    html =
        html.replace(
            /\*\*(.*?)\*\*/g,
            "<strong>$1</strong>"
        );


    // ======================================
    // CURSIVA
    // ======================================

    html =
        html.replace(
            /(?<!\*)\*([^*\n]+)\*(?!\*)/g,
            "<em>$1</em>"
        );


    // ======================================
    // CÓDIGO INLINE
    // ======================================

    html =
        html.replace(
            /`([^`\n]+)`/g,
            "<code>$1</code>"
        );


    // ======================================
    // LISTAS SIMPLES
    // ======================================

    html =
        html.replace(
            /^\s*[-•] (.*)$/gm,
            "<li>$1</li>"
        );


    html =
        html.replace(
            /(<li>.*<\/li>)/gs,
            "<ul>$1</ul>"
        );


    // ======================================
    // SALTOS DE LÍNEA
    // ======================================

    html =
        html.replace(
            /\n/g,
            "<br>"
        );


    // ======================================
    // EVITAR BR DESPUÉS DE ELEMENTOS
    // ======================================

    html =
        html.replace(
            /<\/h1><br>/g,
            "</h1>"
        );


    html =
        html.replace(
            /<\/h2><br>/g,
            "</h2>"
        );


    html =
        html.replace(
            /<\/h3><br>/g,
            "</h3>"
        );


    html =
        html.replace(
            /<\/h4><br>/g,
            "</h4>"
        );


    html =
        html.replace(
            /<\/pre><br>/g,
            "</pre>"
        );


    // ======================================
    // INSERTAR TARJETAS COMPARATIVAS
    // ======================================

    tablas.forEach(
        function (tabla, indice) {

            const marcador =
                marcadorBase +
                indice;


            const encabezado =
                tabla.encabezado;


            const filas =
                tabla.filas;


            const titulo =
                encabezado[0];


            let tarjetas = "";


            // ==================================
            // CREAR UNA TARJETA POR ELEMENTO
            // ==================================

            for (
                let columna = 1;
                columna < encabezado.length;
                columna++
            ) {

                const nombreElemento =
                    encabezado[columna];


                let contenidoTarjeta = "";


                filas.forEach(
                    function (fila) {

                        const aspecto =
                            fila[0];


                        const valor =
                            fila[columna]
                            || "";


                        contenidoTarjeta += `

                            <div class="comparacion-item">

                                <div class="comparacion-aspecto">

                                    ${aspecto}

                                </div>


                                <div class="comparacion-valor">

                                    ${valor}

                                </div>

                            </div>

                        `;

                    }
                );


                tarjetas += `

                    <div class="comparacion-card">

                        <div class="comparacion-card-header">

                            ${nombreElemento}

                        </div>


                        <div class="comparacion-card-body">

                            ${contenidoTarjeta}

                        </div>

                    </div>

                `;

            }


            const comparacionHTML = `

                <div class="comparacion">

                    <div class="comparacion-titulo">

                        ${titulo}

                    </div>


                    <div class="comparacion-columnas">

                        ${tarjetas}

                    </div>

                </div>

            `;


            html =
                html.replace(
                    marcador,
                    comparacionHTML
                );

        }
    );


    return html;

}


// ==========================================
// MOSTRAR MENSAJE
// ==========================================

function mostrarMensaje(
    tipo,
    contenido,
    preguntaOriginal = null
) {

    const mensaje =
        document.createElement(
            "div"
        );


    mensaje.className =
        `mensaje ${tipo}`;


    const nombre =
        tipo === "usuario"
            ? "Tú"
            : "RIC-AI";


    mensaje.innerHTML = `

        <div class="mensaje-nombre">

            ${nombre}

        </div>


        <div class="mensaje-contenido markdown">

            ${
                tipo === "ric-ai"
                    ? convertirMarkdown(
                        contenido
                    )
                    : contenido
            }

        </div>

    `;


    // ======================================
    // ACCIONES DE RIC-AI
    // ======================================

    if (
        tipo === "ric-ai"
        &&
        preguntaOriginal
    ) {

        const acciones =
            document.createElement(
                "div"
            );


        acciones.className =
            "mensaje-acciones";


        // ==================================
        // COPIAR
        // ==================================

        const botonCopiar =
            document.createElement(
                "button"
            );


        botonCopiar.className =
            "accion-mensaje";


        botonCopiar.type =
            "button";


        botonCopiar.innerHTML =
            "📋 Copiar";


        botonCopiar.title =
            "Copiar respuesta";


        botonCopiar.addEventListener(
            "click",
            async function () {

                const texto =
                    mensaje.querySelector(
                        ".mensaje-contenido"
                    ).innerText;


                try {

                    await navigator.clipboard.writeText(
                        texto
                    );


                    botonCopiar.innerHTML =
                        "✓ Copiado";


                    setTimeout(
                        function () {

                            botonCopiar.innerHTML =
                                "📋 Copiar";

                        },
                        1500
                    );


                } catch (error) {

                    console.error(
                        "❌ Error copiando:",
                        error
                    );


                }

            }
        );


        // ==================================
        // REGENERAR
        // ==================================

        const botonRegenerar =
            document.createElement(
                "button"
            );


        botonRegenerar.className =
            "accion-mensaje";


        botonRegenerar.type =
            "button";


        botonRegenerar.innerHTML =
            "🔄 Regenerar";


        botonRegenerar.title =
            "Regenerar respuesta";


        botonRegenerar.addEventListener(
            "click",
            function () {

                regenerarRespuesta(
                    mensaje,
                    preguntaOriginal
                );

            }
        );


        acciones.appendChild(
            botonCopiar
        );


        acciones.appendChild(
            botonRegenerar
        );


        mensaje.appendChild(
            acciones
        );

    }


    chat.appendChild(
        mensaje
    );


    chat.scrollTop =
        chat.scrollHeight;

}


// ==========================================
// ENVIAR MENSAJE
// ==========================================

async function enviarMensaje() {

    const mensaje =
        caja.value.trim();


    if (
        mensaje === ""
    ) {

        return;

    }


    console.log(
        "📤 Mensaje:",
        mensaje
    );


    cambiarSeccion(
        "chat"
    );


    bienvenida.style.display =
        "none";


    // Mostrar usuario

    mostrarMensaje(
        "usuario",
        escaparHTML(
            mensaje
        )
    );


    caja.value =
        "";


    caja.style.height =
        "auto";


    boton.disabled =
        true;


    caja.disabled =
        true;


    mostrarIndicadorEscritura();


    try {

        const respuesta =
            await fetch(
                `/chat?mensaje=${encodeURIComponent(
                    mensaje
                )}`
            );


        console.log(
            "📥 HTTP:",
            respuesta.status
        );


        if (
            !respuesta.ok
        ) {

            throw new Error(
                `HTTP ${respuesta.status}`
            );

        }


        const datos =
            await respuesta.json();


        console.log(
            "🤖 Respuesta:",
            datos
        );


        const respuestaIA =
            datos.ric_ai
            ||
            "No recibí una respuesta.";


        mostrarMensaje(
            "ric-ai",
            respuestaIA,
            mensaje
        );


    } catch (error) {

        console.error(
            "❌ Error:",
            error
        );


        mostrarMensaje(
            "ric-ai",
            "Ocurrió un error al conectar con RIC-AI."
        );


    } finally {

        ocultarIndicadorEscritura();


        boton.disabled =
            false;


        caja.disabled =
            false;


        caja.focus();

    }

}


// ==========================================
// REGENERAR RESPUESTA
// ==========================================

async function regenerarRespuesta(
    mensajeAnterior,
    pregunta
) {

    console.log(
        "🔄 Regenerando:",
        pregunta
    );


    const contenido =
        mensajeAnterior.querySelector(
            ".mensaje-contenido"
        );


    const acciones =
        mensajeAnterior.querySelector(
            ".mensaje-acciones"
        );


    contenido.innerHTML = `

        <span class="regenerando">

            <span class="puntos-regenerando">

                <span></span>

                <span></span>

                <span></span>

            </span>

            RIC-AI está escribiendo...

        </span>

    `;


    if (acciones) {

        acciones.style.pointerEvents =
            "none";


        acciones.style.opacity =
            "0.5";

    }


    try {

        const respuesta =
            await fetch(
                `/chat?mensaje=${encodeURIComponent(
                    pregunta
                )}`
            );


        if (
            !respuesta.ok
        ) {

            throw new Error(
                `HTTP ${respuesta.status}`
            );

        }


        const datos =
            await respuesta.json();


        const nuevaRespuesta =
            datos.ric_ai
            ||
            "No recibí una respuesta.";


        contenido.innerHTML =
            convertirMarkdown(
                nuevaRespuesta
            );


        console.log(
            "✅ Respuesta regenerada."
        );


    } catch (error) {

        console.error(
            "❌ Error regenerando:",
            error
        );


        contenido.innerHTML =
            "No se pudo regenerar la respuesta.";


    } finally {

        if (acciones) {

            acciones.style.pointerEvents =
                "auto";


            acciones.style.opacity =
                "1";

        }

    }

}


// ==========================================
// EVENTOS DE CHAT
// ==========================================

boton.addEventListener(
    "click",
    enviarMensaje
);


caja.addEventListener(
    "keydown",
    function (event) {

        if (
            event.key === "Enter"
            &&
            !event.shiftKey
        ) {

            event.preventDefault();

            enviarMensaje();

        }

    }
);


// ==========================================
// ALTURA DEL TEXTAREA
// ==========================================

caja.addEventListener(
    "input",
    function () {

        caja.style.height =
            "auto";


        caja.style.height =
            Math.min(
                caja.scrollHeight,
                150
            )
            + "px";

    }
);


// ==========================================
// CARGAR MEMORIA
// ==========================================

async function cargarMemoria() {

    const contenedor =
        document.getElementById(
            "listaMemoria"
        );


    contenedor.innerHTML = `
        <div class="cargando-pagina">
            Cargando memoria...
        </div>
    `;


    try {

        const respuesta =
            await fetch(
                "/memoria"
            );


        if (
            !respuesta.ok
        ) {

            throw new Error(
                "No se pudo obtener la memoria"
            );

        }


        const datos =
            await respuesta.json();


        contenedor.innerHTML =
            "";


        if (
            !datos.memorias
            ||
            datos.memorias.length === 0
        ) {

            contenedor.innerHTML = `
                <div class="cargando-pagina">
                    RIC-AI todavía no tiene
                    memorias guardadas.
                </div>
            `;

            return;

        }


        datos.memorias.forEach(
            function (memoria) {

                const item =
                    document.createElement(
                        "div"
                    );


                item.className =
                    "memoria-item";


                item.innerHTML = `

                    <div class="memoria-clave">

                        ${escaparHTML(
                            String(
                                memoria.clave
                            )
                        )}

                    </div>


                    <div class="memoria-valor">

                        ${escaparHTML(
                            String(
                                memoria.valor
                            )
                        )}

                    </div>


                    <div class="memoria-importancia">

                        Importancia:
                        ${memoria.importancia}

                    </div>

                `;


                contenedor.appendChild(
                    item
                );

            }
        );


    } catch (error) {

        console.error(
            "❌ Error cargando memoria:",
            error
        );


        contenedor.innerHTML = `
            <div class="cargando-pagina">
                No se pudo cargar la memoria.
            </div>
        `;

    }

}


// ==========================================
// CARGAR HISTORIAL
// ==========================================

async function cargarHistorial() {

    const contenedor =
        document.getElementById(
            "listaHistorial"
        );


    contenedor.innerHTML = `
        <div class="cargando-pagina">
            Cargando historial...
        </div>
    `;


    try {

        const respuesta =
            await fetch(
                "/historial"
            );


        if (
            !respuesta.ok
        ) {

            throw new Error(
                "No se pudo obtener el historial"
            );

        }


        const datos =
            await respuesta.json();


        contenedor.innerHTML =
            "";


        if (
            !datos.historial
            ||
            datos.historial.length === 0
        ) {

            contenedor.innerHTML = `
                <div class="cargando-pagina">
                    Todavía no existen conversaciones.
                </div>
            `;

            return;

        }


        datos.historial.forEach(
            function (conversacion) {

                const item =
                    document.createElement(
                        "div"
                    );


                item.className =
                    "historial-item";


                item.innerHTML = `

                    <div class="historial-fecha">

                        ${escaparHTML(
                            String(
                                conversacion.fecha
                            )
                        )}

                    </div>


                    <div class="historial-usuario">

                        <strong>
                            Tú:
                        </strong>

                        ${escaparHTML(
                            String(
                                conversacion.usuario
                            )
                        )}

                    </div>


                    <div class="historial-ric">

                        <strong>
                            RIC-AI:
                        </strong>

                        ${escaparHTML(
                            String(
                                conversacion.ric_ai
                            )
                        )}

                    </div>

                `;


                contenedor.appendChild(
                    item
                );

            }
        );


    } catch (error) {

        console.error(
            "❌ Error cargando historial:",
            error
        );


        contenedor.innerHTML = `
            <div class="cargando-pagina">
                No se pudo cargar el historial.
            </div>
        `;

    }

}


// ==========================================
// BOTONES DE ACTUALIZACIÓN
// ==========================================

document
    .getElementById(
        "actualizarMemoria"
    )
    .addEventListener(
        "click",
        cargarMemoria
    );


document
    .getElementById(
        "actualizarHistorial"
    )
    .addEventListener(
        "click",
        cargarHistorial
    );


console.log(
    "✅ RIC-AI v0.4 listo"
);
