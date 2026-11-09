# Reporte de Análisis Exploratorio de Datos (EDA) Comparativo
## Sistema Inteligente de Análisis del Abandono Escolar mediante Machine Learning (SIAAE-ML)

- **Centro Educativo:** Politécnico José Antonio Castillo Ferreiras (Paso de Moca, Provincia Espaillat, República Dominicana — Distrito Educativo 06-06)
- **Programa Académico:** Maestría en Inteligencia Artificial Aplicada a la Educación y la Tecnología — Universidad Federico Henríquez y Carvajal (UFHEC)
- **Asignatura:** Machine Learning
- **Autor:** Ing. Adonamil Cruz Evangelista
- **Períodos Analizados:** `2024-2025` y `2025-2026`
- **Unidad de Observación:** Sección-Año Escolar ($n = 33$ registros agregados verificados; $24$ abandonos acumulados)
- **Criterio Institucional:** Los traslados escolares **no** se contabilizan como abandono escolar.

---

## 1. Resumen Ejecutivo de Auditoría de Datos

Antes de realizar el procesamiento estadístico, se efectuó una auditoría cruzada fila por fila entre el documento institucional verificado (`Archivos_proyecto/SIAAE_ML_Abandono_Verificado.docx`) y el cuaderno computacional base (`Archivos_proyecto/Proyecto__ML_SIAAE.ipynb`).

- **Coincidencia de registros:** 100 % de exactitud en los **33 registros sección-año** y los **24 casos de abandono escolar** ($9$ en `2024-2025` y $15$ en `2025-2026`).
- **Estandarización documental:** En el Segundo Ciclo Técnico-Profesional, la sección `C` fue normalizada con su denominación oficial completa del documento institucional: **«Gestión Administrativa y Tributaria»** (en el cuaderno original figuraba abreviada como «Gestión Administrativa»).
- **Nota metodológica sobre tasas porcentuales:** El registro institucional consigna conteos absolutos de abandono por sección, sin incluir la matrícula total inscrita por sección. Por rigor científico, todas las comparaciones se expresan como **conteos absolutos**, **promedios de casos por sección reportada** y **variación relativa del conteo**, sin fabricar tasas porcentuales sobre denominadores inexistentes.

---

## 2. Comparativa General por Período Académico (`2024-2025` vs. `2025-2026`)

| Período Escolar | Secciones Reportadas ($n$) | Total de Abandonos | Promedio por Sección ($\bar{x}$) | Mediana | Desviación Estándar ($s$) | Mínimo | Máximo | Secciones con 0 Casos | Secciones con $\ge 1$ Caso |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **2024-2025** | 17 | 9 | 0.5294 | 0.0000 | 0.7174 | 0 | 2 | 10 (58.8 %) | 7 (41.2 %) |
| **2025-2026** | 16* | 15 | 0.9375 | 0.5000 | 1.1236 | 0 | 4 | 7 (43.8 %) | 9 (56.3 %) |
| **Total / Global** | **33** | **24** | **0.7273** | **0.0000** | **0.9445** | **0** | **4** | **17 (51.5 %)** | **16 (48.5 %)** |

> \* **Nota sobre `1.º D`:** En el período `2024-2025` se reportaron 4 secciones en Primer Grado (`1.º A`, `1.º B`, `1.º C`, `1.º D`), mientras que en `2025-2026` la sección `1.º D` figura como **no reportada (`—`)** en el cuadro institucional verificado.

### Hallazgos Clave por Período
1. **Incremento interanual del conteo:** El número absoluto de abandonos pasó de **9 casos** en `2024-2025` a **15 casos** en `2025-2026`, lo que representa una diferencia de **+6 abandonos** (**+66.7 %** en el conteo absoluto).
2. **Aumento en la densidad por sección:** Aun con una sección menos reportada en `2025-2026` ($16$ vs. $17$), el promedio de abandonos por sección aumentó de **0.5294** a **0.9375** (**+77.1 %**).
3. **Mayor dispersión en el segundo período:** La desviación estándar pasó de $0.7174$ a $1.1236$, impulsada principalmente por el pico atípico observado en la sección `1.º C` durante `2025-2026` ($4$ casos).

---

## 3. Análisis Comparativo por Ciclo Educativo

El sistema educativo secundario analizado comprende dos ciclos:
- **Primer Ciclo (Nivel Secundario General):** Grados `1.º`, `2.º` y `3.º`.
- **Segundo Ciclo (Modalidad Técnico-Profesional):** Grados `4.º`, `5.º` y `6.º`.

| Ciclo Educativo | Secciones 2024-2025 | Abandonos 2024-2025 | Promedio 2024-2025 | Secciones 2025-2026 | Abandonos 2025-2026 | Promedio 2025-2026 | Total Abandonos | % del Total (24) | Variación Conteo |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Primer Ciclo (1.º a 3.º)** | 8 | 6 | 0.7500 | 7 | 10 | 1.4286 | **16** | **66.7 %** | +4 (+66.7 %) |
| **Segundo Ciclo (4.º a 6.º)** | 9 | 3 | 0.3333 | 9 | 5 | 0.5556 | **8** | **33.3 %** | +2 (+66.7 %) |
| **Total Institucional** | **17** | **9** | **0.5294** | **16** | **15** | **0.9375** | **24** | **100.0 %** | **+6 (+66.7 %)** |

### Interpretación por Ciclo
- **Concentración en el Primer Ciclo:** Dos terceras partes de todo el abandono institucional (**16 de 24 casos, 66.7 %**) ocurren en el Primer Ciclo, pese a contar con menos secciones totales ($15$ secciones-año frente a $18$ del Segundo Ciclo).
- **Transición crítica al nivel secundario:** El promedio global del Primer Ciclo es de **1.0667 abandonos por sección**, más del doble del registrado en el Segundo Ciclo (**0.4444 abandonos por sección**).

---

## 4. Análisis Comparativo por Grado Escolar (`1.º` a `6.º`)

| Grado | Ciclo | Secc. 24-25 | Aband. 24-25 | Prom. 24-25 | Secc. 25-26 | Aband. 25-26 | Prom. 25-26 | Total Abandonos | % del Total | Diferencia Interanual |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1.º** | Primer Ciclo | 4 | 1 | 0.2500 | 3 | 6 | 2.0000 | **7** | 29.2 % | +5 (+500.0 %) |
| **2.º** | Primer Ciclo | 2 | 4 | 2.0000 | 2 | 3 | 1.5000 | **7** | 29.2 % | -1 (-25.0 %) |
| **3.º** | Primer Ciclo | 2 | 1 | 0.5000 | 2 | 1 | 0.5000 | **2** | 8.3 % | 0 (0.0 %) |
| **4.º** | Segundo Ciclo | 3 | 2 | 0.6667 | 3 | 2 | 0.6667 | **4** | 16.7 % | 0 (0.0 %) |
| **5.º** | Segundo Ciclo | 3 | 1 | 0.3333 | 3 | 3 | 1.0000 | **4** | 16.7 % | +2 (+200.0 %) |
| **6.º** | Segundo Ciclo | 3 | 0 | 0.0000 | 3 | 0 | 0.0000 | **0** | 0.0 % | 0 (0.0 %) |
| **Total** | **Ambos Ciclos** | **17** | **9** | **0.5294** | **16** | **15** | **0.9375** | **24** | **100.0 %** | **+6 (+66.7 %)** |

### Hallazgos por Grado
1. **`1.º` y `2.º` de Secundaria concentran el 58.3 % del abandono total** ($7 + 7 = 14$ casos de $24$).
2. **Cambio de foco en Primer Ciclo:** En `2024-2025`, el grado con mayor afectación fue `2.º` ($4$ casos, promedio $2.00$), mientras que en `2025-2026` el foco principal se desplazó hacia `1.º` ($6$ casos en $3$ secciones, promedio $2.00$).
3. **Incremento en `5.º` de Secundaria:** En el Segundo Ciclo, `5.º` triplicó su conteo interanual al pasar de $1$ caso en `2024-2025` a $3$ casos en `2025-2026`.
4. **Retención total en `6.º` de Secundaria:** Ninguna de las secciones de término (`6.º A`, `6.º B`, `6.º C`) registró abandonos en los dos períodos evaluados ($0$ casos en $6$ observaciones sección-año).

---

## 5. Análisis por Especialidad Técnico-Profesional (Segundo Ciclo: `4.º` a `6.º`)

En el Segundo Ciclo, la letra de sección identifica el área técnica del Politécnico José Antonio Castillo Ferreiras:
- **Sección A:** Producción Agropecuaria
- **Sección B:** Comercio y Mercadeo
- **Sección C:** Gestión Administrativa y Tributaria

| Especialidad Técnico-Profesional | Secc. 24-25 | Aband. 24-25 | Prom. 24-25 | Secc. 25-26 | Aband. 25-26 | Prom. 25-26 | Total 2.º Ciclo | % dentro del 2.º Ciclo (8) | % del Total Institucional (24) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Producción Agropecuaria (A)** | 3 | 2 | 0.6667 | 3 | 4 | 1.3333 | **6** | **75.0 %** | 25.0 % |
| **Comercio y Mercadeo (B)** | 3 | 1 | 0.3333 | 3 | 0 | 0.0000 | **1** | **12.5 %** | 4.2 % |
| **Gestión Administrativa y Tributaria (C)** | 3 | 0 | 0.0000 | 3 | 1 | 0.3333 | **1** | **12.5 %** | 4.2 % |
| **Subtotal Segundo Ciclo** | **9** | **3** | **0.3333** | **9** | **5** | **0.5556** | **8** | **100.0 %** | **33.3 %** |

### Interpretación Técnico-Profesional
- **Producción Agropecuaria (`4.º A`, `5.º A`, `6.º A`)** concentra el **75.0 %** de todos los abandonos del Segundo Ciclo ($6$ de $8$ casos), duplicando su incidencia de $2$ casos en `2024-2025` a $4$ casos en `2025-2026` (`4.º A` con $2$ casos y `5.º A` con $2$ casos).
- **Comercio y Mercadeo (`B`)** y **Gestión Administrativa y Tributaria (`C`)** muestran una incidencia muy baja ($1$ caso acumulado cada una en el bienio).

---

## 6. Detalle Completo por Sección-Grado (Matriz Comparativa de 33 Registros)

| Grupo | Ciclo | Grado | Sección | Especialidad / Nivel | Abandonos 2024-2025 | Abandonos 2025-2026 | Total Bienio | Variación Interanual |
| :---: | :--- | :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| **1.º A** | Primer Ciclo | 1 | A | Nivel Secundario General (1.er Ciclo) | 0 | 1 | 1 | +1 |
| **1.º B** | Primer Ciclo | 1 | B | Nivel Secundario General (1.er Ciclo) | 0 | 1 | 1 | +1 |
| **1.º C** | Primer Ciclo | 1 | C | Nivel Secundario General (1.er Ciclo) | 0 | 4 | 4 | +4 |
| **1.º D** | Primer Ciclo | 1 | D | Nivel Secundario General (1.er Ciclo) | 1 | — (No reportada) | 1 | N/A |
| **2.º A** | Primer Ciclo | 2 | A | Nivel Secundario General (1.er Ciclo) | 2 | 1 | 3 | -1 |
| **2.º B** | Primer Ciclo | 2 | B | Nivel Secundario General (1.er Ciclo) | 2 | 2 | 4 | 0 |
| **3.º A** | Primer Ciclo | 3 | A | Nivel Secundario General (1.er Ciclo) | 1 | 1 | 2 | 0 |
| **3.º B** | Primer Ciclo | 3 | B | Nivel Secundario General (1.er Ciclo) | 0 | 0 | 0 | 0 |
| **4.º A** | Segundo Ciclo | 4 | A | Producción Agropecuaria | 1 | 2 | 3 | +1 |
| **4.º B** | Segundo Ciclo | 4 | B | Comercio y Mercadeo | 1 | 0 | 1 | -1 |
| **4.º C** | Segundo Ciclo | 4 | C | Gestión Administrativa y Tributaria | 0 | 0 | 0 | 0 |
| **5.º A** | Segundo Ciclo | 5 | A | Producción Agropecuaria | 1 | 2 | 3 | +1 |
| **5.º B** | Segundo Ciclo | 5 | B | Comercio y Mercadeo | 0 | 0 | 0 | 0 |
| **5.º C** | Segundo Ciclo | 5 | C | Gestión Administrativa y Tributaria | 0 | 1 | 1 | +1 |
| **6.º A** | Segundo Ciclo | 6 | A | Producción Agropecuaria | 0 | 0 | 0 | 0 |
| **6.º B** | Segundo Ciclo | 6 | B | Comercio y Mercadeo | 0 | 0 | 0 | 0 |
| **6.º C** | Segundo Ciclo | 6 | C | Gestión Administrativa y Tributaria | 0 | 0 | 0 | 0 |
| **TOTAL** | — | — | — | **33 observaciones sección-año** | **9** | **15** | **24** | **+6 (+66.7 %)** |

### Secciones Prioritarias de Intervención Psicopedagógica
1. **`1.º C`** ($4$ casos acumulados, todos en `2025-2026`): Representa el valor máximo registrado en una sola sección durante el bienio.
2. **`2.º B`** ($4$ casos acumulados: $2$ en `2024-2025` y $2$ en `2025-2026`): Presenta persistencia alta en ambos períodos.
3. **`2.º A`**, **`4.º A`** y **`5.º A`** ($3$ casos acumulados cada una): Muestran recurrencia sistemática en ambos años escolares, destacando el eje agropecuario (`4.º A` y `5.º A`).

---

## 7. Distribución Estadística de Conteos por Sección ($n = 33$)

| Conteo de Abandonos ($y$) | Frecuencia de Secciones ($f_i$) | Porcentaje de Secciones (%) | Abandonos Aportados ($y \cdot f_i$) | % del Total de Abandonos |
| :---: | :---: | :---: | :---: | :---: |
| **0 abandonos** | 17 | 51.52 % | 0 | 0.00 % |
| **1 abandono** | 10 | 30.30 % | 10 | 41.67 % |
| **2 abandonos** | 5 | 15.15 % | 10 | 41.67 % |
| **3 abandonos** | 0 | 0.00 % | 0 | 0.00 % |
| **4 abandonos** | 1 | 3.03 % | 4 | 16.67 % |
| **Total** | **33** | **100.00 %** | **24** | **100.00 %** |

- **Asimetría positiva y concentración:** Más de la mitad de las secciones-año ($51.52\%$) no presentan abandonos ($y = 0$), mientras que las $6$ secciones-año con $2$ o más casos ($18.18\%$ de las observaciones) concentran el **58.33 %** de todos los abandonos ($14$ de $24$ casos).
- **Relación varianza-media:** La media muestral es $\bar{y} = 0.7273$ y la varianza muestral es $s^2 = 0.8920$ ($\text{razón } s^2 / \bar{y} = 1.2265$), comportamiento típico de una variable de conteo discreta con ligera sobredispersión.

---

## 8. Síntesis de Modelos Exploratorios de Conteo (Nivel Sección)

En el cuaderno computacional base se contrastó una línea base ingenua (`DummyRegressor`) frente a un modelo lineal generalizado de conteo (`PoissonRegressor`, $\alpha = 1.0$) utilizando validación cruzada por grupos (`LeaveOneGroupOut` por `anio_escolar`):

| Modelo Exploratorio de Conteo | Estrategia de Validación | MAE Promedio | RMSE Promedio | Interpretación Metodológica |
| :--- | :--- | :---: | :---: | :--- |
| **`DummyRegressor(strategy='mean')`** | `LeaveOneGroupOut` (`anio_escolar`) | 0.7804 | 0.9950 | Línea base ingenua (predice la media del año de entrenamiento). |
| **`PoissonRegressor(alpha=1.0)`** | `LeaveOneGroupOut` (`anio_escolar`) | 0.7574 | 0.9952 | Reducción marginal en MAE (-2.95 %), con RMSE prácticamente idéntico. |

- **Parámetros ajustados sobre los 33 registros (`PoissonRegressor`):**
  - Intercepto ($\beta_0$): `0.309708`
  - `es_periodo_2` ($\beta_1$): `+0.091631` (asociación positiva con el período `2025-2026`)
  - `grado` ($\beta_3$): `-0.186514` (asociación inversa: a mayor grado escolar, menor conteo esperado de abandono)
  - `ciclo_num`, `es_segundo_ciclo`, `grado_alto`: `-0.031281` cada uno (reducción del conteo esperado en el Segundo Ciclo y grados superiores).

> **Conclusión analítica:** Estos modelos operan **exclusivamente sobre conteos agregados por sección** ($n = 33$) con fines descriptivos y exploratorios. Para conocer la evaluación técnica sobre modelos predictivos individuales (**Regresión Logística** y **Random Forest**), consúltese el documento [`docs/viabilidad_ml_supervisado.md`](../../docs/viabilidad_ml_supervisado.md).
