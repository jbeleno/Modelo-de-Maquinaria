"""
Script para entrenar modelo Random Forest de consumo de combustible
Optimizado para Docker - solo genera el modelo sin gráficas ni resultados detallados
Descarga el dataset desde Kaggle usando kagglehub
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os
import kagglehub
import glob

def descargar_dataset():
    """Descarga el dataset desde Kaggle"""
    print("📥 Descargando dataset desde Kaggle...")
    # Download latest version
    path = kagglehub.dataset_download("jessbeleo/datos-maquinaria-consumo")
    print(f"✅ Dataset descargado en: {path}")
    return path

def encontrar_archivo_csv(dataset_path):
    """Encuentra el archivo CSV dentro del dataset descargado"""
    # Buscar archivos CSV en el directorio del dataset
    csv_files = glob.glob(os.path.join(dataset_path, "*.csv"))
    
    if not csv_files:
        # Buscar recursivamente
        csv_files = glob.glob(os.path.join(dataset_path, "**", "*.csv"), recursive=True)
    
    if not csv_files:
        raise FileNotFoundError(f"No se encontró ningún archivo CSV en {dataset_path}")
    
    # Buscar el archivo con el nombre esperado o usar el primero
    for csv_file in csv_files:
        if "datos_maquinaria_consumo" in csv_file.lower() or "maquinaria" in csv_file.lower():
            print(f"✅ Archivo CSV encontrado: {csv_file}")
            return csv_file
    
    # Si no encuentra el específico, usar el primero
    print(f"✅ Usando archivo CSV: {csv_files[0]}")
    return csv_files[0]

def cargar_datos():
    """Carga los datos del CSV con las columnas necesarias"""
    # Descargar dataset
    dataset_path = descargar_dataset()
    
    # Encontrar archivo CSV
    csv_path = encontrar_archivo_csv(dataset_path)
    
    # Columnas necesarias
    cols_usar = [
        'Pnominal(kW)', 'T(°C)', 'Implemento', 'k_base', 'n',
        'Ancho(m)', 'Profundidad(m)', 'Textura', 'Humedad(%)',
        'Velocidad(km/h)', 'Masa_total(kg)', 'Pendiente(%)',
        'Tipo_suelo', 'RPM', 'Duracion(h)', 'Consumo_total(L)'
    ]
    
    # Leer CSV
    df = pd.read_csv(csv_path, encoding='latin1', sep=';', usecols=cols_usar)
    return df

def limpiar_datos(df):
    """Limpia y convierte los datos a tipos numéricos adecuados"""
    df_limpio = df.copy()
    
    # Definir columnas categóricas (texto)
    cols_texto = ['Implemento', 'Textura', 'Tipo_suelo']
    
    # Limpiar comas decimales y espacios
    df_limpio = df_limpio.apply(lambda x: x.str.replace(',', '.').str.strip() if x.dtype == "object" else x)
    
    # Convertir todas las columnas no categóricas a numéricas
    for col in df_limpio.columns:
        if col not in cols_texto:
            df_limpio[col] = pd.to_numeric(df_limpio[col], errors='coerce')
    
    return df_limpio

def codificar_variables(df):
    """Codifica las variables categóricas"""
    # Codificación ordinal para 'Textura'
    mapa_textura = {'arenoso': 1, 'franco': 2, 'arcilla': 3}
    df['Textura'] = df['Textura'].map(mapa_textura)
    
    # One-Hot Encoding para 'Implemento' y 'Tipo_suelo'
    df_encoded = pd.get_dummies(
        df,
        columns=['Implemento', 'Tipo_suelo'],
        drop_first=True  # Evita multicolinealidad
    )
    
    return df_encoded

def entrenar_modelo():
    """Función principal que entrena y guarda el modelo Random Forest"""
    print("🔄 Iniciando proceso de entrenamiento...")
    
    # 1. Cargar datos
    print("📂 Cargando datos...")
    df_entrada = cargar_datos()
    print(f"✅ Datos cargados: {df_entrada.shape[0]} registros")
    
    # 2. Limpiar datos
    print("🧹 Limpiando datos...")
    df_limpio = limpiar_datos(df_entrada)
    
    # 3. Codificar variables
    print("🔧 Codificando variables categóricas...")
    df_encoded = codificar_variables(df_limpio)
    print(f"✅ Variables codificadas: {df_encoded.shape[1]} columnas")
    
    # 4. Preparar variables de entrada y salida
    target = "Consumo_total(L)"
    X = df_encoded.drop(columns=[target])
    y = df_encoded[target]
    
    # 5. División en entrenamiento y prueba
    print("📊 Dividiendo datos en entrenamiento y prueba...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"✅ Conjunto de entrenamiento: {X_train.shape[0]} muestras")
    print(f"✅ Conjunto de prueba: {X_test.shape[0]} muestras")
    
    # 6. Entrenar Random Forest con hiperparámetros optimizados
    print("🌲 Entrenando modelo Random Forest...")
    model = RandomForestRegressor(
        n_estimators=400,
        max_depth=15,
        min_samples_split=10,
        min_samples_leaf=4,
        max_features=None,
        bootstrap=True,
        random_state=42,
        n_jobs=-1
    )
    
    model.fit(X_train, y_train)
    print("✅ Modelo entrenado exitosamente")
    
    # 7. Guardar modelo
    print("💾 Guardando modelo...")
    modelo_path = "random_forest_optimizado.pkl"
    joblib.dump(model, modelo_path)
    print(f"✅ Modelo guardado en: {modelo_path}")
    
    # Información básica del modelo guardado
    file_size = os.path.getsize(modelo_path) / (1024 * 1024)  # MB
    print(f"📦 Tamaño del archivo: {file_size:.2f} MB")
    
    return model

if __name__ == "__main__":
    try:
        modelo = entrenar_modelo()
        print("\n🎉 Proceso completado exitosamente")
        print("📌 Modelo listo para usar en Docker")
    except Exception as e:
        print(f"\n❌ Error durante el entrenamiento: {str(e)}")
        raise

