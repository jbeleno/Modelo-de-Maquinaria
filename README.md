# 🚜 Modelo de Predicción de Consumo de Combustible para Maquinaria Agrícola

## 🎯 Descripción del Proyecto

Este proyecto implementa modelos de machine learning para predecir el consumo de combustible en maquinaria agrícola utilizando un dataset completo de **32,060 muestras** con **16 variables de entrada**. Se evaluaron múltiples algoritmos para encontrar el modelo más preciso y confiable.

## 📊 Dataset

- **Tamaño:** 32,060 muestras
- **Variables de entrada:** 16 características
- **Variable objetivo:** Consumo total de combustible (L)
- **Rango de consumo real:** 1.34 - 455.18 L
- **Consumo promedio real:** 53.53 L

### Variables del Dataset

| Variable | Tipo | Descripción |
|----------|------|-------------|
| Pnominal(kW) | Numérica | Potencia nominal del motor |
| T(°C) | Numérica | Temperatura ambiente |
| Implemento | Categórica | Tipo de implemento agrícola |
| k_base | Numérica | Coeficiente base |
| n | Numérica | Factor de eficiencia |
| Ancho(m) | Numérica | Ancho del implemento |
| Profundidad(m) | Numérica | Profundidad de trabajo |
| Textura | Categórica | Textura del suelo |
| Humedad(%) | Numérica | Humedad del suelo |
| Velocidad(km/h) | Numérica | Velocidad de trabajo |
| Masa_total(kg) | Numérica | Masa total del equipo |
| Pendiente(%) | Numérica | Pendiente del terreno |
| Tipo_suelo | Categórica | Tipo de suelo |
| RPM | Numérica | Revoluciones por minuto |
| Duracion(h) | Numérica | Duración de la operación |

## 🤖 Modelos Implementados

Se evaluaron los siguientes algoritmos de machine learning:

- **Random Forest Regressor**
- **XGBoost Regressor**
- **Gradient Boosting Regressor**
- **Ensemble (Promedio de todos los modelos)**

## 📈 Resultados de Rendimiento

### 🏆 Ranking de Modelos (por Accuracy)

| Posición | Modelo | Accuracy (%) | R² | RMSE (L) | MAE (L) |
|----------|--------|--------------|----|---------|---------| 
| 🥇 **1°** | **Random Forest** | **87.14%** | **0.9017** | **13.91** | **7.16** |
| 🥈 **2°** | **Gradient Boosting** | **83.51%** | **0.8730** | **15.81** | **8.72** |
| 🥉 **3°** | **XGBoost** | **82.86%** | **0.8694** | **16.03** | **8.92** |
| 4° | **Ensemble** | **84.69%** | **0.8849** | **15.05** | **8.18** |

## 📊 Análisis Estadístico Detallado

### 📈 Tabla Comparativa Completa de Rendimiento

| Modelo | R² | RMSE (L) | MAE (L) | Accuracy (%) | Media Predicción (L) | Std Predicción (L) | Min Predicción (L) | Max Predicción (L) |
|--------|----|---------|---------|--------------|---------------------|-------------------|-------------------|-------------------|
| **Random Forest** | **0.9017** | **13.91** | **7.16** | **87.14%** | **53.74** | **40.61** | **3.96** | **305.32** |
| Gradient Boosting | 0.8730 | 15.81 | 8.72 | 83.51% | 53.63 | 40.55 | 4.57 | 363.47 |
| XGBoost | 0.8694 | 16.03 | 8.92 | 82.86% | 53.63 | 40.38 | 4.88 | 357.63 |

### 🥇 Mejor Modelo: Random Forest

**🎯 Rendimiento Superior:**
- **Accuracy: 87.14%** - El más preciso de todos los modelos
- **R²: 0.9017** - Explica el 90.17% de la varianza
- **RMSE: 13.91 L** - Error promedio más bajo
- **MAE: 7.16 L** - Error absoluto más pequeño

**📊 Estadísticas de Predicción:**
- Media de predicción: 53.74 L
- Desviación estándar: 40.61 L
- Rango: 3.96 - 305.32 L

**✅ Precisión por Rangos:**
- 31.60% de predicciones con error ≤ 5%
- 58.55% de predicciones con error ≤ 10%
- 82.50% de predicciones con error ≤ 20%

### 🔗 Análisis del Ensemble (Promedio)

**📊 Rendimiento del Ensemble:**
- **Accuracy: 84.69%** - Mejor que XGBoost pero inferior a Random Forest
- **R²: 0.8849** - Explica el 88.49% de la varianza
- **RMSE: 15.05 L** - Error intermedio
- **MAE: 8.18 L** - Error absoluto moderado

**📈 Características:**
- Media de predicción: 53.67 L
- Desviación estándar: 40.42 L
- Variabilidad entre modelos: 1.61 L (baja variabilidad)

**⚠️ Observación Importante:**
El ensemble no mejoró el rendimiento del mejor modelo individual (Random Forest), lo que indica que Random Forest ya captura muy bien los patrones del dataset.

## 📊 Análisis de Errores

### 🔍 Distribución de Errores Absolutos

| Modelo | Media Error (L) | Std Error (L) | Min Error (L) | Max Error (L) |
|--------|----------------|---------------|---------------|---------------|
| **Random Forest** | **-0.21** | **13.91** | **-123.83** | **166.69** |
| XGBoost | -0.10 | 16.03 | -126.81 | 146.60 |
| Gradient Boosting | -0.10 | 15.81 | -140.02 | 157.93 |
| Ensemble | -0.13 | 15.05 | -127.51 | 152.80 |

### 📈 Distribución de Errores Relativos

| Modelo | Media Error (%) | Std Error (%) | Mediana Error (%) |
|--------|----------------|---------------|-------------------|
| **Random Forest** | **12.86%** | **16.11%** | **8.15%** |
| XGBoost | 17.14% | 21.77% | 11.18% |
| Gradient Boosting | 16.49% | 19.96% | 10.92% |
| Ensemble | 15.31% | 18.73% | 9.95% |

### 📊 Estadísticas de Errores por Cuartiles

| Modelo | Q1 Error (L) | Q2 Error (L) | Q3 Error (L) |
|--------|--------------|--------------|--------------|
| **Random Forest** | **-3.20** | **-0.08** | **2.30** |
| XGBoost | -4.26 | -0.12 | 3.42 |
| Gradient Boosting | -4.17 | -0.03 | 3.26 |
| Ensemble | -3.86 | -0.08 | 2.93 |

## 🎯 Conclusiones y Recomendaciones

### ✅ Fortalezas del Random Forest

1. **Mayor Precisión:** 87.14% de accuracy, significativamente superior a los otros modelos
2. **Menor Error:** RMSE de 13.91 L vs 15-16 L de los otros modelos
3. **Mejor Consistencia:** 82.50% de predicciones con error ≤ 20%
4. **Estabilidad:** Menor variabilidad en los errores

### 📊 Comparación con el Dataset Real

- **Consumo real promedio:** 53.53 L
- **Consumo real std:** 44.37 L
- **Rango real:** 1.34 - 455.18 L

**Observación:** Los modelos predicen correctamente la media (≈53.6 L) pero con menor variabilidad (≈40.4 L vs 44.4 L real), lo que sugiere que los modelos son conservadores en sus predicciones extremas.

### 🎯 Recomendaciones de Uso

#### 🥇 **Para Aplicaciones Críticas:**
- **Usar Random Forest** - Mayor precisión y consistencia
- **Confianza alta** para predicciones dentro del rango de entrenamiento
- **Monitorear** predicciones extremas (>300 L)

#### 🔄 **Para Aplicaciones Generales:**
- **Random Forest** sigue siendo la mejor opción
- **Ensemble** como alternativa si se requiere mayor robustez
- **Validar** predicciones con datos históricos cuando sea posible

#### ⚠️ **Limitaciones Identificadas:**
1. **Sobreestimación conservadora:** Los modelos tienden a ser conservadores
2. **Errores en extremos:** Mayor error en consumos muy altos o muy bajos
3. **Variabilidad reducida:** Predicen con menor variabilidad que la realidad

## 📁 Archivos del Proyecto

### 📊 Datos
- `datos_maquinaria_consumo.csv` - Dataset completo con 32,060 muestras
- `predicciones_completas_detalladas.csv` - Predicciones detalladas de todos los modelos

### 🤖 Modelos Entrenados
- `random_forest_optimizado.pkl` - Mejor modelo (87.14% accuracy)
- `xgboost_optimizado.pkl` - Modelo XGBoost optimizado
- `gradient_boosting_optimizado.pkl` - Modelo Gradient Boosting optimizado

### 📋 Documentación
- `modelos_finales_consumo.ipynb` - Notebook con el código completo
- `evaluacion_completa_modelos.txt` - Resultados detallados de evaluación

## 🚀 Instalación y Uso

### Requisitos del Sistema
- Python 3.7+
- 8GB RAM mínimo recomendado
- 2GB espacio en disco

### Instalación de Dependencias
```bash
pip install -r requirements.txt
```

### Uso del Modelo
```python
import joblib
import pandas as pd

# Cargar el modelo entrenado
modelo = joblib.load('random_forest_optimizado.pkl')

# Preparar datos de entrada (ejemplo)
datos_entrada = pd.DataFrame({
    'Pnominal(kW)': [150],
    'T(°C)': [25],
    'Implemento': ['Arado'],
    'k_base': [1.2],
    'n': [0.8],
    'Ancho(m)': [3.0],
    'Profundidad(m)': [0.3],
    'Textura': ['Media'],
    'Humedad(%)': [15],
    'Velocidad(km/h)': [8],
    'Masa_total(kg)': [2500],
    'Pendiente(%)': [5],
    'Tipo_suelo': ['Arcilloso'],
    'RPM': [1500],
    'Duracion(h)': [4]
})

# Realizar predicción
prediccion = modelo.predict(datos_entrada)
print(f"Consumo predicho: {prediccion[0]:.2f} L")
```

## 📈 Métricas de Calidad del Dataset

- **Tamaño:** 32,060 muestras (excelente para entrenamiento)
- **Variables:** 16 características (buena diversidad)
- **Rango de consumo:** 1.34 - 455.18 L (amplio rango)
- **Distribución:** Media 53.53 L, Std 44.37 L (distribución realista)

## 🔮 Perspectivas Futuras

### 🚀 Mejoras Potenciales:
1. **Recolección de más datos** en rangos extremos
2. **Feature engineering** adicional
3. **Técnicas de ensemble** más sofisticadas
4. **Validación cruzada** temporal si hay dependencia temporal

### 📊 Monitoreo Continuo:
1. **Tracking de accuracy** en producción
2. **Detección de drift** en los datos
3. **Reentrenamiento periódico** con nuevos datos
4. **Validación** con casos reales

---

*📅 Evaluación realizada con dataset completo de 32,060 muestras*  
*🤖 Modelos evaluados: Random Forest, XGBoost, Gradient Boosting, Ensemble*  
*🎯 Mejor modelo: Random Forest con 87.14% de accuracy*
