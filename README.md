# 📊 ACCESO DIRECTO AL PORTAL INTERACTIVO SIAAE-ML
### 🔗 [VER GRÁFICOS Y RESULTADOS DEL PROYECTO](https://adonamil46.github.io/SIAAE-ML-Abandono-Escolar/#graficos)
**Explora las visualizaciones estadísticas, los resultados y las evidencias del Sistema Inteligente de Análisis del Abandono Escolar mediante Machine Learning.**
# 🎓 Sistema Inteligente de Análisis del Abandono Escolar mediante Machine Learning (SIAAE-ML)
[![Universidad](https://img.shields.io/badge/Universidad-UFHEC-1e3a8a?style=for-the-badge)](https://ufhec.edu.do/)
[![Programa](https://img.shields.io/badge/Maestr%C3%ADa-IA%20Aplicada%20a%20la%20Educaci%C3%B3n-2563eb?style=for-the-badge)](#autor-e-institucion)
[![Python](https://img.shields.io/badge/Python-3.11%2B-0d9488?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App%20Desplegada-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://siaae-ml-abandono-escolar-fkdckk6h2ejqtmvhqzq9a6.streamlit.app/)
[![Metodología](https://img.shields.io/badge/Metodolog%C3%ADa-CRISP--ML(Q)-d97706?style=for-the-badge)](docs/documentacion_crisp_ml.md)
[![Datos](https://img.shields.io/badge/Datos%20Verificados-33%20Secciones%20%7C%2024%20Abandonos-16a34a?style=for-the-badge)](data/processed/abandono_agregado_siaae.csv)

> **Investigación aplicada de Ciencia de Datos y Machine Learning sobre la permanencia y el abandono escolar en el Politécnico José Antonio Castillo Ferreiras (Paso de Moca, Provincia Espaillat, República Dominicana) durante los períodos académicos `2024-2025` y `2025-2026`.**
>
> 🚀 **Aplicación Interactiva en Vivo (Streamlit Community Cloud):** [https://siaae-ml-abandono-escolar-fkdckk6h2ejqtmvhqzq9a6.streamlit.app/](https://siaae-ml-abandono-escolar-fkdckk6h2ejqtmvhqzq9a6.streamlit.app/)

---

## 📋 1. Descripción General del Sistema

El **Sistema Inteligente de Análisis del Abandono Escolar mediante Machine Learning (SIAAE-ML)** es un proyecto académico integral, interactivo y reproducible desarrollado en el marco de la asignatura **Machine Learning** de la **Maestría en Inteligencia Artificial Aplicada a la Educación y la Tecnología** en la **Universidad Federico Henríquez y Carvajal (UFHEC)**.

El sistema analiza exclusivamente los **33 registros institucionales verificados a nivel de sección-año** ($17$ secciones en `2024-2025` y $16$ secciones en `2025-2026`, sumando **24 casos confirmados de abandono escolar** y excluyendo rigurosamente los traslados) para:
1. Identificar patrones de concentración del abandono por **período académico**, **ciclo educativo**, **grado escolar (`1.º` a `6.º`)**, **sección (`A`, `B`, `C`, `D`)** y **especialidad técnico-profesional**.
2. Evaluar modelos exploratorios de conteo agregado a nivel de sección (`DummyRegressor` y `PoissonRegressor` con validación cruzada por período).
3. Documentar con rigor metodológico la **viabilidad técnica de modelos supervisados individuales (`Regresión Logística` y `Random Forest Classifier`)**, especificando los microdatos longitudinales necesarios para una Fase II de alerta temprana sin caer en falacia ecológica ni inventar registros.

---

## 👨‍💻 2. Autor e Institución Académica {#autor-e-institucion}

- **Autor:** Ing. Adonamil Cruz Evangelista
- **Universidad:** Universidad Federico Henríquez y Carvajal (UFHEC)
- **Programa:** Maestría en Inteligencia Artificial Aplicada a la Educación y la Tecnología
- **Asignatura:** Machine Learning
- **Centro Educativo Objeto del Estudio:** Politécnico José Antonio Castillo Ferreiras (Paso de Moca, Municipio de Moca, Provincia Espaillat, República Dominicana — Distrito Educativo 06-06, Regional 06 La Vega)
- **Períodos Académicos Analizados:** `2024-2025` y `2025-2026`

---

## 🎯 3. Objetivos del Proyecto

### Objetivo General
Desarrollar el **Sistema Inteligente de Análisis del Abandono Escolar mediante Machine Learning (SIAAE-ML)** para el Politécnico José Antonio Castillo Ferreiras (`2024-2025` y `2025-2026`), integrando auditoría de datos verificados, análisis exploratorio comparativo, modelado exploratorio de conteos y diseño técnico de viabilidad para clasificadores supervisados de apoyo a la decisión educativa.

### Objetivos Específicos
1. **Auditar y estructurar** los 33 registros sección-año y los 24 abandonos verificados del centro educativo (excluyendo traslados), documentando un diccionario técnico de 17 variables.
2. **Comparar multidimensionalmente** la evolución del abandono entre `2024-2025` y `2025-2026` por ciclo, grado, sección y especialidad técnico-profesional.
3. **Evaluar la viabilidad metodológica** de **Regresión Logística** y **Random Forest**, diferenciando entre el análisis de conteos por sección y la predicción de riesgo individual.
4. **Desplegar un ecosistema interactivo** compuesto por un cuaderno de Google Colab, una aplicación web en Streamlit Community Cloud y una landing page científica para GitHub Pages.

---

## 🛠️ 4. Tecnologías Utilizadas

- **Lenguaje y Procesamiento de Datos:** Python 3.11+, `pandas`, `numpy`
- **Machine Learning y Validación:** `scikit-learn` (`DummyRegressor`, `PoissonRegressor`, `LeaveOneGroupOut`)
- **Visualización Científica e Interactiva:** `plotly`, `matplotlib`, `seaborn`, gráficos vectoriales `SVG`
- **Aplicación Web en la Nube:** `streamlit` (Streamlit Community Cloud)
- **Portal Web Científico (GitHub Pages):** HTML5 semántico (`index.html`), CSS3 modular (`assets/css/styles.css`) y JavaScript ES6 (`assets/js/main.js`)
- **Entorno de Cómputo Reproducible:** Jupyter Notebook / Google Colab (`Proyecto_ML_SIAAE_Colab.ipynb`)

---

## 📂 5. Estructura de Carpetas del Proyecto

```text
SIAAE-ML-Maestria/
│
├── index.html                                      # Landing page científica e interactiva (GitHub Pages)
├── app.py                                          # Aplicación interactiva principal en Streamlit
├── requirements.txt                                # Dependencias verificadas para Streamlit Cloud
├── Proyecto_ML_SIAAE_Colab.ipynb                   # Cuaderno mejorado compatible con Google Colab
├── README.md                                       # Documentación principal del repositorio
│
├── Archivos_proyecto/                              # Fuentes institucionales originales (100% intactas)
│   ├── Material_1_Proyecto_ML_UFHEC .docx          # Plantilla académica de UFHEC
│   ├── Material_1_Proyecto_ML_UFHEC.txt            # Copia de texto extraída para lectura
│   ├── Proyecto__ML_SIAAE.ipynb                    # Cuaderno computacional original intacto
│   ├── SIAAE_ML_Abandono_Verificado.docx           # Documento institucional de datos verificados
│   └── SIAAE_ML_Abandono_Verificado.txt            # Copia de texto extraída para verificación
│
├── data/
│   ├── raw/
│   │   └── abandono_institucional_verificado.csv   # 33 registros originales verificados
│   └── processed/
│       ├── abandono_agregado_siaae.csv             # Dataset procesado con variables derivadas (ETL)
│       ├── resumen_comparativo_periodos.csv        # Matriz comparativa 2024-2025 vs. 2025-2026
│       └── diccionario_datos.csv                   # Diccionario técnico de las 17 variables
│
├── results/
│   ├── figures/                                    # 6 gráficos vectoriales SVG de alta resolución
│   │   ├── fig1_abandono_por_periodo.svg
│   │   ├── fig2_abandono_por_ciclo.svg
│   │   ├── fig3_abandono_por_grado.svg
│   │   ├── fig4_abandono_por_seccion_y_especialidad.svg
│   │   ├── fig5_mapa_calor_grado_periodo.svg
│   │   └── fig6_distribucion_conteos_seccion.svg
│   └── reports/
│       ├── reporte_eda_comparativo.md              # Informe detallado del Análisis Exploratorio (EDA)
│       └── reporte_calidad_abandono.html           # Reporte HTML de auditoría de calidad de datos
│
├── docs/
│   ├── documentacion_crisp_ml.md                   # Documentación científica integral CRISP-ML(Q)
│   └── viabilidad_ml_supervisado.md                # Viabilidad técnica de Regresión Logística y Random Forest
│
├── assets/
│   ├── css/
│   │   └── styles.css                              # Estilos de la landing page
│   ├── js/
│   │   └── main.js                                 # Filtros dinámicos y demostrador matemático JS
│   └── images/
│       ├── ilustracion_hero_siaae.svg              # Ilustración principal del sistema SIAAE-ML
│       ├── diagrama_crisp_ml.svg                   # Diagrama de las 6 fases CRISP-ML(Q)
│       └── ilustracion_permanencia_ia.svg          # Esquema de prevención temprana e IA ética
│
├── models/
│   └── README.md                                   # Nota metodológica sobre modelos y prevención de sobreajuste
└── video/
    └── README.md                                   # Espacio reservado para producción audiovisual (Bloque D)
```

---

## 🔄 6. Metodología CRISP-ML(Q)

El desarrollo sigue las etapas del estándar **CRISP-ML(Q)** documentadas en detalle en [`docs/documentacion_crisp_ml.md`](docs/documentacion_crisp_ml.md):
1. **Comprensión del problema educativo:** Delimitación del abandono escolar en el Politécnico José Antonio Castillo excluyendo traslados.
2. **Comprensión y auditoría de datos:** Verificación cruzada 100 % exacta de los 33 registros sección-año y 24 abandonos.
3. **Preparación de datos (ETL):** Generación de indicadores estructurales (`es_periodo_2`, `ciclo_num`, `es_segundo_ciclo`, `grado_alto`) y conservación categórica de `seccion`.
4. **Análisis Exploratorio (EDA):** Tablas comparativas y 6 visualizaciones científicas por período, ciclo, grado, sección y especialidad.
5. **Modelado de conteos y viabilidad supervisada:** Evaluación de `DummyRegressor` vs. `PoissonRegressor` ($n = 33$) y diseño técnico de **Regresión Logística** y **Random Forest** para Fase II (`docs/viabilidad_ml_supervisado.md`).
6. **Despliegue y gobernanza ética:** Publicación en Colab, Streamlit y GitHub Pages bajo la Ley No. 172-13 y normativas del MINERD.

---

## 📊 7. Datos Utilizados y Resultados Verificados (`2024-2025` vs. `2025-2026`)

### 7.1 Cuadro Resumen Verificado

| Dimensión | Categoría Institucional | Secc. 24-25 | Secc. 25-26 | Aband. 24-25 | Aband. 25-26 | Total Bienio | Variación Conteo | % del Total |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Total Centro** | **Politécnico José Antonio Castillo** | **17** | **16\*** | **9** | **15** | **24** | **+6 (+66.7 %)** | **100.0 %** |
| **Ciclo** | Primer Ciclo (`1.º` a `3.º`) | 8 | 7 | 6 | 10 | **16** | +4 (+66.7 %) | 66.7 % |
| **Ciclo** | Segundo Ciclo Técnico (`4.º` a `6.º`) | 9 | 9 | 3 | 5 | **8** | +2 (+66.7 %) | 33.3 % |
| **Grado** | `1.º` de Secundaria | 4 | 3 | 1 | 6 | **7** | +5 (+500.0 %) | 29.2 % |
| **Grado** | `2.º` de Secundaria | 2 | 2 | 4 | 3 | **7** | -1 (-25.0 %) | 29.2 % |
| **Grado** | `3.º` de Secundaria | 2 | 2 | 1 | 1 | **2** | 0 (0.0 %) | 8.3 % |
| **Grado** | `4.º` de Secundaria | 3 | 3 | 2 | 2 | **4** | 0 (0.0 %) | 16.7 % |
| **Grado** | `5.º` de Secundaria | 3 | 3 | 1 | 3 | **4** | +2 (+200.0 %) | 16.7 % |
| **Grado** | `6.º` de Secundaria | 3 | 3 | 0 | 0 | **0** | 0 (0.0 %) | 0.0 % |
| **Especialidad 2.º Ciclo** | Producción Agropecuaria (`Sección A`) | 3 | 3 | 2 | 4 | **6** | +2 (+100.0 %) | 25.0 % (75 % del 2.º Ciclo) |
| **Especialidad 2.º Ciclo** | Comercio y Mercadeo (`Sección B`) | 3 | 3 | 1 | 0 | **1** | -1 (-100.0 %) | 4.2 % (12.5 % del 2.º Ciclo) |
| **Especialidad 2.º Ciclo** | Gestión Adm. y Tributaria (`Sección C`) | 3 | 3 | 0 | 1 | **1** | +1 (N/A) | 4.2 % (12.5 % del 2.º Ciclo) |

> \* *Nota:* En `2025-2026`, la sección `1.º D` figura como **no reportada (`—`)** en el cuadro institucional verificado; no se le imputa el valor cero.

### 7.2 Hallazgos Principales
1. **Aumento interanual:** El conteo total aumentó de **9 a 15 casos (+66.7 %)** y el promedio por sección reportada subió de **0.5294 a 0.9375 (+77.1 %)**.
2. **Foco crítico en la transición a secundaria:** El **Primer Ciclo** concentra el **66.7 %** de los abandonos ($16$ de $24$), y los grados **`1.º` y `2.º`** acumulan el **58.3 %** ($14$ casos).
3. **Secciones prioritarias de intervención:** `1.º C` ($4$ casos en `2025-2026`), `2.º B` ($4$ casos acumulados: $2$ y $2$), `2.º A` ($3$ casos), `4.º A` ($3$ casos) y `5.º A` ($3$ casos).
4. **Retención total en año de término:** `6.º` de secundaria (`6.º A`, `6.º B`, `6.º C`) mantuvo **0 abandonos** en ambos períodos.

---

## 💻 8. Instrucciones de Instalación y Ejecución Local

### 8.1 Clonar el repositorio e instalar dependencias
```bash
git clone https://github.com/adonamil46/SIAAE-ML-Abandono-Escolar.git
cd SIAAE-ML-Abandono-Escolar
pip install -r requirements.txt
```

### 8.2 Ejecutar la aplicación interactiva en Streamlit
```bash
streamlit run app.py
```

### 8.3 Visualizar la Landing Page (GitHub Pages) localmente
Puedes abrir directamente el archivo `index.html` en cualquier navegador web moderno o levantar un servidor estático local:
```bash
python -m http.server 8000
# Abrir http://localhost:8000 en el navegador
```

---

## 🌐 9. Enlaces Oficiales del Proyecto y Despliegue en GitHub Pages {#enlaces-oficiales-del-proyecto}

- **Repositorio Oficial en GitHub (Rama `main`):**  
  https://github.com/adonamil46/SIAAE-ML-Abandono-Escolar.git
- **Aplicación Oficial en Streamlit Community Cloud:**  
  https://siaae-ml-abandono-escolar-fkdckk6h2ejqtmvhqzq9a6.streamlit.app/
- **Herramienta de Video Referenciada (BRAG):**  
  https://github.com/latent-spaces/brag.git *(producción del video en español programada para el Bloque D)*.

### Cómo activar GitHub Pages para `index.html`
1. En el repositorio de GitHub `adonamil46/SIAAE-ML-Abandono-Escolar`, ir a **Settings** → **Pages**.
2. En **Build and deployment** → **Source**, elegir **Deploy from a branch**.
3. Seleccionar la rama **`main`** y la carpeta **`/ (root)`**, y hacer clic en **Save**.
4. GitHub Pages publicará automáticamente la landing page `index.html` junto con sus recursos en `assets/` y `results/figures/`.

---

## ⚠️ 10. Limitaciones Metodológicas y Recomendaciones

### Limitaciones Declaradas
- **Datos agregados ($n = 33$):** Los registros disponibles corresponden a conteos por sección-año, por lo que no se entrenan modelos predictivos individuales sobre ellos para evitar la falacia ecológica.
- **Denominadores de matrícula ($N_j$) pendientes:** El documento fuente consigna conteos absolutos de abandono sin el total de inscritos por aula, razón por la cual no se inventan tasas porcentuales por sección.

### Recomendaciones Estratégicas para el Centro Educativo
1. **Focalización psicopedagógica inmediata** del Departamento de Orientación y Psicología en `1.º C`, `2.º B`, `2.º A`, `4.º A` y `5.º A`.
2. **Programa de nivelación y acogida** durante el primer bimestre para los estudiantes de nuevo ingreso en `1.º` y `2.º` de secundaria.
3. **Implementación de la Fase II del Sistema de Alerta Temprana (SAT):** Consolidar registros longitudinales anonimizados por estudiante (asistencia del 1.er bimestre, calificaciones parciales P1, sobreedad y matrícula por sección) para entrenar los modelos supervisados de **Regresión Logística** y **Random Forest** diseñados en [`docs/viabilidad_ml_supervisado.md`](docs/viabilidad_ml_supervisado.md).

4. ---

# ENTREGA FINAL DEL PROYECTO — UFHEC 2026

**Proyecto:** Sistema Inteligente de Análisis del Abandono Escolar mediante Machine Learning (SIAAE-ML)

**Autor:** Ing. Adonamil Cruz Evangelista

**Universidad:** Universidad Federico Henríquez y Carvajal (UFHEC)

**Programa:** Maestría en Inteligencia Artificial Aplicada a la Educación y la Tecnología

**Asignatura:** Machine Learning

## Descripción del proyecto

SIAAE-ML es un proyecto académico que analiza el abandono escolar en el Politécnico José Antonio Castillo Ferreiras, Paso de Moca, República Dominicana, durante los períodos escolares 2024-2025 y 2025-2026.

El estudio utiliza 33 observaciones agregadas por sección y período, con 24 casos de abandono verificados, excluyendo los traslados escolares. Integra análisis estadístico, modelado exploratorio de Machine Learning, visualizaciones y herramientas web interactivas.

## Materiales y evidencias de entrega

### 1. Video explicativo del proyecto

[Ver publicación y descargar el video académico](https://github.com/adonamil46/SIAAE-ML-Abandono-Escolar/releases/latest)

### 2. Informe académico final

[Consultar el informe en PDF](docs/Informe_Final_SIAAE_ML_Adonamil_Cruz.pdf)

[Descargar el informe editable en Word](docs/Informe_Final_SIAAE_ML_Adonamil_Cruz.docx)

### 3. Aplicación interactiva Streamlit

[Acceder a la aplicación SIAAE-ML](https://siaae-ml-abandono-escolar-fkdckk6h2ejqtmvhqzq9a6.streamlit.app/)

### 4. Portal web del proyecto

[Visitar el portal científico SIAAE-ML](https://adonamil46.github.io/SIAAE-ML-Abandono-Escolar/)

### 5. Código fuente y cuadernos de investigación

El repositorio contiene los archivos de programación, el código de Streamlit, la documentación metodológica, los cuadernos de trabajo de Machine Learning, los datos agregados autorizados y los gráficos estadísticos.

### 6. Principales resultados

- Período 2024-2025: 9 casos de abandono.
- Período 2025-2026: 15 casos de abandono.
- Total del estudio: 24 casos.
- Primer Ciclo: 16 casos.
- Segundo Ciclo: 8 casos.
- Modelo de Poisson: evaluación exploratoria de conteos agregados, sin realizar predicciones individuales de estudiantes.

## Consideraciones éticas

El proyecto utiliza datos agregados para proteger la privacidad estudiantil. Los traslados escolares no se contabilizan como abandono.

La investigación constituye una base para mejorar el análisis institucional y orientar futuras estrategias de prevención del abandono escolar.

---

**Ing. Adonamil Cruz Evangelista**

**UFHEC — Noviembre de 2026**
