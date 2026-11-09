# Evaluación de Viabilidad Técnica y Metodológica de Modelos Supervisados (Regresión Logística y Random Forest)
## Sistema Inteligente de Análisis del Abandono Escolar mediante Machine Learning (SIAAE-ML)

- **Institución Universitaria:** Universidad Federico Henríquez y Carvajal (UFHEC)
- **Programa:** Maestría en Inteligencia Artificial Aplicada a la Educación y la Tecnología
- **Asignatura:** Machine Learning
- **Autor:** Ing. Adonamil Cruz Evangelista
- **Centro Objeto de Estudio:** Politécnico José Antonio Castillo Ferreiras (Paso de Moca, República Dominicana)
- **Períodos Evaluados:** `2024-2025` y `2025-2026`

---

## 1. Propósito del Documento

El presente documento técnico establece con rigor metodológico y científico la **viabilidad de implementar modelos supervisados de clasificación binaria** —específicamente **Regresión Logística (Modelo A)** y **Random Forest Classifier (Modelo B)**— para la predicción del abandono escolar en el Politécnico José Antonio Castillo Ferreiras, diferenciando claramente entre:

1. **Lo ejecutado con datos institucionales verificados hoy ($n = 33$ registros agregados sección-año):** Análisis Exploratorio de Datos (EDA) comparativo y modelado exploratorio de conteos a nivel de sección (`DummyRegressor` y `PoissonRegressor`).
2. **Por qué NO deben entrenarse modelos predictivos de abandono individual sobre los 33 registros agregados actuales:** Fundamentos estadísticos y metodológicos que impiden entrenar clasificadores individuales sin microdatos por estudiante.
3. **El protocolo técnico para una Fase II (Sistema de Alerta Temprana Individual):** Especificación exacta de variables, estructura de datos, flujo de validación y gobernanza ética necesarios para entrenar y desplegar **Regresión Logística** y **Random Forest** en producción educativa.

---

## 2. Diagnóstico de la Evidencia Disponible ($n = 33$ Observaciones Sección-Año)

### 2.1 Naturaleza de los Datos Actuales
El registro histórico verificado del Politécnico José Antonio Castillo Ferreiras consta de **$n = 33$ observaciones agregadas** ($17$ secciones en `2024-2025` y $16$ secciones en `2025-2026`), donde cada fila $j \in \{1, \dots, 33\}$ representa una **sección escolar en un año académico** y contiene:
- **Variables explicativas estructurales ($\mathbf{x}_j$):** Año escolar (`anio_escolar`), ciclo educativo (`ciclo`), grado (`grado` $\in \{1,\dots,6\}$), sección (`seccion` $\in \{\text{A, B, C, D}\}$), especialidad técnico-profesional (`especialidad`) e indicadores binarios derivados (`es_periodo_2`, `es_segundo_ciclo`, `grado_alto`).
- **Variable respuesta agregada ($y_j$):** Conteo entero no negativo de estudiantes que abandonaron la sección durante el año escolar ($y_j \in \{0, 1, 2, 4\}$, con $\sum_{j=1}^{33} y_j = 24$).

### 2.2 Razones Metodológicas para NO Entrenar Clasificadores Individuales con los 33 Registros Agregados

Entrenar hoy un clasificador binario de abandono estudiantil individual utilizando únicamente los $33$ registros agregados por sección incurriría en cuatro errores metodológicos graves:

1. **Falacia Ecológica (Ecological Fallacy — Robinson, 1950):**
   Las correlaciones observadas a nivel de grupo o sección (por ejemplo, que el Primer Ciclo concentre el $66.7\%$ de los abandonos o que `1.º C` registre $4$ casos en `2025-2026`) no permiten inferir la probabilidad individual de abandono de un estudiante específico sin conocer sus atributos personales (asistencia, calificaciones, sobreedad, situación sociofamiliar).
2. **Ausencia de la Variable Objetivo Individual ($y_i \in \{0, 1\}$) y de Denominadores de Matrícula ($N_j$):**
   Un clasificador supervisado como Regresión Logística o Random Forest requiere observaciones individuales $i = 1, \dots, M$ donde $y_i = 1$ si el estudiante abandonó (excluyendo traslados) y $y_i = 0$ si permaneció matriculado. El cuadro institucional actual reporta cuántos estudiantes abandonaron por sección ($y_j$), pero no el total de estudiantes matriculados ($N_j$) ni los registros de quienes permanecieron ($y_i = 0$).
3. **Insuficiencia Muestral y Riesgo de Sobreajuste (Overfitting) a Nivel Sección:**
   Si se intentara binarizar las $33$ secciones definiendo arbitrariamente $z_j = \mathbb{I}(y_j \ge 1)$ ($16$ secciones con abandono vs. $17$ sin abandono), el tamaño muestral ($n = 33$) y la regla clásica de *Eventos por Variable* ($\text{EPV} \ge 10$, Peduzzi et al., 1996) limitarían cualquier modelo logístico a a lo sumo $1$ predictor estable. Un árbol o bosque aleatorio sobre $33$ filas memorizaría las combinaciones exactas de $(\text{grado}, \text{sección}, \text{año})$ sin capacidad de generalización real.
4. **Fuga Temporal de Información (Data Leakage) si se Usan Conteos Finales:**
   El conteo de abandonos $y_j$ se conoce al cierre del año escolar. Un verdadero Sistema de Alerta Temprana (SAT) debe predecir el riesgo **antes** de que ocurra la desvinculación, utilizando variables medidas en el primer o segundo trimestre escolar.

---

## 3. Distinción entre Modelado Exploratorio Actual y Modelado Predictivo Futuro

| Dimensión Analítica | Nivel Actual Ejecutado (Bloque A) | Nivel Propuesto para Fase II (Microdatos) |
| :--- | :--- | :--- |
| **Unidad de análisis** | Sección-Año Escolar ($n = 33$ observaciones) | Estudiante-Año Escolar ($M \approx 450\text{–}900$ registros/año) |
| **Tipo de variable objetivo** | Conteo discreto por sección: $y_j \in \{0, 1, 2, 4\}$ | Binaria individual: $y_i \in \{0 = \text{Permanece}, 1 = \text{Abandona}\}$ |
| **Algoritmos apropiados** | `DummyRegressor` (línea base) y `PoissonRegressor` | **Modelo A:** Regresión Logística · **Modelo B:** Random Forest |
| **Propósito institucional** | Identificar grados, ciclos, especialidades y secciones críticas | Detectar tempranamente estudiantes en riesgo para tutoría oportuna |
| **Estado en SIAAE-ML** | **Ejecutado y verificado** con datos reales (`2024-2025` y `2025-2026`) | **Diseñado y documentado** (en espera de microdatos institucionales) |

---

## 4. Especificación Técnica de los Modelos Propuestos (Fase II)

### 4.1 Modelo A: Regresión Logística Binaria (Línea Base Interpretable)

La **Regresión Logística** modela la probabilidad condicional de que el estudiante $i$ abandone el centro educativo dado su vector de características pre-abandono $\mathbf{x}_i = (x_{i1}, x_{i2}, \dots, x_{ip})^\top$:

$$P(y_i = 1 \mid \mathbf{x}_i) = \sigma(\beta_0 + \boldsymbol{\beta}^\top \mathbf{x}_i) = \frac{1}{1 + \exp\left(-\left(\beta_0 + \sum_{k=1}^{p} \beta_k x_{ik}\right)\right)}$$

- **Ventajas para el Politécnico José Antonio Castillo:**
  1. **Interpretabilidad directa mediante *Odds Ratios* ($\text{OR}_k = e^{\beta_k}$):** Permite al equipo de Orientación y Psicología comprender exactamente cuánto se incrementa la razón de probabilidades de abandono por cada punto porcentual de inasistencia o por cada asignatura reprobada.
  2. **Calibración de probabilidades:** Produce probabilidades bien calibradas ($\hat{p}_i \in [0, 1]$) que pueden traducirse en semáforos institucionales de riesgo (*Bajo* $< 0.15$, *Moderado* $0.15\text{–}0.35$, *Alto* $> 0.35$).
  3. **Regularización $L_2$ (Ridge) y ponderación de clases (`class_weight='balanced'`):** Mitiga la colinealidad entre indicadores académicos y compensa el desbalance natural de clases (dado que el abandono suele representar una fracción minoritaria de la matrícula total).

### 4.2 Modelo B: Random Forest Classifier (Ensamble No Lineal)

El clasificador **Random Forest** (Breiman, 2001) construye un ensamble de $B$ árboles de decisión $\{T_b\}_{b=1}^{B}$ entrenados sobre muestras *bootstrap* del conjunto de entrenamiento y subconjuntos aleatorios de variables en cada nodo de partición:

$$\hat{P}_{\text{RF}}(y_i = 1 \mid \mathbf{x}_i) = \frac{1}{B} \sum_{b=1}^{B} \hat{P}_{T_b}(y_i = 1 \mid \mathbf{x}_i)$$

- **Ventajas complementarias frente a la Regresión Logística:**
  1. **Captura de interacciones no lineales y umbrales complejos:** Detecta patrones compuestos sin necesidad de especificarlos manualmente (por ejemplo: *estudiante de Primer Ciclo (`1.º` o `2.º`) + asistencia en el primer bimestre $< 82\%$ + sobreedad $\ge 2$ años*).
  2. **Robustez ante valores atípicos y escalas mixtas:** Maneja simultáneamente variables continuas (porcentaje de asistencia, promedio de calificaciones) y categóricas (sección, especialidad técnica, tanda/transporte).
  3. **Importancia de variables (Gini / Permutación y valores SHAP):** Permite jerarquizar cuáles factores institucionales tienen mayor poder predictivo real.

---

## 5. Requerimientos de Datos Adicionales para Entrenar Ambos Modelos

Para pasar del análisis agregado actual ($n = 33$) al entrenamiento válido de **Regresión Logística** y **Random Forest**, el Politécnico José Antonio Castillo Ferreiras debe consolidar una matriz anonimizada de datos longitudinales con los siguientes cinco bloques de información:

| Bloque de Datos | Variables Requeridas (Medición Pre-Abandono: Primer Bimestre / Trimestre) | Tipo de Dato | Justificación Predictiva |
| :--- | :--- | :--- | :--- |
| **1. Identificación Anonimizada y Contexto Estructural** | `id_estudiante_hash` (SHA-256), `anio_escolar`, `ciclo`, `grado`, `seccion`, `especialidad`, `matricula_seccion` ($N_j$) | Categórico / Entero | Permite vincular el contexto de las 33 secciones actuales con el denominador real de matrícula y calcular tasas exactas. |
| **2. Trayectoria e Historial Escolar** | `edad_ingreso`, `sobreedad_anios` (diferencia respecto a la edad teórica del grado), `repitente_previo` ($0/1$), `cambio_centro_reciente` ($0/1$) | Numérico / Binario | La sobreedad y la repitencia previa son predictores estructurales clásicos de desvinculación en el Primer Ciclo. |
| **3. Indicadores Tempranos de Asistencia** | `pct_asistencia_mes1`, `pct_asistencia_mes2`, `ausencias_injustificadas_bim1`, `tardanzas_acumuladas_bim1` | Continuo / Conteo | El ausentismo temprano antecede casi invariablemente al abandono definitivo y es accionable por Orientación Escolar. |
| **4. Desempeño Académico Parcial** | `promedio_calificaciones_p1` (escala 0–100), `asignaturas_reprobadas_p1` ($< 70$ pts), `variacion_promedio` | Continuo / Conteo | Captura el rezago pedagógico inicial, especialmente en la transición a `1.º` y `2.º` de secundaria y en talleres técnicos de `4.º` y `5.º`. |
| **5. Acompañamiento Psicopedagógico y Estado Final Verificado** | `alertas_orientacion_bim1`, `participacion_familia`, `estado_final_anio` (`Promovido`, `Aplazado`, `Traslado`, `Abandono`), `variable_objetivo_abandono` ($0/1$) | Binario / Categórico | Garantiza que los **traslados** se excluyan o codifiquen adecuadamente y define sin ambigüedad la etiqueta supervisada $y_i \in \{0, 1\}$. |

---

## 6. Protocolo de Validación y Métricas para la Fase II

Dado que el abandono escolar a nivel individual es un evento minoritario (clase desbalanceada), el protocolo de evaluación cuando se disponga de los microdatos **no deberá basarse en la exactitud global (*Accuracy*)**, sino en:

1. **Partición Temporal y Estratificada:**
   - Entrenar con las cohortes históricas (`2024-2025` y `2025-2026`) mediante validación cruzada estratificada (`StratifiedKFold(n_splits=5)`) y evaluar prospectivamente sobre la cohorte entrante.
2. **Métricas Principales de Desempeño:**
   - **Recall (Sensibilidad) de la clase positiva ($y_i = 1$):** Prioridad institucional número uno, pues un *Falso Negativo* significa un estudiante en riesgo real de abandono que no recibe apoyo psicopedagógico.
   - **PR-AUC (Área bajo la curva Precisión-Recall):** Métrica óptima ante desbalance de clases.
   - **F1-Score y F2-Score:** Ponderando mayor peso a la sensibilidad ($F_2$) para priorizar la detección temprana.
   - **ROC-AUC y Curva de Calibración (Brier Score):** Para verificar que las probabilidades estimadas reflejen el riesgo empírico real.

---

## 7. Gobernanza Ética, Privacidad y Uso Pedagógico Responsable

1. **Protección de Datos de Menores de Edad:** Todo procesamiento debe cumplir con la **Ley No. 172-13** sobre Protección de Datos Personales de la República Dominicana y las normativas del **MINERD**, reemplazando nombres, números de acta o RNE (Registro Nacional de Estudiantes) por identificadores pseudonimizados antes de cualquier ingesta en Python/Colab.
2. **Principio de No Estigmatización:** Las probabilidades generadas por Regresión Logística o Random Forest **nunca deben utilizarse para excluir, sancionar o etiquetar negativamente al estudiantado**, sino exclusivamente para activar protocolos preventivos de tutoría académica, orientación psicológica y vinculación familiar.
3. **Supervisión Humana en el Bucle (*Human-in-the-Loop*):** El sistema SIAAE-ML actúa como herramienta de apoyo a la decisión del Equipo de Gestión y del Departamento de Orientación y Psicología del Politécnico José Antonio Castillo Ferreiras, quienes conservan siempre el criterio pedagógico final.
