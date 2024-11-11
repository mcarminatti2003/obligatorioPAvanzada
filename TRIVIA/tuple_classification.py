from typing import Dict, Tuple, Generator, List, Any
import pandas as pd

def leer_dataframe_generador(df: pd.DataFrame) -> Generator[Tuple[str, Any], None, None]:
    """
    Generador que itera sobre las filas del DataFrame y devuelve tuplas con categoría y valor.
    df (pd.DataFrame): El DataFrame a iterar.
    Tuple[str, Any]: Una tupla con la categoría y el valor de cada fila.
    """
    for _, row in df.iterrows():
        yield (row['Category'], row['Value'])

def clasificar_tuplas(tuplas: Generator[Tuple[str, Any], None, None], diccionario_categorias: Dict[str, List[Any]]):
    """
    Clasifica una secuencia de tuplas en un diccionario de categorías.
    tuplas (Generator[Tuple[str, Any], None, None]): Un generador de tuplas donde cada tupla contiene una categoría y un valor.
    diccionario_categorias (Dict[str, List[Any]]): Un diccionario donde las claves son categorías y los valores son listas de valores, el diccionario se actualiza agregando los valores a la categoría correspondiente. Si la categoría no existe, se añade bajo la clave 'POTPOURRI'.
    """
    for categoria, valor in tuplas:
        if categoria not in diccionario_categorias:
            diccionario_categorias.setdefault('POTPOURRI', []).append(valor)
        else:
            diccionario_categorias[categoria].append(valor)
