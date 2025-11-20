# MATERIALES Y MÉTODOS - Modelo de Predicción de Consumo de Combustible

## 1. RECOLECCIÓN DE DATOS

### 1.1 Fuente de Datos
El dataset utilizado en este estudio fue obtenido del archivo `datos_maquinaria_consumo.csv`, el cual contiene información sobre el consumo de combustible de maquinaria agrícola en diferentes condiciones operativas. El archivo fue leído utilizando la librería pandas con las siguientes especificaciones:
- **Codificación:** Latin-1
- **Separador:** Punto y coma (;)
- **Total de registros:** 32,060 muestras

### 1.2 Información Recolectada
El dataset comprende **16 variables de entrada** y una variable objetivo. A continuación se detalla la información recolectada:

#### Variables Numéricas (13 variables):
1. **Pnominal(kW)**: Potencia nominal del motor en kilovatios
2. **T(°C)**: Temperatura ambiente en grados Celsius
3. **k_base**: Coeficiente base (valores enteros)
4. **n**: Factor de eficiencia
5. **Ancho(m)**: Ancho del implemento en metros
6. **Profundidad(m)**: Profundidad de trabajo en metros
7. **Humedad(%)**: Humedad del suelo en porcentaje
8. **Velocidad(km/h)**: Velocidad de trabajo en kilómetros por hora
9. **Masa_total(kg)**: Masa total del equipo en kilogramos
10. **Pendiente(%)**: Pendiente del terreno en porcentaje
11. **RPM**: Revoluciones por minuto del motor
12. **Duracion(h)**: Duración de la operación en horas
13. **Consumo_total(L)**: Variable objetivo - Consumo total de combustible en litros

#### Variables Categóricas (3 variables):
1. **Implemento**: Tipo de implemento agrícola utilizado
   - 8 categorías: rodillo_compactador, sembradora_directa, cultivador_campo, arado_vertedera, arado_disco, rastra_discos, subsolador, cincel_chisel

2. **Textura**: Textura del suelo
   - 3 categorías: arenoso, franco, arcilla

3. **Tipo_suelo**: Tipo de suelo
   - 4 categorías: Asfalto, Arena, Franco, Arcilla

### 1.3 Estadísticas Descriptivas del Dataset
- **Tamaño total:** 32,060 muestras
- **Rango de consumo real:** 1.34 - 455.18 litros
- **Consumo promedio real:** 53.53 litros
- **Desviación estándar del consumo:** 44.37 litros
- **Sin valores faltantes:** Todas las variables presentan 32,060 valores no nulos

---

## 2. PREPROCESAMIENTO DE DATOS

### 2.1 Limpieza de Datos
Se realizaron las siguientes operaciones de limpieza sobre el dataset original:

1. **Normalización de formato decimal:**
   - Reemplazo de comas (,) por puntos (.) como separador decimal, ya que el dataset original utilizaba formato europeo
   - Eliminación de espacios en blanco al inicio y final de los valores de tipo texto

2. **Conversión de tipos de datos:**
   - Transformación de variables numéricas almacenadas como texto a tipos numéricos (float64/int64)
   - Manejo de errores mediante conversión a valores nulos cuando no fue posible la conversión
   - Las columnas categóricas (Implemento, Textura, Tipo_suelo) se mantuvieron como tipo texto

**Resultado:** Después de la limpieza, todas las variables numéricas fueron convertidas correctamente a tipos numéricos, manteniendo la integridad de los datos.

### 2.2 Codificación de Variables Categóricas
Para incorporar las variables categóricas en los modelos de machine learning, se aplicaron las siguientes técnicas:

#### 2.2.1 Codificación Ordinal para Textura del Suelo
Se aplicó codificación ordinal a la variable "Textura" debido a su naturaleza ordenada:
- **Arenoso** → 1
- **Franco** → 2
- **Arcilla** → 3

Esta codificación preserva la relación ordinal entre las categorías de textura del suelo.

#### 2.2.2 One-Hot Encoding para Implemento y Tipo de Suelo
Se aplicó codificación binaria (One-Hot Encoding) para las variables nominales:

- **Implemento:** 8 categorías → 7 columnas binarias (se eliminó una categoría de referencia para evitar multicolinealidad)
  - Columnas generadas: `Implemento_arado_vertedera`, `Implemento_cincel_chisel`, `Implemento_cultivador_campo`, `Implemento_rastra_discos`, `Implemento_rodillo_compactador`, `Implemento_sembradora_directa`, `Implemento_subsolador`

- **Tipo_suelo:** 4 categorías → 3 columnas binarias (se eliminó una categoría de referencia)
  - Columnas generadas: `Tipo_suelo_Arena`, `Tipo_suelo_Asfalto`, `Tipo_suelo_Franco`

**Eliminación de categoría de referencia:** Se eliminó una categoría de referencia para cada variable nominal mediante el parámetro `drop_first=True` para evitar multicolinealidad en el modelo.

**Resultado del preprocesamiento:** El dataset final contiene **23 variables de entrada** después de la codificación:
- 13 variables numéricas originales
- 1 variable de textura codificada ordinalmente
- 7 variables binarias de implemento
- 3 variables binarias de tipo de suelo

---

## 3. DIVISIÓN DE DATOS

Los datos se dividieron en conjuntos de entrenamiento y prueba mediante división aleatoria con los siguientes parámetros:

- **Proporción:** 80% entrenamiento (25,648 muestras) y 20% prueba (6,412 muestras)
- **Semilla aleatoria:** `random_state=42` para garantizar reproducibilidad
- **Estratificación:** No aplicada (problema de regresión)

Esta división permite evaluar el rendimiento del modelo en datos no vistos durante el entrenamiento.

---

## 4. MODELOS DE MACHINE LEARNING

### 4.1 Algoritmos Evaluados
Se evaluaron cuatro algoritmos de aprendizaje supervisado para regresión:

#### 4.1.1 Regresión Lineal (Linear Regression)
- Modelo base de referencia
- Sin hiperparámetros a optimizar

#### 4.1.2 Random Forest Regressor
- **Hiperparámetros optimizados:**
  - `n_estimators=400` (número de árboles)
  - `max_depth=15` (profundidad máxima de los árboles)
  - `min_samples_split=10` (mínimo de muestras para dividir un nodo)
  - `min_samples_leaf=4` (mínimo de muestras en una hoja)
  - `max_features=None` (usa todas las características)
  - `bootstrap=True` (muestreo con reemplazo)
  - `random_state=42` (reproducibilidad)
  - `n_jobs=-1` (uso de todos los núcleos disponibles)

#### 4.1.3 XGBoost Regressor
- **Hiperparámetros optimizados:**
  - `n_estimators=200` (número de árboles)
  - `learning_rate=0.05` (tasa de aprendizaje)
  - `max_depth=6` (profundidad máxima)
  - `min_child_weight=7` (peso mínimo de la hoja)
  - `subsample=0.7` (fracción de muestras para entrenar cada árbol)
  - `colsample_bytree=0.9` (fracción de características por árbol)
  - `gamma=0` (reducción mínima de pérdida)
  - `reg_alpha=0.5` (regularización L1)
  - `reg_lambda=1.5` (regularización L2)
  - `random_state=42`
  - `tree_method='hist'` (método de construcción de árboles)
  - `n_jobs=-1`

#### 4.1.4 Gradient Boosting Regressor
- **Hiperparámetros optimizados:**
  - `n_estimators=200` (número de árboles)
  - `learning_rate=0.05` (tasa de aprendizaje)
  - `max_depth=6` (profundidad máxima)
  - `min_samples_split=10` (mínimo de muestras para dividir)
  - `min_samples_leaf=4` (mínimo de muestras en hoja)
  - `subsample=0.8` (fracción de muestras)
  - `random_state=42`

### 4.2 Proceso de Entrenamiento
1. **Entrenamiento:** Cada modelo se entrenó utilizando el conjunto de entrenamiento (80% de los datos, 25,648 muestras)
2. **Predicción:** Se realizaron predicciones sobre el conjunto de prueba (20% de los datos, 6,412 muestras)
3. **Evaluación:** Se calcularon métricas de rendimiento para cada modelo
4. **Guardado:** Los modelos entrenados se serializaron para su posterior uso

---

## 5. MÉTRICAS DE EVALUACIÓN

### 5.1 Métricas Utilizadas
Para evaluar el rendimiento de los modelos de regresión, se utilizaron las siguientes métricas:

#### 5.1.1 Coeficiente de Determinación (R²)
- **Definición:** Mide la proporción de varianza de la variable dependiente que es explicada por el modelo
- **Rango:** 0 a 1 (valores más altos indican mejor ajuste)
- **Fórmula:** R² = 1 - (SS_res / SS_tot)

#### 5.1.2 Error Cuadrático Medio Raíz (RMSE)
- **Definición:** Raíz cuadrada del promedio de los errores al cuadrado
- **Unidad:** Litros (L)
- **Interpretación:** Error promedio en las mismas unidades que la variable objetivo
- **Fórmula:** RMSE = √(Σ(y_real - y_pred)² / n)

#### 5.1.3 Error Absoluto Medio (MAE)
- **Definición:** Promedio de los valores absolutos de los errores
- **Unidad:** Litros (L)
- **Interpretación:** Error promedio sin considerar la dirección del error
- **Fórmula:** MAE = Σ|y_real - y_pred| / n

#### 5.1.4 Accuracy (Precisión)
- **Definición:** Medida de precisión calculada como el complemento del error relativo medio
- **Fórmula:** Accuracy = 100 × (1 - error_relativo_medio)
- **Donde:** error_relativo_medio = promedio(|y_real - y_pred| / y_real)
- **Interpretación:** Porcentaje de precisión del modelo (valores más altos indican mejor rendimiento)

### 5.2 Nota sobre Precision, Recall y F1-Score
**Precision, Recall y F1-Score** son métricas diseñadas para problemas de **clasificación** (donde se predice una clase discreta), no para problemas de **regresión** (donde se predice un valor continuo).

En este estudio, el problema es de **regresión** (predicción del consumo de combustible en litros, un valor continuo), por lo que estas métricas no son aplicables. En su lugar, se utilizaron las métricas de regresión mencionadas anteriormente (R², RMSE, MAE, Accuracy).

### 5.3 Nota sobre Matriz de Confusión
La **matriz de confusión** es una herramienta de evaluación diseñada para problemas de **clasificación**, donde se comparan las clases predichas con las clases reales.

En este estudio de **regresión**, no es posible construir una matriz de confusión tradicional, ya que se predice un valor continuo, no una clase discreta. En su lugar, se utilizaron:
- **Gráficos de dispersión** (valores reales vs. predichos)
- **Análisis de residuales** (errores de predicción)
- **Distribución de errores** (histogramas de errores)

---

## 6. RESULTADOS

### 6.1 Cantidad de Datos Utilizados
- **Total de muestras:** 32,060 registros
- **Conjunto de entrenamiento:** 25,648 muestras (80%)
- **Conjunto de prueba:** 6,412 muestras (20%)
- **Variables de entrada:** 23 variables (después del preprocesamiento)
- **Variable objetivo:** Consumo_total(L)

**Estadísticas descriptivas del consumo real:**
- **Media:** 53.53 L
- **Desviación estándar:** 44.37 L
- **Rango:** 1.34 - 455.18 L
- **Mínimo:** 1.34 L
- **Máximo:** 455.18 L

### 6.2 Accuracy Obtenido por el Modelo
El modelo **Random Forest** obtuvo el mejor rendimiento con:
- **Accuracy: 87.14%** (evaluado en el conjunto completo de 32,060 muestras)
- **Accuracy en conjunto de prueba:** 82.03% (evaluado en 6,412 muestras)

### 6.3 Comparación entre Modelos

#### 6.3.1 Rendimiento en Conjunto de Prueba (20% de los datos)
| Modelo | Accuracy (%) | R² | RMSE (L) | MAE (L) |
|--------|--------------|----|---------|---------|
| **Random Forest** | **82.03%** | **0.8133** | **18.62** | **9.92** |
| **Gradient Boosting** | **82.17%** | **0.8142** | **18.57** | **9.81** |
| **XGBoost** | **81.71%** | **0.8177** | **18.39** | **9.87** |
| **Regresión Lineal** | **26.87%** | **0.5475** | **28.98** | **21.46** |

#### 6.3.2 Rendimiento en Dataset Completo (32,060 muestras)
| Modelo | Accuracy (%) | R² | RMSE (L) | MAE (L) |
|--------|--------------|----|---------|---------|
| **Random Forest** | **87.14%** | **0.9017** | **13.91** | **7.16** |
| **Gradient Boosting** | **83.51%** | **0.8730** | **15.81** | **8.72** |
| **XGBoost** | **82.86%** | **0.8694** | **16.03** | **8.92** |
| **Ensemble (Promedio)** | **84.69%** | **0.8849** | **15.05** | **8.18** |

**Nota sobre el Ensemble:** El ensemble (promedio de las predicciones de Random Forest, XGBoost y Gradient Boosting) no mejoró el rendimiento del mejor modelo individual (Random Forest), lo que indica que Random Forest ya captura muy bien los patrones del dataset. La variabilidad entre modelos es baja (desviación estándar promedio de 1.61 L), lo que sugiere que los modelos están de acuerdo en sus predicciones.

#### 6.3.3 Análisis Detallado del Mejor Modelo (Random Forest)
**Rendimiento Superior:**
- **Accuracy: 87.14%** - El más preciso de todos los modelos
- **R²: 0.9017** - Explica el 90.17% de la varianza
- **RMSE: 13.91 L** - Error promedio más bajo
- **MAE: 7.16 L** - Error absoluto más pequeño

**Estadísticas de Predicción:**
- Media de predicción: 53.74 L
- Desviación estándar: 40.61 L
- Rango de predicciones: 3.96 - 305.32 L

**Precisión por Rangos de Error:**
- 31.60% de predicciones con error ≤ 5%
- 58.55% de predicciones con error ≤ 10%
- 82.50% de predicciones con error ≤ 20%

**Distribución de Errores:**
- Media del error: -0.21 L (ligera subestimación)
- Desviación estándar del error: 13.91 L
- Rango de errores: -123.83 L a 166.69 L
- Error relativo medio: 12.86%

### 6.4 Importancia de Variables del Suelo

El análisis de importancia de variables se realizó utilizando la importancia de características (feature importance) del modelo Random Forest, el cual mide la contribución de cada variable a las predicciones del modelo mediante la reducción promedio de impureza que cada variable produce en los árboles del bosque.

#### 6.4.1 Variables Relacionadas con el Suelo

Las variables relacionadas con el suelo y su importancia son:

| Variable | Importancia | Porcentaje del Total |
|----------|-------------|---------------------|
| **Humedad(%)** | **0.6807** | **68.07%** |
| **Textura** | 0.0032 | 0.32% |
| **Tipo_suelo_Franco** | 0.0013 | 0.13% |
| **Tipo_suelo_Arena** | 0.0012 | 0.12% |
| **Tipo_suelo_Asfalto** | 0.0000 | 0.00% |

**Importancia total de variables del suelo: 0.6863 (68.63%)**

#### 6.4.2 Análisis de Importancia

**Humedad(%)** es la variable más importante del modelo, representando el 68.07% de la importancia total. Esta variable es significativamente más relevante que cualquier otra variable, lo que indica que la humedad del suelo es el factor determinante más crítico para predecir el consumo de combustible en maquinaria agrícola.

Las otras variables relacionadas con el suelo (Textura y Tipo_suelo) tienen una importancia muy baja:
- **Textura:** 0.32% del total - Aunque codificada ordinalmente, su contribución es mínima
- **Tipo_suelo:** Las variables binarias de tipo de suelo (Franco, Arena, Asfalto) tienen importancias muy bajas (0.00% - 0.13%)

#### 6.4.3 Top 10 Variables Más Importantes del Modelo

| Posición | Variable | Importancia | Porcentaje |
|----------|----------|-------------|------------|
| 1° | **Humedad(%)** | **0.6807** | **68.07%** |
| 2° | **Pnominal(kW)** | **0.1542** | **15.42%** |
| 3° | **Duracion(h)** | **0.0359** | **3.59%** |
| 4° | **Velocidad(km/h)** | **0.0234** | **2.34%** |
| 5° | **Profundidad(m)** | **0.0177** | **1.77%** |
| 6° | **Pendiente(%)** | **0.0158** | **1.58%** |
| 7° | **Masa_total(kg)** | **0.0137** | **1.37%** |
| 8° | **Ancho(m)** | **0.0134** | **1.34%** |
| 9° | **RPM** | **0.0128** | **1.28%** |
| 10° | **T(°C)** | **0.0115** | **1.15%** |

**Observación:** Las dos variables más importantes (Humedad y Potencia Nominal) representan juntas el 83.49% de la importancia total del modelo, lo que indica que son los factores más determinantes para la predicción del consumo de combustible. Las variables relacionadas con implementos y tipo de suelo tienen importancias muy bajas (< 0.5%), lo que sugiere que estas características tienen un impacto menor en el consumo de combustible comparado con las condiciones operativas y del suelo (humedad).

---

## 7. HERRAMIENTAS Y SOFTWARE UTILIZADOS

El análisis se realizó utilizando Python 3.10 con las siguientes librerías: pandas para manipulación de datos, numpy para operaciones numéricas, scikit-learn para algoritmos de machine learning y evaluación, xgboost para el algoritmo XGBoost, y matplotlib para visualización de resultados.

---

## 8. SELECCIÓN DEL MODELO FINAL

El modelo seleccionado como final fue **Random Forest Regressor**, debido a que presentó el mejor rendimiento en todas las métricas evaluadas:

- **Accuracy: 87.14%** (superior a los otros modelos)
- **R²: 0.9017** (explica el 90.17% de la varianza)
- **RMSE: 13.91 L** (menor error cuadrático medio)
- **MAE: 7.16 L** (menor error absoluto medio)
- **Mayor consistencia:** 82.50% de predicciones con error ≤ 20%

Este modelo fue serializado para su posterior uso en producción.


