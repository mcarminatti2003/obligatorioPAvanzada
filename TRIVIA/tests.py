import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from main import iniciar_juego, menu_juego, generar_preguntas
from question_selection import seleccionar_pregunta, seleccionar_respuestas_incorrectas, mostrar_opciones
from data_preparation import cargar_datos, filtrar_categorias_frecuentes, crear_diccionario_categorias
from tuple_classification import leer_dataframe_generador, clasificar_tuplas

class TestJeopardyGame(unittest.TestCase):
    def setUp(self):
        # Cargar el DataFrame con los datos del juego
        self.df = cargar_datos('JEOPARDY_CSV.csv')
        self.df_frecuente = filtrar_categorias_frecuentes(self.df, min_count=1)

    @patch('builtins.input', side_effect=['1', '1', '2', '1', '3'])  # Mocking 5 user inputs
    @patch('builtins.print')  # Mocking print to avoid console output during testing
    def test_iniciar_juego(self, mock_print, mock_input):
       score = iniciar_juego(self.df_frecuente)
       self.assertIsInstance(score, int)
       self.assertTrue(mock_print.called)

    @patch('builtins.input', side_effect=['1', '1', '2','3','3'])  # Mocking user inputs
    @patch('builtins.print')  # Mocking print to avoid console output during testing
    def test_menu_juego(self, mock_print, mock_input):
        with patch('main.iniciar_juego', return_value=1):
            menu_juego(self.df_frecuente)
        self.assertTrue(mock_print.called)

    def test_cargar_datos(self):
        df = cargar_datos('JEOPARDY_CSV.csv')
        self.assertIsInstance(df, pd.DataFrame)

    def test_filtrar_categorias_frecuentes(self):
        df_filtrado = filtrar_categorias_frecuentes(self.df, min_count=1)
        categorias_filtradas = df_filtrado['Category'].unique()
        self.assertTrue(len(categorias_filtradas) > 0)
    
    def test_leer_dataframe_generador(self):
        generador = leer_dataframe_generador(self.df)
        tupla = next(generador)
        self.assertIsInstance(tupla, tuple)

    
    def test_seleccionar_pregunta(self):
        with patch('builtins.input', return_value='1'):
            pregunta = seleccionar_pregunta(self.df_frecuente)
            self.assertIn(pregunta['Question'], self.df_frecuente['Question'].values)
    
    def test_seleccionar_respuestas_incorrectas(self):
        df_categoria = self.df_frecuente[self.df_frecuente['Category'] == 'Category1']
        if len(df_categoria) >= 2:
            incorrectas = seleccionar_respuestas_incorrectas(self.df_frecuente, 'Category1')
            self.assertEqual(len(incorrectas), 2)
        else:
            self.skipTest("Not enough data for sampling in this category")    

    def test_mostrar_opciones(self):
        df_categoria = self.df_frecuente[self.df_frecuente['Category'] == 'Category1']
        if len(df_categoria) >= 3:
            pregunta = self.df_frecuente.iloc[0]
            incorrectas = seleccionar_respuestas_incorrectas(self.df_frecuente, 'Category1')
            opciones = mostrar_opciones(incorrectas, pregunta)
            self.assertEqual(len(opciones), 3)
            self.assertIn(pregunta['Answer'], opciones)
        else:
            self.skipTest("Not enough data for sampling in this category")    



if __name__ == '__main__':
    unittest.main()