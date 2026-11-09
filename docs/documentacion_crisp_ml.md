# Documentación Científica Integral bajo Metodología CRISP-ML(Q)
## Sistema Inteligente de Análisis del Abandono Escolar mediante Machine Learning (SIAAE-ML)

- **Universidad:** Universidad Federico Henríquez y Carvajal (UFHEC)
- **Programa:** Maestría en Inteligencia Artificial Aplicada a la Educación y la Tecnología
- **Asignatura:** Machine Learning
- **Autor:** Ing. Adonamil Cruz Evangelista
- **Centro Objeto del Estudio:** Politécnico José Antonio Castillo Ferreiras (Paso de Moca, Provincia Espaillat, República Dominicana — Distrito Educativo 06-06)
- **Períodos Académicos Analizados:** `2024-2025` y `2025-2026`
- **Estándar Metodológico:** CRISP-ML(Q) (*Cross-Industry Standard Process for the Development of Machine Learning Applications with Quality Assurance*, Studer et al., 2021)

---

## Resumen de Arquitectura y Decisiones Metodológicas (ADRs)

| ID Decisión | Título de la Decisión Arquitectónica / Metodológica | Estado | Justificación Científica |
| :--- | :--- | :---: | :--- |
| **ADR-001** | Unidad de análisis verificada: Sección-Año Escolar ($n = 33$) | Aprobado | La fuente oficial verificada consigna conteos por sección ($17$ en `2024-2025` y $16$ en `2025-2026`), sumando $24$ abandonos comprobados. |
| **ADR-002** | Exclusión estricta de los traslados escolares | Aprobado | Un traslado con continuidad lectiva en otro plantel no constituye desvinculación del sistema educativo. |
| **ADR-003** | No invención de denominadores de matrícula ($N_j$) ni tasas ficticias | Aprobado | Al no figurar la matrícula inscrita por sección en el documento fuente, las comparaciones se expresan en conteos absolutos y promedios por sección reportada. |
| **ADR-004** | Separación entre modelado de conteos por sección y clasificación individual | Aprobado | Previene la **falacia ecológica** (Robinson, 1950) y el sobreajuste (*overfitting*). No se entrenan Regresión Logística ni Random Forest individuales sobre 33 filas agregadas. |

---

## Fase 1: Comprensión del Problema Educativo e Institucional (*Business & Educational Problem Understanding*)

### 1.1 Contexto del Centro Educativo
El **Politécnico José Antonio Castillo Ferreiras**, ubicado en Paso de Moca (Distrito Educativo 06-06, Regional 06 La Vega, República Dominicana), imparte educación secundaria estructurada en dos ciclos:
1. **Primer Ciclo (Nivel Secundario General):** Grados `1.º`, `2.º` y `3.º` de secundaria, orientados a la formación general básica y la adaptación del estudiantado procedente del Nivel Primario.
2. **Segundo Ciclo (Modalidad Técnico-Profesional):** Grados `4.º`, `5.º` y `6.º` de secundaria, organizados en tres especialidades técnicas definidas por la letra de la sección:
   - **Sección A:** Producción Agropecuaria.
   - **Sección B:** Comercio y Mercadeo.
   - **Sección C:** Gestión Administrativa y Tributaria.

### 1.2 Formulación del Problema
Durante el bienio `2024-2025` y `2025-2026`, el centro registró **24 casos verificados de abandono escolar**, pasando de **9 abandonos** en `2024-2025` a **15 abandonos** en `2025-2026` (+6 casos, +66.7 % en el conteo absoluto). La dirección académica y el Departamento de Orientación y Psicología requieren:
1. Identificar con exactitud estadística en qué ciclos, grados, secciones y especialidades técnicas se concentra el fenómeno.
2. Establecer las bases técnicas y de captura de datos para evolucionar desde el diagnóstico descriptivo por sección hacia un **Sistema de Alerta Temprana (SAT)** individualizado basado en Machine Learning.

---

## Fase 2: Comprensión y Auditoría de los Datos (*Data Understanding*)

### 2.1 Fuentes Documentales Primarias
El estudio utiliza exclusivamente las fuentes originales resguardadas en `Archivos_proyecto/`:
- `SIAAE_ML_Abandono_Verificado.docx`: Documento institucional con el cuadro oficial de abandonos verificados por sección y año escolar.
- `Proyecto__ML_SIAAE.ipynb`: Cuaderno computacional base con la estructura tabular de las 33 observaciones.
- `Material_1_Proyecto_ML_UFHEC .docx`: Guía académica oficial de la asignatura Machine Learning en UFHEC.

### 2.2 Resultados de la Auditoría de Calidad de Datos
- **Volumen exacto:** $n = 33$ observaciones sección-año ($17$ secciones en `2024-2025` y $16$ secciones en `2025-2026`).
- **Completitud de las 33 filas:** $100\%$ en las variables estructurales y en la variable objetivo de conteo (`abandonos`).
- **Caso estructural documentado (`1.º D` en `2025-2026`):** En `2024-2025` funcionaron cuatro secciones de primer grado (`1.º A`, `1.º B`, `1.º C`, `1.º D`), registrándose $1$ abandono en `1.º D`. En `2025-2026`, la sección `1.º D` figura como **no reportada (`—`)** en el cuadro institucional. Por rigor metodológico, no se incluye como fila numérica ni se le imputa el valor cero.
- **Homologación terminológica:** Se unificó la denominación oficial completa **«Gestión Administrativa y Tributaria»** para las secciones `C` del Segundo Ciclo (`4.º C`, `5.º C`, `6.º C`).

---

## Fase 3: Preparación de los Datos e Ingeniería de Características (*Data Preparation / ETL*)

A partir de los registros verificados (`data/raw/abandono_institucional_verificado.csv`), el flujo ETL genera el conjunto procesado `data/processed/abandono_agregado_siaae.csv` bajo el estándar RFC 4180 (codificación UTF-8 y entrecomillado estricto) con las siguientes transformaciones deterministas:

1. **Identificación y clave primaria compuesta:** `id_observacion` $\in \{1, \dots, 33\}$ y clave única $(\text{anio\_escolar}, \text{grado}, \text{seccion})$ con $0$ duplicados.
2. **Etiqueta compuesta de aula (`grupo`):** Concatenación legible de grado ordinal y sección (`1.º A` hasta `6.º C`).
3. **Indicador temporal binario (`es_periodo_2`):**
   $$\text{es\_periodo\_2}_j = \begin{cases} 0 & \text{si } \text{anio\_escolar}_j = \text{«2024-2025»} \\ 1 & \text{si } \text{anio\_escolar}_j = \text{«2025-2026»} \end{cases}$$
4. **Codificación estructural de ciclo (`ciclo_num`, `es_segundo_ciclo`, `grado_alto`):**
   - $\text{ciclo\_num}_j \in \{1, 2\}$.
   - $\text{es\_segundo\_ciclo}_j = \mathbb{I}(\text{grado}_j \ge 4) \in \{0, 1\}$.
   - $\text{grado\_alto}_j = \mathbb{I}(\text{grado}_j \ge 4) \in \{0, 1\}$.
5. **Preservación categórica de `seccion`:** Las letras `A`, `B`, `C` y `D` se conservan estrictamente como variables categóricas nominales, sin convertirlas en números arbitrarios.

---

## Fase 4: Análisis Exploratorio de Datos (EDA) Comparativo

### 4.1 Síntesis Estadística por Período, Ciclo, Grado y Especialidad

| Dimensión Analítica | Categoría | Secc. 24-25 | Secc. 25-26 | Aband. 24-25 | Aband. 25-26 | Total Bienio | Promedio Global ($\bar{x}$) | % del Total (24) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Global** | Total Politécnico J.A. Castillo | 17 | 16 | 9 | 15 | **24** | 0.7273 | 100.0 % |
| **Ciclo** | Primer Ciclo (`1.º` a `3.º`) | 8 | 7 | 6 | 10 | **16** | 1.0667 | 66.7 % |
| **Ciclo** | Segundo Ciclo (`4.º` a `6.º`) | 9 | 9 | 3 | 5 | **8** | 0.4444 | 33.3 % |
| **Grado** | `1.º` de Secundaria | 4 | 3 | 1 | 6 | **7** | 1.0000 | 29.2 % |
| **Grado** | `2.º` de Secundaria | 2 | 2 | 4 | 3 | **7** | 1.7500 | 29.2 % |
| **Grado** | `3.º` de Secundaria | 2 | 2 | 1 | 1 | **2** | 0.5000 | 8.3 % |
| **Grado** | `4.º` de Secundaria | 3 | 3 | 2 | 2 | **4** | 0.6667 | 16.7 % |
| **Grado** | `5.º` de Secundaria | 3 | 3 | 1 | 3 | **4** | 0.6667 | 16.7 % |
| **Grado** | `6.º` de Secundaria | 3 | 3 | 0 | 0 | **0** | 0.0000 | 0.0 % |
| **Especialidad 2.º Ciclo** | Producción Agropecuaria (`A`) | 3 | 3 | 2 | 4 | **6** | 1.0000 | 25.0 % (75 % del 2.º Ciclo) |
| **Especialidad 2.º Ciclo** | Comercio y Mercadeo (`B`) | 3 | 3 | 1 | 0 | **1** | 0.1667 | 4.2 % (12.5 % del 2.º Ciclo) |
| **Especialidad 2.º Ciclo** | Gestión Adm. y Tributaria (`C`) | 3 | 3 | 0 | 1 | **1** | 0.1667 | 4.2 % (12.5 % del 2.º Ciclo) |

### 4.2 Propiedades Distributivas del Conteo ($y_j$)
- **Frecuencias observadas:** $0$ casos en $17$ secciones ($51.52\%$), $1$ caso en $10$ secciones ($30.30\%$), $2$ casos en $5$ secciones ($15.15\%$), $3$ casos en $0$ secciones ($0.00\%$) y $4$ casos en $1$ sección (`1.º C` en `2025-2026`, $3.03\%$).
- **Media y dispersión:** Media muestral $\bar{y} = 0.7273$, desviación estándar muestral $s = 0.9445$, varianza $s^2 = 0.8920$ e índice de dispersión $s^2 / \bar{y} = 1.2265$ (asimetría positiva con concentración en el Primer Ciclo).

---

## Fase 5: Viabilidad y Diseño del Aprendizaje Supervisado (*Modeling & Feasibility*)

### 5.1 Diferencia Fundamental entre Analizar Conteos Agregados y Predecir el Abandono Individual

Uno de los aportes metodológicos centrales del proyecto **SIAAE-ML** es establecer con claridad la frontera matemática y epistemológica entre dos niveles de modelado:

1. **Nivel Agregado de Sección (Ejecutado en SIAAE-ML con $n = 33$):**
   - **Unidad:** Sección escolar $j$ en el período lectivo $t$.
   - **Variable respuesta:** Conteo discreto $y_j \in \{0, 1, 2, \dots\}$.
   - **Modelo estadístico:** Regresión de Poisson con enlace logarítmico:
     $$\ln(\hat{\lambda}_j) = \beta_0 + \beta_1 (\text{es\_periodo\_2}_j) + \beta_2 (\text{ciclo\_num}_j) + \beta_3 (\text{grado}_j) + \beta_4 (\text{es\_segundo\_ciclo}_j) + \beta_5 (\text{grado\_alto}_j)$$
   - **Alcance:** Permite estimar el número esperado de abandonos por aula según su nivel curricular, pero **no** predice qué estudiante específico abandonará.

2. **Nivel Individual de Estudiante (Diseñado para Fase II con Microdatos):**
   - **Unidad:** Estudiante $i$ matriculado en el centro ($i = 1, \dots, M$).
   - **Variable respuesta:** Indicador binario individual $y_i \in \{0 = \text{Permanece}, 1 = \text{Abandona}\}$.
   - **Modelos supervisados objetivo:**
     - **Modelo A — Regresión Logística Binaria:** $P(y_i = 1 \mid \mathbf{x}_i) = \frac{1}{1 + \exp(-(\beta_0 + \boldsymbol{\beta}^\top \mathbf{x}_i))}$. Ofrece interpretabilidad directa mediante *Odds Ratios* ($\text{OR}_k = e^{\beta_k}$).
     - **Modelo B — Random Forest Classifier:** $\hat{P}_{\text{RF}}(y_i = 1 \mid \mathbf{x}_i) = \frac{1}{B}\sum_{b=1}^{B} \hat{P}_{T_b}(\mathbf{x}_i)$. Captura interacciones no lineales complejas entre grado, asistencia temprana, calificaciones parciales y sobreedad.
   - **Por qué no se entrenan hoy sobre $n = 33$:** Carecer de los registros de quienes permanecieron ($y_i = 0$), de los denominadores de matrícula ($N_j$) y de predictores individuales pre-abandono produciría **falacia ecológica**, **fuga temporal de datos** y **sobreajuste extremo**.

---

## Fase 6: Evaluación (*Evaluation*)

### 6.1 Evaluación del Modelado Exploratorio de Conteos ($n = 33$)
Utilizando validación cruzada agrupada por período escolar (`LeaveOneGroupOut` sobre `anio_escolar`):
- **`DummyRegressor(strategy='mean')`:** $\text{MAE} = 0.7804$, $\text{RMSE} = 0.9950$.
- **`PoissonRegressor(alpha=1.0)`:** $\text{MAE} = 0.7574$ ($-2.95\%$ de error absoluto medio respecto a la línea base), $\text{RMSE} = 0.9952$.
- **Coeficientes de Poisson sobre las 33 secciones:** Intercepto $= +0.309708$; `es_periodo_2` $= +0.091631$; `grado` $= -0.186514$; `ciclo_num` $= -0.031281$. Confirma cuantitativamente que el conteo esperado disminuye a medida que el estudiante avanza de `1.º` a `6.º` grado.

### 6.2 Protocolo de Evaluación para Clasificadores Individuales (Fase II)
Cuando el centro integre la matriz de microdatos individuales, la evaluación de **Regresión Logística** y **Random Forest** se regirá por:
- **Validación:** `StratifiedKFold(n_splits=5)` y validación temporal inter-cohorte.
- **Métricas primarias:** **Sensibilidad (*Recall*) de la clase positiva ($y_i = 1$)** para minimizar falsos negativos (estudiantes en riesgo no detectados), **PR-AUC** (área bajo la curva Precisión-Recall), **F2-Score** y **Brier Score** (calibración de probabilidades).

---

## Fase 7: Implementación y Despliegue (*Deployment*)

El sistema **SIAAE-ML** se ha implementado en una arquitectura de triple capa reproducible:
1. **Capa Computacional (`Proyecto_ML_SIAAE_Colab.ipynb`):** Cuaderno Jupyter estructurado y compatible con Google Colab para reproducir la auditoría, el EDA, los gráficos y el modelado de conteos.
2. **Capa Aplicativa en la Nube (`app.py` + `requirements.txt`):** Aplicación interactiva desplegada en **Streamlit Community Cloud** con filtros dinámicos, gráficos Plotly y laboratorio pedagógico de Machine Learning.
3. **Capa de Difusión Científica (`index.html` + `assets/css/styles.css` + `assets/js/main.js`):** Portal web académico responsive preparado para **GitHub Pages**.

---

## Fase 8: Monitoreo, Privacidad y Mantenimiento (*Monitoring, Privacy & Maintenance*)

1. **Privacidad y Protección de Datos Personales:** Cumplimiento estricto de la **Ley No. 172-13** de la República Dominicana y los reglamentos del **MINERD**. Ningún archivo del repositorio ni de las aplicaciones públicas contiene nombres, cédulas, RNE ni datos identificables de menores de edad.
2. **Monitoreo de Deriva de Datos (*Data & Concept Drift*):** Como demuestra el cambio observado entre `2024-2025` (foco en `2.º` con 4 casos) y `2025-2026` (foco en `1.º C` con 4 casos), la distribución del abandono varía entre cohortes. El sistema debe actualizarse al cierre de cada período lectivo y tras cada corte bimestral.
3. **Uso Pedagógico No Estigmatizante (*Human-in-the-Loop*):** Las salidas analíticas tienen carácter exclusivamente preventivo para guiar tutorías y apoyo sociofamiliar por parte del Departamento de Orientación y Psicología.

---

## Fase 9: Limitaciones Metodológicas Declaradas

1. **Granularidad agregada de la evidencia actual ($n = 33$):** Impide estimar efectos causales individuales hasta contar con registros por estudiante.
2. **Ausencia de matrícula por sección ($N_j$) en el cuadro fuente:** Obliga a trabajar con conteos absolutos y promedios por sección reportada, evitando fabricar porcentajes de tasa de abandono sin denominador oficial.
3. **Sección `1.º D` no reportada en `2025-2026`:** Se documenta de forma transparente como dato estructural no reportado (`—`), sin imputarle valores arbitrarios.
4. **Serie histórica corta (2 períodos académicos):** No permite extrapolaciones de series de tiempo de largo plazo, aunque sí comparaciones interanuales rigurosas por ciclo, grado, sección y especialidad.
