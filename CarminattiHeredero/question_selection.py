import pandas as pd
from typing import Dict, List
from itertools import chain

def seleccionar_pregunta(df: pd.DataFrame) -> pd.Series:
    """
    Selecciona y muestra 5 preguntas aleatorias de un DataFrame.
    Permite al usuario seleccionar una pregunta mediante un número.
    df (pd.DataFrame): El DataFrame que contiene las preguntas y respuestas.
    pd.Series: La fila del DataFrame que corresponde a la pregunta seleccionada por el usuario.
    """
    # Seleccionar 5 preguntas aleatorias del DataFrame
    preguntas = df.sample(5).reset_index(drop=True)
    
    # Mostrar las preguntas disponibles
    print("\nSeleccione la pregunta que desea responder:")
    for i, pregunta in enumerate(preguntas['Question'], 1):
        print(f"{i}. {pregunta}")
    
    # Solicitar al usuario seleccionar una pregunta
    selected = int(input("Seleccione el número de la pregunta (1-5): "))
    while not 1 <= selected <= 5:
        selected = int(input("Selección inválida. Seleccione un número del 1 al 5: "))
    
    # Devolver la fila del DataFrame correspondiente a la pregunta seleccionada
    pregunta = preguntas.iloc[selected - 1]
    return pregunta

def seleccionar_respuestas_incorrectas(df: pd.DataFrame, categoria: str) -> pd.DataFrame:
    """
    Selecciona 2 respuestas incorrectas de una categoría específica.
    df (pd.DataFrame): El DataFrame que contiene las respuestas y categorías.
    categoria (str): La categoría de la cual seleccionar las respuestas incorrectas.
    pd.DataFrame: Un DataFrame que contiene 2 respuestas incorrectas de la categoría especificada.
    """
    # Seleccionar 2 respuestas incorrectas de la categoría proporcionada
    respuestas_incorrectas = df[df['Category'] == categoria].sample(2)
    return respuestas_incorrectas

def mostrar_opciones(respuestas_incorrectas: pd.DataFrame, pregunta: pd.Series) -> List[str]:
    """
    Muestra opciones de respuestas combinando respuestas incorrectas con la correcta.
    respuestas_incorrectas (pd.DataFrame): DataFrame con respuestas incorrectas.
    pregunta (pd.Series): La pregunta correcta y su respuesta.
    List[str]: Una lista con las opciones de respuesta, incluyendo la correcta y las incorrectas.
    """
    # Combinar respuestas incorrectas con la respuesta correcta
    opciones = list(chain(respuestas_incorrectas['Answer'], [pregunta['Answer']]))
    return opciones
