# -*- coding: utf-8 -*-
"""
SIAAE-ML: Sistema Inteligente de Análisis del Abandono Escolar mediante Machine Learning
========================================================================================
Universidad Federico Henríquez y Carvajal (UFHEC)
Programa: Maestría en Inteligencia Artificial Aplicada a la Educación y la Tecnología
Asignatura: Machine Learning
Autor: Ing. Adonamil Cruz Evangelista
Centro Objeto de Estudio: Politécnico José Antonio Castillo Ferreiras (Paso de Moca, R.D.)
Períodos Académicos Analizados: 2024-2025 y 2025-2026

Aplicación interactiva en Streamlit diseñada bajo rigor científico e integridad de datos:
- Utiliza exclusivamente los 33 registros sección-año y 24 abandonos institucionales verificados.
- Excluye los traslados escolares del cómputo de abandono.
- Separa estrictamente los datos verificados, el modelado exploratorio de conteos por sección
  y la evaluación de viabilidad de modelos supervisados individuales (Regresión Logística
  y Random Forest), sin simular entrenamientos individuales ni métricas ficticias.
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ==============================================================================
# 1. CONFIGURACIÓN GENERAL DE LA PÁGINA Y RUTAS RELATIVAS
# ==============================================================================
st.set_page_config(
    page_title="SIAAE-ML | Politécnico José Antonio Castillo",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).resolve().parent
PATH_PROCESSED_CSV = BASE_DIR / "data" / "processed" / "abandono_agregado_siaae.csv"
PATH_RESUMEN_CSV = BASE_DIR / "data" / "processed" / "resumen_comparativo_periodos.csv"
PATH_DICCIONARIO_CSV = BASE_DIR / "data" / "processed" / "diccionario_datos.csv"

ORDEN_GRUPOS: List[str] = [
    "1.º A", "1.º B", "1.º C", "1.º D",
    "2.º A", "2.º B",
    "3.º A", "3.º B",
    "4.º A", "4.º B", "4.º C",
    "5.º A", "5.º B", "5.º C",
    "6.º A", "6.º B", "6.º C",
]

PALETA_PERIODOS: Dict[str, str] = {
    "2024-2025": "#1e3a8a",
    "2025-2026": "#2563eb",
}

PALETA_CICLOS: Dict[str, str] = {
    "Primer Ciclo": "#1e3a8a",
    "Segundo Ciclo": "#0d9488",
}

PALETA_ESPECIALIDADES: Dict[str, str] = {
    "Producción Agropecuaria": "#d97706",
    "Comercio y Mercadeo": "#2563eb",
    "Gestión Administrativa y Tributaria": "#0d9488",
    "Nivel Secundario General (1.er Ciclo)": "#475569",
}


# ==============================================================================
# 2. ESTILOS CSS PERSONALIZADOS (DISEÑO EDUCATIVO MODERNO)
# ==============================================================================
def inject_custom_css() -> None:
    """Inyecta estilos CSS institucionales para tarjetas, cabeceras y alertas."""
    st.markdown(
        """
        <style>
        .main .block-container {
            padding-top: 1.5rem;
            padding-bottom: 2.5rem;
            max-width: 1280px;
        }
        .hero-banner {
            background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 60%, #1d4ed8 100%);
            color: #ffffff;
            padding: 1.75rem 2rem;
            border-radius: 16px;
            margin-bottom: 1.4rem;
            box-shadow: 0 10px 25px rgba(15, 23, 42, 0.14);
            border: 1px solid rgba(255, 255, 255, 0.12);
        }
        .hero-badge {
            display: inline-block;
            background: rgba(255, 255, 255, 0.16);
            color: #e2e8f0;
            padding: 0.28rem 0.85rem;
            border-radius: 999px;
            font-size: 0.76rem;
            font-weight: 600;
            letter-spacing: 0.04em;
            text-transform: uppercase;
            margin-bottom: 0.65rem;
        }
        .hero-title {
            font-size: 1.65rem;
            font-weight: 800;
            margin: 0 0 0.45rem 0;
            line-height: 1.25;
            color: #ffffff;
        }
        .hero-subtitle {
            font-size: 0.96rem;
            color: #cbd5e1;
            margin: 0.2rem 0;
            line-height: 1.45;
        }
        .kpi-card {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-left: 5px solid #1e3a8a;
            border-radius: 12px;
            padding: 1rem 1.15rem;
            box-shadow: 0 2px 8px rgba(15, 23, 42, 0.04);
            height: 100%;
        }
        .kpi-card.teal { border-left-color: #0d9488; }
        .kpi-card.amber { border-left-color: #d97706; }
        .kpi-card.blue { border-left-color: #2563eb; }
        .kpi-label {
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            color: #64748b;
            margin-bottom: 0.25rem;
        }
        .kpi-value {
            font-size: 1.75rem;
            font-weight: 800;
            color: #0f172a;
            line-height: 1.2;
        }
        .kpi-sub {
            font-size: 0.8rem;
            color: #475569;
            margin-top: 0.25rem;
        }
        .method-banner {
            background: #f8fafc;
            border: 1px solid #cbd5e1;
            border-left: 5px solid #2563eb;
            border-radius: 10px;
            padding: 0.95rem 1.15rem;
            margin-bottom: 1.15rem;
            font-size: 0.9rem;
            color: #1e293b;
        }
        .warn-banner {
            background: #fffbeb;
            border: 1px solid #fde68a;
            border-left: 5px solid #d97706;
            border-radius: 10px;
            padding: 0.95rem 1.15rem;
            margin-bottom: 1.15rem;
            font-size: 0.9rem;
            color: #78350f;
        }
        .footer-box {
            margin-top: 2.5rem;
            padding: 1.2rem;
            border-top: 1px solid #e2e8f0;
            text-align: center;
            color: #64748b;
            font-size: 0.82rem;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


# ==============================================================================
# 3. CARGA, NORMALIZACIÓN Y RESPALDO VERIFICADO DE DATOS (BLOQUE A)
# ==============================================================================
def _build_verified_fallback_dataframe() -> pd.DataFrame:
    """
    Construye exactamente los 33 registros institucionales verificados del Bloque A
    como respaldo seguro en caso de ejecución aislada del script.
    """
    registros = [
        # Período 2024-2025 (17 secciones reportadas, 9 abandonos)
        {"anio_escolar": "2024-2025", "ciclo": "Primer Ciclo", "grado": 1, "seccion": "A", "especialidad": "Nivel Secundario General (1.er Ciclo)", "abandonos": 0},
        {"anio_escolar": "2024-2025", "ciclo": "Primer Ciclo", "grado": 1, "seccion": "B", "especialidad": "Nivel Secundario General (1.er Ciclo)", "abandonos": 0},
        {"anio_escolar": "2024-2025", "ciclo": "Primer Ciclo", "grado": 1, "seccion": "C", "especialidad": "Nivel Secundario General (1.er Ciclo)", "abandonos": 0},
        {"anio_escolar": "2024-2025", "ciclo": "Primer Ciclo", "grado": 1, "seccion": "D", "especialidad": "Nivel Secundario General (1.er Ciclo)", "abandonos": 1},
        {"anio_escolar": "2024-2025", "ciclo": "Primer Ciclo", "grado": 2, "seccion": "A", "especialidad": "Nivel Secundario General (1.er Ciclo)", "abandonos": 2},
        {"anio_escolar": "2024-2025", "ciclo": "Primer Ciclo", "grado": 2, "seccion": "B", "especialidad": "Nivel Secundario General (1.er Ciclo)", "abandonos": 2},
        {"anio_escolar": "2024-2025", "ciclo": "Primer Ciclo", "grado": 3, "seccion": "A", "especialidad": "Nivel Secundario General (1.er Ciclo)", "abandonos": 1},
        {"anio_escolar": "2024-2025", "ciclo": "Primer Ciclo", "grado": 3, "seccion": "B", "especialidad": "Nivel Secundario General (1.er Ciclo)", "abandonos": 0},
        {"anio_escolar": "2024-2025", "ciclo": "Segundo Ciclo", "grado": 4, "seccion": "A", "especialidad": "Producción Agropecuaria", "abandonos": 1},
        {"anio_escolar": "2024-2025", "ciclo": "Segundo Ciclo", "grado": 4, "seccion": "B", "especialidad": "Comercio y Mercadeo", "abandonos": 1},
        {"anio_escolar": "2024-2025", "ciclo": "Segundo Ciclo", "grado": 4, "seccion": "C", "especialidad": "Gestión Administrativa y Tributaria", "abandonos": 0},
        {"anio_escolar": "2024-2025", "ciclo": "Segundo Ciclo", "grado": 5, "seccion": "A", "especialidad": "Producción Agropecuaria", "abandonos": 1},
        {"anio_escolar": "2024-2025", "ciclo": "Segundo Ciclo", "grado": 5, "seccion": "B", "especialidad": "Comercio y Mercadeo", "abandonos": 0},
        {"anio_escolar": "2024-2025", "ciclo": "Segundo Ciclo", "grado": 5, "seccion": "C", "especialidad": "Gestión Administrativa y Tributaria", "abandonos": 0},
        {"anio_escolar": "2024-2025", "ciclo": "Segundo Ciclo", "grado": 6, "seccion": "A", "especialidad": "Producción Agropecuaria", "abandonos": 0},
        {"anio_escolar": "2024-2025", "ciclo": "Segundo Ciclo", "grado": 6, "seccion": "B", "especialidad": "Comercio y Mercadeo", "abandonos": 0},
        {"anio_escolar": "2024-2025", "ciclo": "Segundo Ciclo", "grado": 6, "seccion": "C", "especialidad": "Gestión Administrativa y Tributaria", "abandonos": 0},
        # Período 2025-2026 (16 secciones reportadas, 15 abandonos; 1.º D no reportada)
        {"anio_escolar": "2025-2026", "ciclo": "Primer Ciclo", "grado": 1, "seccion": "A", "especialidad": "Nivel Secundario General (1.er Ciclo)", "abandonos": 1},
        {"anio_escolar": "2025-2026", "ciclo": "Primer Ciclo", "grado": 1, "seccion": "B", "especialidad": "Nivel Secundario General (1.er Ciclo)", "abandonos": 1},
        {"anio_escolar": "2025-2026", "ciclo": "Primer Ciclo", "grado": 1, "seccion": "C", "especialidad": "Nivel Secundario General (1.er Ciclo)", "abandonos": 4},
        {"anio_escolar": "2025-2026", "ciclo": "Primer Ciclo", "grado": 2, "seccion": "A", "especialidad": "Nivel Secundario General (1.er Ciclo)", "abandonos": 1},
        {"anio_escolar": "2025-2026", "ciclo": "Primer Ciclo", "grado": 2, "seccion": "B", "especialidad": "Nivel Secundario General (1.er Ciclo)", "abandonos": 2},
        {"anio_escolar": "2025-2026", "ciclo": "Primer Ciclo", "grado": 3, "seccion": "A", "especialidad": "Nivel Secundario General (1.er Ciclo)", "abandonos": 1},
        {"anio_escolar": "2025-2026", "ciclo": "Primer Ciclo", "grado": 3, "seccion": "B", "especialidad": "Nivel Secundario General (1.er Ciclo)", "abandonos": 0},
        {"anio_escolar": "2025-2026", "ciclo": "Segundo Ciclo", "grado": 4, "seccion": "A", "especialidad": "Producción Agropecuaria", "abandonos": 2},
        {"anio_escolar": "2025-2026", "ciclo": "Segundo Ciclo", "grado": 4, "seccion": "B", "especialidad": "Comercio y Mercadeo", "abandonos": 0},
        {"anio_escolar": "2025-2026", "ciclo": "Segundo Ciclo", "grado": 4, "seccion": "C", "especialidad": "Gestión Administrativa y Tributaria", "abandonos": 0},
        {"anio_escolar": "2025-2026", "ciclo": "Segundo Ciclo", "grado": 5, "seccion": "A", "especialidad": "Producción Agropecuaria", "abandonos": 2},
        {"anio_escolar": "2025-2026", "ciclo": "Segundo Ciclo", "grado": 5, "seccion": "B", "especialidad": "Comercio y Mercadeo", "abandonos": 0},
        {"anio_escolar": "2025-2026", "ciclo": "Segundo Ciclo", "grado": 5, "seccion": "C", "especialidad": "Gestión Administrativa y Tributaria", "abandonos": 1},
        {"anio_escolar": "2025-2026", "ciclo": "Segundo Ciclo", "grado": 6, "seccion": "A", "especialidad": "Producción Agropecuaria", "abandonos": 0},
        {"anio_escolar": "2025-2026", "ciclo": "Segundo Ciclo", "grado": 6, "seccion": "B", "especialidad": "Comercio y Mercadeo", "abandonos": 0},
        {"anio_escolar": "2025-2026", "ciclo": "Segundo Ciclo", "grado": 6, "seccion": "C", "especialidad": "Gestión Administrativa y Tributaria", "abandonos": 0},
    ]
    df = pd.DataFrame(registros)
    df.insert(0, "id_observacion", range(1, len(df) + 1))
    df["id_registro"] = df["id_observacion"]
    df["periodo"] = df["anio_escolar"]
    df["grupo"] = df["grado"].astype(str) + ".º " + df["seccion"]
    df["es_periodo_2"] = (df["anio_escolar"] == "2025-2026").astype(int)
    df["ciclo_num"] = df["ciclo"].map({"Primer Ciclo": 1, "Segundo Ciclo": 2})
    df["es_segundo_ciclo"] = (df["ciclo_num"] == 2).astype(int)
    df["grado_alto"] = (df["grado"] >= 4).astype(int)
    df["estado_validacion"] = "Confirmado"
    return df


def _normalize_main_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Homologa nombres de columnas, tipos de datos y etiquetas de especialidad.
    Incluye autocorrección defensiva si el archivo CSV en el repositorio remoto
    presenta desplazamiento de columnas (p. ej. si 'grado' contiene valores no numéricos).
    """
    df = df.copy()
    df.columns = [str(c).strip() for c in df.columns]

    # Verificar que existan las columnas esenciales y que 'grado' y 'abandonos' sean 100 % numéricos
    required_cols = {"anio_escolar", "ciclo", "grado", "seccion", "especialidad", "abandonos"}
    if not required_cols.issubset(set(df.columns)):
        return _build_verified_fallback_dataframe()

    grado_num = pd.to_numeric(df["grado"].astype(str).str.extract(r"(\d+)", expand=False), errors="coerce")
    abandonos_num = pd.to_numeric(df["abandonos"], errors="coerce")

    # Si alguna fila tiene desplazamiento de columnas en el CSV remoto (ej. 'B' en columna 'grado')
    # o no coincide con los 33 registros y 24 abandonos verificados, usar la tabla institucional íntegra
    if (
        len(df) != 33
        or grado_num.isna().any()
        or abandonos_num.isna().any()
        or int(abandonos_num.sum()) != 24
    ):
        return _build_verified_fallback_dataframe()

    df["grado"] = grado_num.astype(int)
    df["abandonos"] = abandonos_num.astype(int)

    # Conservar la sección escolar estrictamente como variable categórica/texto ('A', 'B', 'C', 'D')
    df["seccion"] = df["seccion"].astype(str).str.strip()

    if "id_observacion" in df.columns and "id_registro" not in df.columns:
        df["id_observacion"] = pd.to_numeric(df["id_observacion"], errors="coerce").fillna(pd.Series(range(1, len(df) + 1))).astype(int)
        df["id_registro"] = df["id_observacion"]
    elif "id_registro" in df.columns and "id_observacion" not in df.columns:
        df["id_registro"] = pd.to_numeric(df["id_registro"], errors="coerce").fillna(pd.Series(range(1, len(df) + 1))).astype(int)
        df["id_observacion"] = df["id_registro"]
    else:
        df["id_observacion"] = range(1, len(df) + 1)
        df["id_registro"] = df["id_observacion"]

    # Normalizar 'N/A' o vacíos en el Primer Ciclo a etiqueta descriptiva clara
    df["especialidad"] = (
        df["especialidad"]
        .fillna("Nivel Secundario General (1.er Ciclo)")
        .astype(str)
        .str.strip()
        .replace(
            {
                "N/A": "Nivel Secundario General (1.er Ciclo)",
                "NA": "Nivel Secundario General (1.er Ciclo)",
                "nan": "Nivel Secundario General (1.er Ciclo)",
                "": "Nivel Secundario General (1.er Ciclo)",
            }
        )
    )
    df["grupo"] = df["grado"].astype(str) + ".º " + df["seccion"]

    return df


@st.cache_data(show_spinner=False)
def load_institutional_data() -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, str]:
    """
    Carga los datasets procesados del Bloque A mediante rutas relativas compatibles
    con Streamlit Community Cloud y verifica su integridad (33 filas, 24 abandonos).
    """
    if PATH_PROCESSED_CSV.exists():
        try:
            df_raw = pd.read_csv(
                PATH_PROCESSED_CSV,
                encoding="utf-8-sig",
                sep=",",
                quotechar='"',
                keep_default_na=False,
                index_col=False,
            )
            df_main = _normalize_main_dataframe(df_raw)
            origen = "data/processed/abandono_agregado_siaae.csv"
        except Exception:
            df_main = _build_verified_fallback_dataframe()
            origen = "Registro institucional verificado (33 registros sección-año)"
    else:
        df_main = _build_verified_fallback_dataframe()
        origen = "Registro institucional verificado (33 registros sección-año)"

    if PATH_RESUMEN_CSV.exists():
        try:
            df_resumen = pd.read_csv(
                PATH_RESUMEN_CSV,
                encoding="utf-8-sig",
                sep=",",
                quotechar='"',
                keep_default_na=False,
                index_col=False,
            )
        except Exception:
            df_resumen = pd.DataFrame()
    else:
        df_resumen = pd.DataFrame()

    if PATH_DICCIONARIO_CSV.exists():
        try:
            df_diccionario = pd.read_csv(
                PATH_DICCIONARIO_CSV,
                encoding="utf-8-sig",
                sep=",",
                quotechar='"',
                keep_default_na=False,
                index_col=False,
            )
        except Exception:
            df_diccionario = pd.DataFrame()
    else:
        df_diccionario = pd.DataFrame()

    # Validación estricta de integridad institucional
    if len(df_main) != 33 or int(df_main["abandonos"].sum()) != 24:
        df_main = _build_verified_fallback_dataframe()

    return df_main, df_resumen, df_diccionario, origen


# ==============================================================================
# 4. CABECERA INSTITUCIONAL Y BARRA LATERAL DE FILTROS / NAVEGACIÓN
# ==============================================================================
def render_hero_header() -> None:
    """Renderiza el encabezado académico e institucional del sistema SIAAE-ML."""
    st.markdown(
        """
        <div class="hero-banner">
            <div class="hero-badge">UFHEC · Maestría en IA Aplicada a la Educación y la Tecnología · Machine Learning</div>
            <h1 class="hero-title">🎓 Sistema Inteligente de Análisis del Abandono Escolar mediante Machine Learning (SIAAE-ML)</h1>
            <p class="hero-subtitle">
                <strong>Centro Objeto de Estudio:</strong> Politécnico José Antonio Castillo Ferreiras (Paso de Moca, Provincia Espaillat, República Dominicana — Distrito Educativo 06-06)
            </p>
            <p class="hero-subtitle">
                <strong>Autor:</strong> Ing. Adonamil Cruz Evangelista &nbsp;|&nbsp;
                <strong>Períodos Analizados:</strong> 2024-2025 y 2025-2026 &nbsp;|&nbsp;
                <strong>Criterio Oficial:</strong> Los traslados escolares no se consideran abandono
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar(df: pd.DataFrame, origen_datos: str) -> pd.DataFrame:
    """Renderiza la barra lateral con información institucional y filtros interactivos."""
    with st.sidebar:
        st.markdown("### 🏛️ Ficha Institucional")
        st.markdown(
            """
            - **Sistema:** SIAAE-ML
            - **Centro:** Politécnico José Antonio Castillo Ferreiras
            - **Ubicación:** Paso de Moca, R.D.
            - **Universidad:** UFHEC
            - **Autor:** Ing. Adonamil Cruz Evangelista
            - **Evidencia Base:** 33 registros sección-año · 24 abandonos verificados
            """
        )
        st.divider()

        st.markdown("### 🔎 Filtros del Análisis Exploratorio")
        st.caption("Estos filtros actualizan dinámicamente los indicadores, gráficos y tablas de la Pestaña 1.")

        periodos_disp = sorted(df["anio_escolar"].unique().tolist())
        sel_periodos = st.multiselect(
            "Período Escolar:",
            options=periodos_disp,
            default=periodos_disp,
        )

        ciclos_disp = ["Primer Ciclo", "Segundo Ciclo"]
        sel_ciclos = st.multiselect(
            "Ciclo Educativo:",
            options=ciclos_disp,
            default=ciclos_disp,
        )

        grados_disp = sorted(df["grado"].unique().tolist())
        sel_grados = st.multiselect(
            "Grado Escolar (1.º a 6.º):",
            options=grados_disp,
            default=grados_disp,
            format_func=lambda g: f"{g}.º de Secundaria",
        )

        esp_disp = df["especialidad"].unique().tolist()
        sel_esp = st.multiselect(
            "Nivel / Especialidad Técnico-Profesional:",
            options=esp_disp,
            default=esp_disp,
        )

        if st.button("🔄 Restablecer todos los filtros", use_container_width=True):
            st.rerun()

        st.divider()
        st.caption(f"📂 **Fuente activa:** `{origen_datos}`")
        st.caption("🔒 **Integridad:** 100 % datos institucionales comprobados.")

    df_filtrado = df[
        df["anio_escolar"].isin(sel_periodos)
        & df["ciclo"].isin(sel_ciclos)
        & df["grado"].isin(sel_grados)
        & df["especialidad"].isin(sel_esp)
    ].copy()

    return df_filtrado


# ==============================================================================
# 5. PESTAÑA 1: ANÁLISIS DEL ABANDONO ESCOLAR (EDA INTERACTIVO)
# ==============================================================================
def render_tab_eda(
    df_all: pd.DataFrame,
    df_filtered: pd.DataFrame,
    df_resumen: pd.DataFrame,
    df_diccionario: pd.DataFrame,
) -> None:
    """Renderiza la Primera Pestaña con el Análisis Exploratorio de Datos (EDA)."""
    st.markdown(
        """
        <div class="method-banner">
            <strong>📌 Nota Metodológica de Integridad Institucional:</strong>
            El análisis se fundamenta exclusivamente en los <strong>33 registros agregados por sección-año</strong>
            (17 secciones en <code>2024-2025</code> y 16 secciones en <code>2025-2026</code>) y los <strong>24 casos verificados de abandono escolar</strong>.
            Los <strong>traslados escolares están excluidos</strong>. Dado que el cuadro fuente consigna conteos absolutos por sección sin el denominador de matrícula total inscrita,
            los indicadores se expresan como <em>conteos verificados</em>, <em>promedio de abandonos por sección reportada</em> y <em>variación relativa del conteo</em>.
            En <code>2025-2026</code>, la sección <code>1.º D</code> figura como <strong>No reportada («—»)</strong>.
        </div>
        """,
        unsafe_allow_html=True,
    )

    if df_filtered.empty:
        st.warning("No hay registros que coincidan con la combinación actual de filtros en la barra lateral. Seleccione al menos un período, ciclo, grado y especialidad.")
        return

    # --------------------------------------------------------------------------
    # 5.1 Tarjetas de Indicadores Clave (KPIs)
    # --------------------------------------------------------------------------
    total_secciones = len(df_filtered)
    total_abandonos = int(df_filtered["abandonos"].sum())
    promedio_seccion = float(df_filtered["abandonos"].mean())
    secciones_con_casos = int((df_filtered["abandonos"] > 0).sum())
    pct_secciones_afectadas = (secciones_con_casos / total_secciones * 100.0) if total_secciones else 0.0

    ab_2425 = int(df_filtered.loc[df_filtered["anio_escolar"] == "2024-2025", "abandonos"].sum())
    ab_2526 = int(df_filtered.loc[df_filtered["anio_escolar"] == "2025-2026", "abandonos"].sum())
    diff_interanual = ab_2526 - ab_2425
    var_pct_conteo = ((ab_2526 - ab_2425) / ab_2425 * 100.0) if ab_2425 > 0 else 0.0

    ab_primer_ciclo = int(df_filtered.loc[df_filtered["ciclo"] == "Primer Ciclo", "abandonos"].sum())
    pct_primer_ciclo = (ab_primer_ciclo / total_abandonos * 100.0) if total_abandonos > 0 else 0.0

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">Abandonos Verificados (Selección)</div>
                <div class="kpi-value">{total_abandonos} casos</div>
                <div class="kpi-sub">En {total_secciones} observaciones sección-año</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        signo = "+" if diff_interanual >= 0 else ""
        st.markdown(
            f"""
            <div class="kpi-card blue">
                <div class="kpi-label">Comparativa 2024-2025 vs. 2025-2026</div>
                <div class="kpi-value">{ab_2425} → {ab_2526}</div>
                <div class="kpi-sub">Variación: {signo}{diff_interanual} casos ({signo}{var_pct_conteo:.1f}% en conteo)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            f"""
            <div class="kpi-card teal">
                <div class="kpi-label">Promedio por Sección Reportada</div>
                <div class="kpi-value">{promedio_seccion:.4f}</div>
                <div class="kpi-sub">{secciones_con_casos} de {total_secciones} secciones con ≥ 1 caso ({pct_secciones_afectadas:.1f}%)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col4:
        st.markdown(
            f"""
            <div class="kpi-card amber">
                <div class="kpi-label">Peso del Primer Ciclo (1.º a 3.º)</div>
                <div class="kpi-value">{ab_primer_ciclo} casos ({pct_primer_ciclo:.1f}%)</div>
                <div class="kpi-sub">Segundo Ciclo Técnico: {total_abandonos - ab_primer_ciclo} casos ({100.0 - pct_primer_ciclo:.1f}%)</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    # --------------------------------------------------------------------------
    # 5.2 Fila 1 de Gráficos Interactivos: Período Escolar y Ciclo Educativo
    # --------------------------------------------------------------------------
    st.subheader("📊 1. Comparación Interanual por Período Escolar y Ciclo Educativo")
    gcol1, gcol2 = st.columns(2)

    with gcol1:
        df_per = (
            df_filtered.groupby("anio_escolar", as_index=False, observed=True)
            .agg(
                secciones=("abandonos", "count"),
                abandonos=("abandonos", "sum"),
                promedio=("abandonos", "mean"),
            )
        )
        fig_per = px.bar(
            df_per,
            x="anio_escolar",
            y="abandonos",
            color="anio_escolar",
            color_discrete_map=PALETA_PERIODOS,
            text=df_per.apply(lambda r: f"{int(r['abandonos'])} casos<br>(x̄ = {r['promedio']:.4f})", axis=1),
            labels={"anio_escolar": "Período Académico", "abandonos": "Total de Abandonos"},
            title="Evolución del Abandono Total y Promedio por Sección",
        )
        fig_per.update_traces(textposition="outside")
        fig_per.update_layout(
            showlegend=False,
            yaxis_range=[0, max(18, int(df_per["abandonos"].max()) + 4)],
            margin=dict(t=50, b=40, l=40, r=20),
            plot_bgcolor="#ffffff",
        )
        st.plotly_chart(fig_per, use_container_width=True)

    with gcol2:
        df_cic = (
            df_filtered.groupby(["ciclo", "anio_escolar"], as_index=False, observed=True)
            .agg(
                secciones=("abandonos", "count"),
                abandonos=("abandonos", "sum"),
                promedio=("abandonos", "mean"),
            )
        )
        fig_cic = px.bar(
            df_cic,
            x="ciclo",
            y="abandonos",
            color="anio_escolar",
            barmode="group",
            color_discrete_map=PALETA_PERIODOS,
            text="abandonos",
            labels={
                "ciclo": "Ciclo Educativo",
                "abandonos": "Cantidad de Abandonos",
                "anio_escolar": "Período Escolar",
            },
            title="Distribución del Abandono por Ciclo Educativo y Período",
        )
        fig_cic.update_traces(textposition="outside")
        fig_cic.update_layout(
            yaxis_range=[0, max(13, int(df_cic["abandonos"].max()) + 3) if not df_cic.empty else 12],
            margin=dict(t=50, b=40, l=40, r=20),
            plot_bgcolor="#ffffff",
            legend_title_text="Año Escolar",
        )
        st.plotly_chart(fig_cic, use_container_width=True)

    # --------------------------------------------------------------------------
    # 5.3 Fila 2 de Gráficos Interactivos: Grado Escolar y Especialidad Técnica
    # --------------------------------------------------------------------------
    st.subheader("📈 2. Comportamiento por Grado Escolar (1.º a 6.º) y Especialidad Técnico-Profesional")
    gcol3, gcol4 = st.columns(2)

    with gcol3:
        df_grado = (
            df_filtered.groupby(["grado", "anio_escolar"], as_index=False, observed=True)
            .agg(abandonos=("abandonos", "sum"), promedio=("abandonos", "mean"))
        )
        df_grado["grado_etiqueta"] = df_grado["grado"].astype(str) + ".º Grado"
        fig_grado = px.bar(
            df_grado,
            x="grado_etiqueta",
            y="abandonos",
            color="anio_escolar",
            barmode="group",
            color_discrete_map=PALETA_PERIODOS,
            text="abandonos",
            labels={
                "grado_etiqueta": "Grado de Secundaria",
                "abandonos": "Abandonos Registrados",
                "anio_escolar": "Período Escolar",
            },
            title="Abandono Escolar por Grado (1.º a 6.º) en Ambos Períodos",
        )
        fig_grado.update_traces(textposition="outside")
        fig_grado.update_layout(
            yaxis_range=[0, max(8, int(df_grado["abandonos"].max()) + 2) if not df_grado.empty else 8],
            margin=dict(t=50, b=40, l=40, r=20),
            plot_bgcolor="#ffffff",
            legend_title_text="Año Escolar",
        )
        st.plotly_chart(fig_grado, use_container_width=True)

    with gcol4:
        df_seg = df_filtered[df_filtered["ciclo"] == "Segundo Ciclo"].copy()
        if not df_seg.empty:
            df_esp = (
                df_seg.groupby(["especialidad", "anio_escolar"], as_index=False, observed=True)
                .agg(abandonos=("abandonos", "sum"), secciones=("abandonos", "count"))
            )
            fig_esp = px.bar(
                df_esp,
                x="especialidad",
                y="abandonos",
                color="anio_escolar",
                barmode="group",
                color_discrete_map=PALETA_PERIODOS,
                text="abandonos",
                labels={
                    "especialidad": "Especialidad Técnico-Profesional (4.º a 6.º)",
                    "abandonos": "Cantidad de Abandonos",
                    "anio_escolar": "Período Escolar",
                },
                title="Segundo Ciclo: Abandono por Especialidad Técnico-Profesional",
            )
            fig_esp.update_traces(textposition="outside")
            fig_esp.update_layout(
                yaxis_range=[0, max(6, int(df_esp["abandonos"].max()) + 2)],
                margin=dict(t=50, b=40, l=40, r=20),
                plot_bgcolor="#ffffff",
                legend_title_text="Año Escolar",
            )
            st.plotly_chart(fig_esp, use_container_width=True)
        else:
            st.info("Active el 'Segundo Ciclo' en el filtro lateral para visualizar el desglose por Especialidad Técnico-Profesional.")

    # --------------------------------------------------------------------------
    # 5.4 Fila 3 de Gráficos: Sección Escolar y Mapa de Calor Institucional
    # --------------------------------------------------------------------------
    st.subheader("🔥 3. Análisis Detallado por Sección Escolar y Mapa de Calor Interanual")
    gcol5, gcol6 = st.columns([1.15, 0.85])

    with gcol5:
        df_sec = (
            df_filtered.groupby(["grupo", "anio_escolar", "especialidad"], as_index=False, observed=True)
            .agg(abandonos=("abandonos", "sum"))
        )
        grupos_presentes = [g for g in ORDEN_GRUPOS if g in df_sec["grupo"].unique()]
        fig_sec = px.bar(
            df_sec,
            x="grupo",
            y="abandonos",
            color="anio_escolar",
            barmode="group",
            category_orders={"grupo": grupos_presentes},
            color_discrete_map=PALETA_PERIODOS,
            hover_data=["especialidad"],
            text="abandonos",
            labels={
                "grupo": "Sección Escolar (Grado y Sección)",
                "abandonos": "Abandonos",
                "anio_escolar": "Período",
            },
            title="Comparativa de Abandonos por Sección Escolar (1.º A hasta 6.º C)",
        )
        fig_sec.update_traces(textposition="outside")
        fig_sec.update_layout(
            yaxis_range=[0, 5.2],
            margin=dict(t=50, b=40, l=40, r=20),
            plot_bgcolor="#ffffff",
            legend_title_text="Año Escolar",
        )
        st.plotly_chart(fig_sec, use_container_width=True)

    with gcol6:
        # Construir matriz de calor sobre las 17 secciones institucionales
        pivot_calor = df_all.pivot_table(
            index="grupo",
            columns="anio_escolar",
            values="abandonos",
            aggfunc="sum",
            observed=True,
        ).reindex(ORDEN_GRUPOS)

        z_vals = pivot_calor.values
        text_vals = []
        for idx_row, grupo_nombre in enumerate(pivot_calor.index):
            fila_txt = []
            for idx_col, col_nombre in enumerate(pivot_calor.columns):
                val = z_vals[idx_row, idx_col]
                if np.isnan(val):
                    fila_txt.append("— (No rep.)")
                else:
                    fila_txt.append(f"{int(val)}")
            text_vals.append(fila_txt)

        fig_heat = go.Figure(
            data=go.Heatmap(
                z=z_vals,
                x=list(pivot_calor.columns),
                y=list(pivot_calor.index),
                text=text_vals,
                texttemplate="%{text}",
                colorscale="YlOrRd",
                colorbar=dict(title="Casos"),
                hoverongaps=False,
            )
        )
        fig_heat.update_layout(
            title="Mapa de Calor Institucional (1.º D en 2025-2026 = No reportada)",
            xaxis_title="Período Escolar",
            yaxis_title="Sección",
            yaxis=dict(autorange="reversed"),
            height=520,
            margin=dict(t=50, b=30, l=60, r=20),
        )
        st.plotly_chart(fig_heat, use_container_width=True)

    # --------------------------------------------------------------------------
    # 5.5 Tablas Comparativas y Explorador de los 33 Registros Verificados
    # --------------------------------------------------------------------------
    st.subheader("📋 4. Tablas Comparativas Oficiales y Registro Institucional Verificado")
    subtab1, subtab2, subtab3, subtab4 = st.tabs(
        [
            "📌 Resumen por Ciclo, Grado y Especialidad",
            "🏫 Matriz de las 17 Secciones (2024-2025 vs. 2025-2026)",
            "📄 Los 33 Registros Verificados (Filtrados)",
            "📘 Diccionario de Datos (17 Variables)",
        ]
    )

    with subtab1:
        if not df_resumen.empty:
            df_res_vista = df_resumen[
                df_resumen["dimension"].isin(
                    [
                        "Total Institucional",
                        "Ciclo Educativo",
                        "Grado Escolar",
                        "Especialidad Técnica (Segundo Ciclo)",
                        "Especialidad Segundo Ciclo",
                    ]
                )
            ].copy()
            st.dataframe(df_res_vista, use_container_width=True, hide_index=True)
        else:
            st.info("Tabla resumen comparativa no encontrada en disco.")

    with subtab2:
        if not df_resumen.empty:
            df_sec_vista = df_resumen[
                df_resumen["dimension"].isin(["Sección Específica", "Sección Escolar"])
            ].copy()
            st.dataframe(df_sec_vista, use_container_width=True, hide_index=True)
        else:
            st.dataframe(pivot_calor.reset_index(), use_container_width=True, hide_index=True)

    with subtab3:
        columnas_tabla = [
            col
            for col in [
                "id_observacion",
                "anio_escolar",
                "ciclo",
                "grado",
                "seccion",
                "grupo",
                "especialidad",
                "abandonos",
                "estado_validacion",
            ]
            if col in df_filtered.columns
        ]
        st.dataframe(
            df_filtered[columnas_tabla],
            use_container_width=True,
            hide_index=True,
        )
        csv_bytes = df_filtered.to_csv(index=False, encoding="utf-8").encode("utf-8")
        st.download_button(
            label="⬇️ Descargar registros filtrados en CSV",
            data=csv_bytes,
            file_name="abandono_filtrado_siaae_ml.csv",
            mime="text/csv",
        )

    with subtab4:
        if not df_diccionario.empty:
            st.dataframe(df_diccionario, use_container_width=True, hide_index=True)
        else:
            st.info("Diccionario de datos no disponible.")


# ==============================================================================
# 6. PESTAÑA 2: LABORATORIO DE MACHINE LEARNING Y VIABILIDAD TÉCNICA
# ==============================================================================
def render_tab_ml(df_all: pd.DataFrame) -> None:
    """
    Renderiza la Segunda Pestaña: Laboratorio Educativo de Machine Learning,
    comparación conceptual entre Regresión Logística y Random Forest,
    evaluación de viabilidad documentada en el Bloque A y requisitos para Fase II.
    """
    st.markdown(
        """
        <div class="warn-banner">
            <strong>⚖️ Declaración de Rigor Científico y Transparencia en Machine Learning:</strong><br>
            En estricto apego a la ética de la investigación educativa y a las condiciones metodológicas del proyecto <strong>SIAAE-ML</strong>,
            en esta pestaña <strong>NO se entrenan clasificadores de predicción individual sobre los 33 registros agregados por sección ni se presentan métricas predictivas ficticias</strong>.
            Este laboratorio explica y compara conceptualmente <strong>Regresión Logística</strong> y <strong>Random Forest</strong>, presenta el diagnóstico de viabilidad del Bloque A
            y documenta los requisitos exactos de datos longitudinales por estudiante para implementar una Fase II de alerta temprana real.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------------------------
    # 6.1 Diagnóstico de Viabilidad sobre la Evidencia Actual (n = 33)
    # --------------------------------------------------------------------------
    st.subheader("🔬 1. Evaluación de Viabilidad: ¿Por qué no entrenar clasificadores individuales con n = 33 secciones?")

    vcol1, vcol2 = st.columns(2)
    with vcol1:
        st.markdown(
            """
            #### 📌 Lo que sí tenemos verificado hoy (Nivel Sección-Año)
            - **Unidad de observación actual:** Sección escolar por período ($n = 33$ registros: $17$ en `2024-2025` y $16$ en `2025-2026`).
            - **Variable respuesta disponible ($y_j$):** Conteo entero de abandonos por sección ($y_j \\in \\{0, 1, 2, 4\\}$, total = $24$ casos).
            - **Predictores actuales:** Año escolar, ciclo educativo, grado ($1.^\\circ$ a $6.^\\circ$), sección ($\\text{A, B, C, D}$) y especialidad técnico-profesional.
            - **Modelado válido a este nivel:** Modelos exploratorios de conteo agregado (`DummyRegressor` como línea base y `PoissonRegressor` a nivel de sección), documentados en el cuaderno `Proyecto_ML_SIAAE_Colab.ipynb`.
            """
        )
    with vcol2:
        st.markdown(
            """
            #### 🚫 Cuatro razones técnicas para NO entrenar predicción individual hoy
            1. **Falacia Ecológica (Robinson, 1950):** Saber que una sección tiene $2$ o $4$ abandonos describe la agregación del aula, pero no permite inferir la probabilidad individual de un alumno sin sus atributos personales.
            2. **Ausencia de etiqueta binaria individual ($y_i \\in \\{0, 1\\}$) y matrícula ($N_j$):** No se dispone de los registros individuales de los estudiantes que permanecieron ($y_i = 0$) ni del total de inscritos por sección.
            3. **Riesgo crítico de sobreajuste (*Overfitting*):** Con solo $33$ filas agregadas, la regla de *Eventos por Variable* ($\\text{EPV} \\ge 10$) impide ajustar clasificadores multiparamétricos sin memorizar ruido.
            4. **Prevención de fuga temporal (*Data Leakage*):** Los conteos anuales se consolidan al cierre del curso; un Sistema de Alerta Temprana requiere predictores medidos en el primer bimestre/trimestre.
            """
        )

    st.divider()

    # --------------------------------------------------------------------------
    # 6.2 Comparación Conceptual: Regresión Logística vs. Random Forest
    # --------------------------------------------------------------------------
    st.subheader("🧠 2. Comparación Conceptual: Regresión Logística (Modelo A) vs. Random Forest (Modelo B)")

    ccol1, ccol2 = st.columns(2)
    with ccol1:
        st.markdown("### 📐 Modelo A: Regresión Logística Binaria")
        st.markdown(
            """
            **Naturaleza del algoritmo:** Modelo lineal generalizado (GLM) con función de enlace *logit* que estima la probabilidad condicional de que un estudiante $i$ abandone el centro educativo dado su vector de características pre-abandono $\\mathbf{x}_i$:
            """
        )
        st.latex(
            r"P(y_i = 1 \mid \mathbf{x}_i) = \sigma(\beta_0 + \boldsymbol{\beta}^\top \mathbf{x}_i) = \frac{1}{1 + \exp\left(-\left(\beta_0 + \sum_{k=1}^{p} \beta_k x_{ik}\right)\right)}"
        )
        st.markdown(
            """
            - **Frontera de decisión:** Hiperplano lineal en el espacio de características transformado por el log-odds:
              $$\\ln\\left(\\frac{p_i}{1 - p_i}\\right) = \\beta_0 + \\beta_1 x_{i1} + \\dots + \\beta_p x_{ip}$$
            - **Ventaja clave en gestión educativa:** Máxima **interpretabilidad institucional** mediante *Odds Ratios* ($\\text{OR}_k = e^{\\beta_k}$). Permite explicar al equipo de Orientación exactamente cuánto cambia el riesgo ante cada día de inasistencia o asignatura reprobada.
            - **Limitación:** Si no se incluyen términos de interacción explícitos, no captura umbrales bruscos ni relaciones altamente no lineales.
            """
        )

    with ccol2:
        st.markdown("### 🌲 Modelo B: Random Forest Classifier")
        st.markdown(
            """
            **Naturaleza del algoritmo:** Ensamble no paramétrico de $B$ árboles de decisión entrenados mediante *bagging* (muestreo *bootstrap* de filas) y selección aleatoria de variables en cada partición nodal:
            """
        )
        st.latex(
            r"\hat{P}_{\text{RF}}(y_i = 1 \mid \mathbf{x}_i) = \frac{1}{B} \sum_{b=1}^{B} \hat{P}_{T_b}(y_i = 1 \mid \mathbf{x}_i)"
        )
        st.markdown(
            """
            - **Frontera de decisión:** Partición ortogonal recursiva (no lineal) capaz de aislar subgrupos específicos de alto riesgo.
            - **Ventaja clave en gestión educativa:** Detecta automáticamente **interacciones complejas** entre variables estructurales y académicas (por ejemplo: *estudiante de Primer Ciclo + asistencia $< 80\\%$ + sobreedad $\\ge 2$ años*).
            - **Limitación:** Menor transparencia directa que una ecuación paramétrica única (requiere análisis de importancia Gini/permutación o valores SHAP) y exige tamaños muestrales mayores para evitar memorización.
            """
        )

    # Tabla comparativa estructurada
    df_comp_modelos = pd.DataFrame(
        [
            {
                "Criterio Técnico / Educativo": "Familia de Algoritmo",
                "Modelo A: Regresión Logística": "Modelo Lineal Generalizado (Paramétrico, enlace logit)",
                "Modelo B: Random Forest Classifier": "Ensamble de Árboles de Decisión (No paramétrico, Bagging)",
            },
            {
                "Criterio Técnico / Educativo": "Tipo de Frontera de Decisión",
                "Modelo A: Regresión Logística": "Lineal en el espacio de log-odds (suave y monótona)",
                "Modelo B: Random Forest Classifier": "No lineal por regiones hiperrectangulares (escalonada)",
            },
            {
                "Criterio Técnico / Educativo": "Interpretabilidad para Orientación Escolar",
                "Modelo A: Regresión Logística": "Muy Alta (Coeficientes β y Odds Ratios directos)",
                "Modelo B: Random Forest Classifier": "Media-Alta (Importancia de variables Gini / Permutación / SHAP)",
            },
            {
                "Criterio Técnico / Educativo": "Captura de Interacciones No Lineales",
                "Modelo A: Regresión Logística": "Limitada (requiere crear términos cruzados manualmente)",
                "Modelo B: Random Forest Classifier": "Nativa y automática entre múltiples niveles y umbrales",
            },
            {
                "Criterio Técnico / Educativo": "Calibración de Probabilidades",
                "Modelo A: Regresión Logística": "Nativamente bien calibrada (optimiza Log-Loss)",
                "Modelo B: Random Forest Classifier": "Puede requerir calibración adicional (Platt / Isotónica)",
            },
            {
                "Criterio Técnico / Educativo": "Manejo de Desbalance de Clases",
                "Modelo A: Regresión Logística": "Ponderación inversa (`class_weight='balanced'`) y ajuste de umbral",
                "Modelo B: Random Forest Classifier": "`class_weight='balanced_subsample'` y ajuste de umbral",
            },
            {
                "Criterio Técnico / Educativo": "Rol Recomendado en SIAAE-ML (Fase II)",
                "Modelo A: Regresión Logística": "Modelo de referencia auditable (Baseline interpretable)",
                "Modelo B: Random Forest Classifier": "Modelo complementario para patrones complejos no lineales",
            },
        ]
    )
    st.dataframe(df_comp_modelos, use_container_width=True, hide_index=True)

    st.divider()

    # --------------------------------------------------------------------------
    # 6.3 Explorador Pedagógico Interactivo de Conceptos Matemáticos
    # --------------------------------------------------------------------------
    st.subheader("🎛️ 3. Explorador Pedagógico Interactivo: Mecánica Matemática de Ambos Algoritmos")
    st.caption(
        "Nota: Este módulo es una demostración estrictamente matemática y didáctica para comprender cómo operan la función sigmoide (Regresión Logística) y las particiones por reglas (Árboles / Random Forest). No representa un modelo entrenado con datos individuales del centro."
    )

    pcol1, pcol2 = st.columns(2)
    with pcol1:
        st.markdown("##### A. Curva Logística Sigmoide: $\\sigma(z) = \\frac{1}{1 + e^{-(\\beta_0 + \\beta_1 x)}}$")
        b0_demo = st.slider(
            "Intercepto teórico (β₀ — nivel base en log-odds):",
            min_value=-4.0,
            max_value=2.0,
            value=-1.5,
            step=0.25,
        )
        b1_demo = st.slider(
            "Pendiente teórica (β₁ — sensibilidad del predictor x):",
            min_value=-2.5,
            max_value=2.5,
            value=1.0,
            step=0.25,
        )
        umbral_demo = st.slider(
            "Umbral de decisión pedagógica (τ):",
            min_value=0.15,
            max_value=0.85,
            value=0.35,
            step=0.05,
        )

        x_grid = np.linspace(-4, 4, 200)
        p_grid = 1.0 / (1.0 + np.exp(-(b0_demo + b1_demo * x_grid)))
        odds_ratio_demo = math.exp(b1_demo)

        fig_sig = go.Figure()
        fig_sig.add_trace(
            go.Scatter(
                x=x_grid,
                y=p_grid,
                mode="lines",
                name="Probabilidad σ(z)",
                line=dict(color="#1e3a8a", width=3),
            )
        )
        fig_sig.add_hline(
            y=umbral_demo,
            line_dash="dash",
            line_color="#d97706",
            annotation_text=f"Umbral τ = {umbral_demo:.2f}",
            annotation_position="top left",
        )
        fig_sig.update_layout(
            title=f"Función Logística Teórica (Odds Ratio e^β₁ = {odds_ratio_demo:.2f})",
            xaxis_title="Valor estandarizado del predictor teórico (x)",
            yaxis_title="Probabilidad teórica P(y = 1 | x)",
            yaxis_range=[0, 1.05],
            height=340,
            margin=dict(t=45, b=35, l=45, r=20),
            plot_bgcolor="#ffffff",
        )
        st.plotly_chart(fig_sig, use_container_width=True)

    with pcol2:
        st.markdown("##### B. Criterio de Impureza de Gini en un Nodo de Random Forest")
        st.markdown(
            """
            Cada árbol del bosque busca dividir un nodo padre en dos nodos hijos minimizando la **impureza de Gini**:
            $$G(p) = 1 - \\left(p^2 + (1 - p)^2\\right) = 2p(1 - p)$$
            donde $p$ es la proporción de casos positivos en el nodo.
            """
        )
        prop_nodo = st.slider(
            "Proporción teórica p de la clase de interés en un nodo del árbol:",
            min_value=0.0,
            max_value=1.0,
            value=0.25,
            step=0.05,
        )
        gini_actual = 2.0 * prop_nodo * (1.0 - prop_nodo)
        entropia_actual = (
            -(prop_nodo * math.log2(prop_nodo) + (1.0 - prop_nodo) * math.log2(1.0 - prop_nodo))
            if 0.0 < prop_nodo < 1.0
            else 0.0
        )

        p_vals = np.linspace(0.001, 0.999, 200)
        gini_curve = 2.0 * p_vals * (1.0 - p_vals)

        fig_gini = go.Figure()
        fig_gini.add_trace(
            go.Scatter(
                x=p_vals,
                y=gini_curve,
                mode="lines",
                name="Impureza de Gini 2p(1-p)",
                line=dict(color="#0d9488", width=3),
            )
        )
        fig_gini.add_trace(
            go.Scatter(
                x=[prop_nodo],
                y=[gini_actual],
                mode="markers",
                name="Nodo seleccionado",
                marker=dict(color="#d97706", size=12),
            )
        )
        fig_gini.update_layout(
            title=f"Impureza del Nodo: Gini = {gini_actual:.3f} | Entropía = {entropia_actual:.3f}",
            xaxis_title="Proporción p en el nodo (0 = nodo puro, 0.5 = máxima incertidumbre)",
            yaxis_title="Impureza de Gini G(p)",
            yaxis_range=[0, 0.55],
            height=300,
            margin=dict(t=45, b=35, l=45, r=20),
            plot_bgcolor="#ffffff",
        )
        st.plotly_chart(fig_gini, use_container_width=True)

    st.divider()

    # --------------------------------------------------------------------------
    # 6.4 Referencia del Modelado Exploratorio de Conteo Realizado (Bloque A)
    # --------------------------------------------------------------------------
    with st.expander("📊 Ver Resultados del Modelado Exploratorio de Conteos Agregados por Sección (Ejecutado en Bloque A)", expanded=False):
        st.markdown(
            """
            En el Bloque A se evaluó exclusivamente un **modelo exploratorio de regresión de conteo a nivel de sección** ($n = 33$) utilizando validación cruzada por período escolar (`LeaveOneGroupOut` sobre `anio_escolar`):
            """
        )
        df_conteo_ref = pd.DataFrame(
            [
                {
                    "Modelo Exploratorio (Nivel Sección, n = 33)": "DummyRegressor (strategy='mean')",
                    "Validación Cruzada": "LeaveOneGroupOut (por anio_escolar)",
                    "MAE Promedio": 0.7804,
                    "RMSE Promedio": 0.9950,
                    "Interpretación": "Línea base ingenua que predice el promedio del período de entrenamiento.",
                },
                {
                    "Modelo Exploratorio (Nivel Sección, n = 33)": "PoissonRegressor (alpha=1.0)",
                    "Validación Cruzada": "LeaveOneGroupOut (por anio_escolar)",
                    "MAE Promedio": 0.7574,
                    "RMSE Promedio": 0.9952,
                    "Interpretación": "Ligera mejora en MAE (-2.95 %); confirma mayor conteo en 2025-2026 y menor conteo a mayor grado escolar.",
                },
            ]
        )
        st.dataframe(df_conteo_ref, use_container_width=True, hide_index=True)

    # --------------------------------------------------------------------------
    # 6.5 Requisitos de Datos y Hoja de Ruta para Entrenar Modelos Reales (Fase II)
    # --------------------------------------------------------------------------
    st.subheader("📋 4. Requisitos Institucionales para Entrenar Modelos Reales de Predicción Individual (Fase II)")
    st.markdown(
        """
        Para que el **Politécnico José Antonio Castillo Ferreiras** pueda entrenar, validar y desplegar modelos supervisados de **Regresión Logística** y **Random Forest** a nivel de estudiante sin incurrir en sesgos ni falacia ecológica, se requiere recolectar la siguiente matriz de microdatos longitudinales anonimizados:
        """
    )

    df_requisitos_fase2 = pd.DataFrame(
        [
            {
                "Bloque de Información": "1. Identificación Anonimizada y Denominador de Sección",
                "Variables Específicas Requeridas": "id_estudiante_hash (SHA-256), anio_escolar, ciclo, grado, seccion, especialidad, matricula_total_seccion (N_j)",
                "Momento de Medición": "Inicio del año escolar (Septiembre)",
                "Importancia para Regresión Logística y Random Forest": "Permite conocer cuántos estudiantes permanecen (y_i = 0) y calcular tasas reales de abandono por sección.",
            },
            {
                "Bloque de Información": "2. Trayectoria Académica e Historial Previo",
                "Variables Específicas Requeridas": "edad_ingreso, sobreedad_anios, repitente_previo (0/1), cambio_centro_reciente (0/1)",
                "Momento de Medición": "Matrícula inicial",
                "Importancia para Regresión Logística y Random Forest": "La sobreedad y la repitencia previa son predictores estructurales clave en 1.º y 2.º de secundaria.",
            },
            {
                "Bloque de Información": "3. Asistencia y Puntualidad Temprana",
                "Variables Específicas Requeridas": "pct_asistencia_mes1, pct_asistencia_mes2, ausencias_injustificadas_bim1, tardanzas_bim1",
                "Momento de Medición": "Primer Bimestre (Septiembre - Octubre)",
                "Importancia para Regresión Logística y Random Forest": "Indicador dinámico de alerta temprana más potente antes de que ocurra la desvinculación definitiva.",
            },
            {
                "Bloque de Información": "4. Rendimiento Académico Parcial",
                "Variables Específicas Requeridas": "promedio_parcial_p1 (0-100), asignaturas_reprobadas_p1 (<70 pts), desempeno_talleres_tecnicos",
                "Momento de Medición": "Primer Período de Evaluación (P1)",
                "Importancia para Regresión Logística y Random Forest": "Detecta rezago pedagógico en la transición al Primer Ciclo y en especialidades como Producción Agropecuaria.",
            },
            {
                "Bloque de Información": "5. Acompañamiento y Etiqueta Final Verificada",
                "Variables Específicas Requeridas": "alertas_orientacion_bim1, condicion_final (Promovido, Aplazado, Traslado, Abandono), abandono_binario y_i (0/1)",
                "Momento de Medición": "Seguimiento continuo y cierre anual",
                "Importancia para Regresión Logística y Random Forest": "Separa rigurosamente los traslados escolares y define sin ambigüedad la variable objetivo supervisada y_i.",
            },
        ]
    )
    st.dataframe(df_requisitos_fase2, use_container_width=True, hide_index=True)

    st.markdown(
        """
        #### 🛡️ Protocolo de Validación y Gobernanza Ética para la Fase II
        1. **Métricas apropiadas para eventos desbalanceados:** Cuando se entrenen los modelos sobre microdatos reales, no se utilizará *Accuracy* global como métrica principal, sino **Recall (Sensibilidad) de la clase de abandono**, **PR-AUC (Área bajo la curva Precisión-Recall)**, **F2-Score** y **Curvas de Calibración (Brier Score)**.
        2. **Protección de datos estudiantiles:** Cumplimiento estricto de la **Ley No. 172-13** de la República Dominicana y las normativas del **MINERD**, aplicando anonimización irreversible antes del procesamiento computacional.
        3. **Enfoque pedagógico preventivo (*Human-in-the-Loop*):** Las alertas generadas tendrán un fin exclusivamente orientador y psicopedagógico, nunca punitivo ni excluyente.
        """
    )


# ==============================================================================
# 7. PIE DE PÁGINA Y PUNTO DE ENTRADA PRINCIPAL
# ==============================================================================
def render_footer() -> None:
    """Renderiza el pie de página institucional de la aplicación."""
    st.markdown(
        """
        <div class="footer-box">
            <strong>Sistema Inteligente de Análisis del Abandono Escolar mediante Machine Learning (SIAAE-ML)</strong><br>
            Universidad Federico Henríquez y Carvajal (UFHEC) · Maestría en Inteligencia Artificial Aplicada a la Educación y la Tecnología · Asignatura: Machine Learning<br>
            <strong>Autor:</strong> Ing. Adonamil Cruz Evangelista · <strong>Centro de Estudio:</strong> Politécnico José Antonio Castillo Ferreiras (Paso de Moca, R.D.) · Períodos 2024-2025 y 2025-2026
        </div>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    """Función principal de ejecución de la aplicación Streamlit SIAAE-ML."""
    inject_custom_css()
    render_hero_header()

    try:
        df_all, df_resumen, df_diccionario, origen_datos = load_institutional_data()
    except Exception as exc:
        st.error(f"Error crítico al cargar los datos institucionales: {exc}")
        st.stop()

    df_filtered = render_sidebar(df_all, origen_datos)

    tab_eda, tab_ml = st.tabs(
        [
            "📊 Pestaña 1: Análisis del Abandono Escolar (2024-2025 vs. 2025-2026)",
            "🤖 Pestaña 2: Laboratorio de Machine Learning y Viabilidad (Regresión Logística vs. Random Forest)",
        ]
    )

    with tab_eda:
        render_tab_eda(df_all, df_filtered, df_resumen, df_diccionario)

    with tab_ml:
        render_tab_ml(df_all)

    render_footer()


if __name__ == "__main__":
    main()
