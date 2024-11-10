import pandas as pd
import random
import time
from itertools import chain
from functools import reduce
from data_preparation import cargar_datos, filtrar_categorias_frecuentes, crear_diccionario_categorias
from question_selection import seleccionar_pregunta, seleccionar_respuestas_incorrectas, mostrar_opciones
from tuple_classification import leer_dataframe_generador, clasificar_tuplas
from monada import Monda, print_monda
from typing import Tuple, List, Generator

def cronometro(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print_monda(f"Tiempo transcurrido: {fin - inicio} segundos")
        return resultado
    return wrapper

def generar_preguntas(df_frecuente: pd.DataFrame) -> Generator[Tuple[pd.Series, List[str]], None, None]:
    while True:
        pregunta = seleccionar_pregunta(df_frecuente)
        respuestas_incorrectas = seleccionar_respuestas_incorrectas(df_frecuente, pregunta['Category'])
        opciones = mostrar_opciones(respuestas_incorrectas, pregunta)
        yield pregunta, opciones

@cronometro
def iniciar_juego(df_frecuente: pd.DataFrame) -> int:
    puntajes = [0] * 5  # Lista inicializada con ceros para almacenar puntajes de cada pregunta
    generador = generar_preguntas(df_frecuente)
    
    for i in range(5):  # Hacer exactamente 5 preguntas
        pregunta, opciones = next(generador)
        random.shuffle(opciones)
        print_monda(f"\nPregunta {i + 1}: {pregunta['Question']}")
        for idx, respuesta in enumerate(opciones, 1):
            print_monda(f"{idx}. {respuesta}")
        
        while True:
            try:
                respuesta_seleccionada = int(input("Seleccione su respuesta (1-3): "))
                if 1 <= respuesta_seleccionada <= len(opciones):
                    break
                else:
                    print_monda(f"Selección inválida. Seleccione un número del 1 al {len(opciones)}.")
            except ValueError:
                print_monda("Entrada no válida. Por favor, ingrese un número.")

        if opciones[respuesta_seleccionada - 1] == pregunta['Answer']:
            print_monda("¡Correcto!")
            puntajes[i] = 10  # Si es correcto, asigna 10 puntos en la posición correspondiente
        else:
            print_monda(f"Incorrecto. La respuesta correcta era: {pregunta['Answer']}")
    
    # Sumar todos los puntajes
    puntaje_total = reduce(lambda x, y: x + y, puntajes)
    print_monda(f"\nJuego terminado. Tu puntaje final es: {puntaje_total}")
    return puntaje_total

def menu_juego(df_frecuente: pd.DataFrame):
    while True:  # Ciclo para permitir reiniciar el juego o salir
        print_monda("\nMenú del Juego de Preguntas")
        print_monda("1. Iniciar Juego")
        print_monda("2. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            puntaje = iniciar_juego(df_frecuente)
            print_monda(f"Gracias por jugar. Tu puntaje final es: {puntaje}")
        elif opcion == '2':
            print_monda("Gracias por jugar. ¡Hasta la próxima!")
            break
        else:
            print_monda("Opción no válida. Por favor, seleccione 1 o 2.")

def main():
    df = cargar_datos('JEOPARDY_CSV.csv')
    df_frecuente = filtrar_categorias_frecuentes(df)
    diccionario_categorias = crear_diccionario_categorias(df_frecuente)
    menu_juego(df_frecuente)

# Protect the entry point of the program
if __name__ == "__main__":
    main()

