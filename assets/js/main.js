/**
 * SIAAE-ML | Lógica Interactiva de la Landing Page (Arquitectura en Capas - Bloque C)
 * Universidad Federico Henríquez y Carvajal (UFHEC)
 * Autor: Ing. Adonamil Cruz Evangelista
 *
 * Contiene exactamente los 33 registros sección-año y los 24 abandonos institucionales
 * verificados del Politécnico José Antonio Castillo Ferreiras (2024-2025 y 2025-2026).
 */

const REGISTROS_VERIFICADOS_SIAAE = [
  // Período 2024-2025 (17 secciones reportadas, 9 abandonos)
  { id: 1, anio: "2024-2025", ciclo: "Primer Ciclo", grado: 1, seccion: "A", grupo: "1.º A", especialidad: "Nivel Secundario General (1.er Ciclo)", abandonos: 0 },
  { id: 2, anio: "2024-2025", ciclo: "Primer Ciclo", grado: 1, seccion: "B", grupo: "1.º B", especialidad: "Nivel Secundario General (1.er Ciclo)", abandonos: 0 },
  { id: 3, anio: "2024-2025", ciclo: "Primer Ciclo", grado: 1, seccion: "C", grupo: "1.º C", especialidad: "Nivel Secundario General (1.er Ciclo)", abandonos: 0 },
  { id: 4, anio: "2024-2025", ciclo: "Primer Ciclo", grado: 1, seccion: "D", grupo: "1.º D", especialidad: "Nivel Secundario General (1.er Ciclo)", abandonos: 1 },
  { id: 5, anio: "2024-2025", ciclo: "Primer Ciclo", grado: 2, seccion: "A", grupo: "2.º A", especialidad: "Nivel Secundario General (1.er Ciclo)", abandonos: 2 },
  { id: 6, anio: "2024-2025", ciclo: "Primer Ciclo", grado: 2, seccion: "B", grupo: "2.º B", especialidad: "Nivel Secundario General (1.er Ciclo)", abandonos: 2 },
  { id: 7, anio: "2024-2025", ciclo: "Primer Ciclo", grado: 3, seccion: "A", grupo: "3.º A", especialidad: "Nivel Secundario General (1.er Ciclo)", abandonos: 1 },
  { id: 8, anio: "2024-2025", ciclo: "Primer Ciclo", grado: 3, seccion: "B", grupo: "3.º B", especialidad: "Nivel Secundario General (1.er Ciclo)", abandonos: 0 },
  { id: 9, anio: "2024-2025", ciclo: "Segundo Ciclo", grado: 4, seccion: "A", grupo: "4.º A", especialidad: "Producción Agropecuaria", abandonos: 1 },
  { id: 10, anio: "2024-2025", ciclo: "Segundo Ciclo", grado: 4, seccion: "B", grupo: "4.º B", especialidad: "Comercio y Mercadeo", abandonos: 1 },
  { id: 11, anio: "2024-2025", ciclo: "Segundo Ciclo", grado: 4, seccion: "C", grupo: "4.º C", especialidad: "Gestión Administrativa y Tributaria", abandonos: 0 },
  { id: 12, anio: "2024-2025", ciclo: "Segundo Ciclo", grado: 5, seccion: "A", grupo: "5.º A", especialidad: "Producción Agropecuaria", abandonos: 1 },
  { id: 13, anio: "2024-2025", ciclo: "Segundo Ciclo", grado: 5, seccion: "B", grupo: "5.º B", especialidad: "Comercio y Mercadeo", abandonos: 0 },
  { id: 14, anio: "2024-2025", ciclo: "Segundo Ciclo", grado: 5, seccion: "C", grupo: "5.º C", especialidad: "Gestión Administrativa y Tributaria", abandonos: 0 },
  { id: 15, anio: "2024-2025", ciclo: "Segundo Ciclo", grado: 6, seccion: "A", grupo: "6.º A", especialidad: "Producción Agropecuaria", abandonos: 0 },
  { id: 16, anio: "2024-2025", ciclo: "Segundo Ciclo", grado: 6, seccion: "B", grupo: "6.º B", especialidad: "Comercio y Mercadeo", abandonos: 0 },
  { id: 17, anio: "2024-2025", ciclo: "Segundo Ciclo", grado: 6, seccion: "C", grupo: "6.º C", especialidad: "Gestión Administrativa y Tributaria", abandonos: 0 },

  // Período 2025-2026 (16 secciones reportadas, 15 abandonos; 1.º D no reportada)
  { id: 18, anio: "2025-2026", ciclo: "Primer Ciclo", grado: 1, seccion: "A", grupo: "1.º A", especialidad: "Nivel Secundario General (1.er Ciclo)", abandonos: 1 },
  { id: 19, anio: "2025-2026", ciclo: "Primer Ciclo", grado: 1, seccion: "B", grupo: "1.º B", especialidad: "Nivel Secundario General (1.er Ciclo)", abandonos: 1 },
  { id: 20, anio: "2025-2026", ciclo: "Primer Ciclo", grado: 1, seccion: "C", grupo: "1.º C", especialidad: "Nivel Secundario General (1.er Ciclo)", abandonos: 4 },
  { id: 21, anio: "2025-2026", ciclo: "Primer Ciclo", grado: 2, seccion: "A", grupo: "2.º A", especialidad: "Nivel Secundario General (1.er Ciclo)", abandonos: 1 },
  { id: 22, anio: "2025-2026", ciclo: "Primer Ciclo", grado: 2, seccion: "B", grupo: "2.º B", especialidad: "Nivel Secundario General (1.er Ciclo)", abandonos: 2 },
  { id: 23, anio: "2025-2026", ciclo: "Primer Ciclo", grado: 3, seccion: "A", grupo: "3.º A", especialidad: "Nivel Secundario General (1.er Ciclo)", abandonos: 1 },
  { id: 24, anio: "2025-2026", ciclo: "Primer Ciclo", grado: 3, seccion: "B", grupo: "3.º B", especialidad: "Nivel Secundario General (1.er Ciclo)", abandonos: 0 },
  { id: 25, anio: "2025-2026", ciclo: "Segundo Ciclo", grado: 4, seccion: "A", grupo: "4.º A", especialidad: "Producción Agropecuaria", abandonos: 2 },
  { id: 26, anio: "2025-2026", ciclo: "Segundo Ciclo", grado: 4, seccion: "B", grupo: "4.º B", especialidad: "Comercio y Mercadeo", abandonos: 0 },
  { id: 27, anio: "2025-2026", ciclo: "Segundo Ciclo", grado: 4, seccion: "C", grupo: "4.º C", especialidad: "Gestión Administrativa y Tributaria", abandonos: 0 },
  { id: 28, anio: "2025-2026", ciclo: "Segundo Ciclo", grado: 5, seccion: "A", grupo: "5.º A", especialidad: "Producción Agropecuaria", abandonos: 2 },
  { id: 29, anio: "2025-2026", ciclo: "Segundo Ciclo", grado: 5, seccion: "B", grupo: "5.º B", especialidad: "Comercio y Mercadeo", abandonos: 0 },
  { id: 30, anio: "2025-2026", ciclo: "Segundo Ciclo", grado: 5, seccion: "C", grupo: "5.º C", especialidad: "Gestión Administrativa y Tributaria", abandonos: 1 },
  { id: 31, anio: "2025-2026", ciclo: "Segundo Ciclo", grado: 6, seccion: "A", grupo: "6.º A", especialidad: "Producción Agropecuaria", abandonos: 0 },
  { id: 32, anio: "2025-2026", ciclo: "Segundo Ciclo", grado: 6, seccion: "B", grupo: "6.º B", especialidad: "Comercio y Mercadeo", abandonos: 0 },
  { id: 33, anio: "2025-2026", ciclo: "Segundo Ciclo", grado: 6, seccion: "C", grupo: "6.º C", especialidad: "Gestión Administrativa y Tributaria", abandonos: 0 }
];

function renderizarTablaInteractiva() {
  const filtroAnio = document.getElementById("filtro-anio");
  const filtroCiclo = document.getElementById("filtro-ciclo");
  const filtroGrado = document.getElementById("filtro-grado");
  const filtroEsp = document.getElementById("filtro-esp");
  const tbody = document.getElementById("tabla-registros-body");
  const resumenFiltro = document.getElementById("resumen-filtro-dinamico");

  if (!tbody) return;

  const valAnio = filtroAnio ? filtroAnio.value : "TODOS";
  const valCiclo = filtroCiclo ? filtroCiclo.value : "TODOS";
  const valGrado = filtroGrado ? filtroGrado.value : "TODOS";
  const valEsp = filtroEsp ? filtroEsp.value : "TODOS";

  const filtrados = REGISTROS_VERIFICADOS_SIAAE.filter((r) => {
    const okAnio = valAnio === "TODOS" || r.anio === valAnio;
    const okCiclo = valCiclo === "TODOS" || r.ciclo === valCiclo;
    const okGrado = valGrado === "TODOS" || String(r.grado) === valGrado;
    const okEsp = valEsp === "TODOS" || r.especialidad === valEsp;
    return okAnio && okCiclo && okGrado && okEsp;
  });

  tbody.innerHTML = "";
  let sumaAbandonos = 0;

  filtrados.forEach((fila) => {
    sumaAbandonos += fila.abandonos;
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td class="num-col">${fila.id}</td>
      <td><strong>${fila.anio}</strong></td>
      <td>${fila.ciclo}</td>
      <td class="num-col">${fila.grado}.º</td>
      <td>${fila.seccion}</td>
      <td><strong>${fila.grupo}</strong></td>
      <td>${fila.especialidad}</td>
      <td class="num-col"><strong>${fila.abandonos}</strong></td>
      <td><span style="color:#0f766e;font-weight:700;">Confirmado</span></td>
    `;
    tbody.appendChild(tr);
  });

  const promedio = filtrados.length > 0 ? (sumaAbandonos / filtrados.length).toFixed(4) : "0.0000";
  if (resumenFiltro) {
    resumenFiltro.innerHTML = `
      Mostrando <strong>${filtrados.length}</strong> de <strong>33</strong> secciones-año verificadas &nbsp;|&nbsp;
      Total de abandonos en la selección: <strong>${sumaAbandonos} casos</strong> &nbsp;|&nbsp;
      Promedio por sección seleccionada: <strong>${promedio}</strong>
    `;
  }
}

function restablecerFiltros() {
  ["filtro-anio", "filtro-ciclo", "filtro-grado", "filtro-esp"].forEach((id) => {
    const el = document.getElementById(id);
    if (el) el.value = "TODOS";
  });
  renderizarTablaInteractiva();
}

function actualizarCalculadoraPedagogica() {
  const sliderB0 = document.getElementById("demo-b0");
  const sliderB1 = document.getElementById("demo-b1");
  const sliderX = document.getElementById("demo-x");
  const salida = document.getElementById("demo-logit-output");

  if (!sliderB0 || !sliderB1 || !sliderX || !salida) return;

  const b0 = parseFloat(sliderB0.value);
  const b1 = parseFloat(sliderB1.value);
  const x = parseFloat(sliderX.value);

  document.getElementById("val-b0").textContent = b0.toFixed(2);
  document.getElementById("val-b1").textContent = b1.toFixed(2);
  document.getElementById("val-x").textContent = x.toFixed(2);

  const z = b0 + b1 * x;
  const prob = 1.0 / (1.0 + Math.exp(-z));
  const oddsRatio = Math.exp(b1);

  salida.innerHTML = `
    <strong>Combinación lineal (z = β₀ + β₁·x):</strong> ${z.toFixed(3)} &nbsp;|&nbsp;
    <strong>Probabilidad logística teórica σ(z):</strong> ${(prob * 100).toFixed(2)}% &nbsp;|&nbsp;
    <strong>Odds Ratio teórico (e^β₁):</strong> ${oddsRatio.toFixed(3)}
  `;
}

document.addEventListener("DOMContentLoaded", () => {
  ["filtro-anio", "filtro-ciclo", "filtro-grado", "filtro-esp"].forEach((id) => {
    const el = document.getElementById(id);
    if (el) el.addEventListener("change", renderizarTablaInteractiva);
  });

  const btnReset = document.getElementById("btn-reset-filtros");
  if (btnReset) btnReset.addEventListener("click", restablecerFiltros);

  ["demo-b0", "demo-b1", "demo-x"].forEach((id) => {
    const el = document.getElementById(id);
    if (el) el.addEventListener("input", actualizarCalculadoraPedagogica);
  });

  renderizarTablaInteractiva();
  actualizarCalculadoraPedagogica();
});
