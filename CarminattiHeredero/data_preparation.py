import pandas as pd
from typing import Dict, List

def cargar_datos(ruta_csv: str) -> pd.DataFrame:
    """
    Carga el csv
    ruta_csv (str): La ruta al archivo CSV a cargar.
       pd.DataFrame: El DataFrame que contiene los datos del CSV
    """
    df = pd.read_csv(ruta_csv, encoding='latin1')
    return df

def filtrar_categorias_frecuentes(df: pd.DataFrame, min_count: int = 2) -> pd.DataFrame:
    """
    Filtra categorías que aparecen más de un número mínimo de veces df
    min_count (int): El número mínimo de apariciones para que una categoría sea incluida
    pd.DataFrame: Un DataFrame que contiene solo las categorías que aparecen más de `min_count` veces
    """
    # Contar las apariciones de cada categoría
    categoria_counts = df['Category'].value_counts()
    
    # Obtener las categorías que aparecen más de min_count veces
    categorias_frecuentes = categoria_counts[categoria_counts > min_count].index
    
    # Filtrar el DataFrame para incluir solo las categorías frecuentes
    df_frecuente = df[df['Category'].isin(categorias_frecuentes)]
    return df_frecuente

def crear_diccionario_categorias(df_frecuente: pd.DataFrame) -> Dict[str, List]:
    """
    Crea un diccionario con categorías y listas vacías basado el df
    df_frecuente (pd.DataFrame): El DataFrame que contiene las categorías filtradas
    Dict[str, List]: Un diccionario donde las claves son las categorías y los valores son listas vacías
    """
    # Obtener los valores únicos de la columna 'Category'
    valores_distintos = df_frecuente['Category'].unique()
    
    # Crear un diccionario con categorías y listas vacías
    diccionario_categorias = {categoria: [] for categoria in valores_distintos}
    return diccionario_categorias
