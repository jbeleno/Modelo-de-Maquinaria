# Entrenamiento de Modelo Random Forest

Script optimizado para Docker que entrena un modelo Random Forest para predecir consumo de combustible de maquinaria agrícola.

## Características

- ✅ Solo entrena Random Forest (modelo más eficiente)
- ✅ Sin gráficas ni outputs detallados
- ✅ Genera solo el archivo `.pkl` del modelo
- ✅ Optimizado para Docker
- ✅ Descarga automática del dataset desde Kaggle
- ✅ **El modelo se genera automáticamente durante el BUILD de Docker**

## Requisitos

- Python 3.10+
- pandas
- numpy
- scikit-learn
- joblib
- kagglehub

## Dataset

El script descarga automáticamente el dataset desde Kaggle:
- Dataset: `jessbeleo/datos-maquinaria-consumo`
- Se descarga usando `kagglehub` (no requiere credenciales de Kaggle API)

## Uso Local

```bash
pip install -r requirements.txt
python entrenar_modelo_rf.py
```

## Uso con Docker

### Construir imagen (el modelo se genera durante el build)
```bash
docker build -t entrenar-modelo-rf .
```

**Nota:** Durante el build, el script descargará el dataset, entrenará el modelo y lo guardará dentro de la imagen Docker.

### Ejecutar contenedor
```bash
docker run -v $(pwd):/app/output entrenar-modelo-rf
```

El modelo ya entrenado se copiará como `random_forest_optimizado.pkl` en el directorio actual.

## Estructura de Archivos

- `entrenar_modelo_rf.py`: Script principal de entrenamiento
- `requirements.txt`: Dependencias Python
- `Dockerfile`: Configuración Docker
- `README_ENTRENAMIENTO.md`: Este archivo

## Output

El script genera:
- `random_forest_optimizado.pkl`: Modelo entrenado listo para usar

## Notas

- **El modelo se genera durante el BUILD de Docker**, no durante la ejecución del contenedor
- El dataset se descarga automáticamente durante el build
- No es necesario tener el archivo CSV localmente
- El dataset se cachea localmente por kagglehub para ejecuciones futuras
- Cada vez que construyas la imagen Docker, se generará un nuevo modelo con los datos más recientes de Kaggle

