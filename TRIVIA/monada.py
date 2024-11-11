from typing import Callable, Any

class Monda:
    def __init__(self, value: Any):
        self.value = value

    def bind(self, func: Callable[[Any], 'Monda']) -> 'Monda':
        """
        Aplica la función `func` al valor contenido en la mónada y devuelve una nueva mónada.
        func (Callable[[Any], 'Monda']): Una función que toma un valor y devuelve una nueva mónada.
        Monda: Una nueva mónada con el resultado de aplicar `func` al valor.
        """
        result = func(self.value)
        return Monda(result)

    def map(self, func: Callable[[Any], Any]) -> 'Monda':
        """
        Aplica la función `func` al valor contenido en la mónada y devuelve una nueva mónada.
        func (Callable[[Any], Any]): Una función que toma un valor y devuelve un nuevo valor.
        Monda: Una nueva mónada con el resultado de aplicar `func` al valor.
        """
        return self.bind(lambda x: Monda(func(x)))

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return repr(self.value)

def print_monda(message: str) -> Monda:
    """
    Función para encapsular la impresión de mensajes.
    message (str): El mensaje a imprimir.
    Monda: Una mónada que representa la operación de impresión (sin valor significativo).
    """
    def print_func(_: None) -> None:
        print(message)
        return None
    return Monda(None).map(print_func)
