# Dockerfile para entrenar modelo Random Forest
FROM python:3.10-slim

WORKDIR /app

# Copiar requirements
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar script (el dataset se descarga automáticamente desde Kaggle)
COPY entrenar_modelo_rf.py .

# Crear directorio de salida
RUN mkdir -p /app/output

# Entrenar modelo durante el BUILD (no durante la ejecución)
# El modelo se genera y guarda en la imagen durante la construcción
RUN python entrenar_modelo_rf.py && \
    cp random_forest_optimizado.pkl /app/output/ && \
    echo "✅ Modelo generado durante el build"

# Comando por defecto: copiar el modelo ya entrenado al directorio de salida
# (el modelo ya existe en la imagen desde el build)
CMD cp random_forest_optimizado.pkl /app/output/ && \
    echo "📦 Modelo disponible en /app/output/random_forest_optimizado.pkl" && \
    tail -f /dev/null

