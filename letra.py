
class Letra:
    def __init__(self, posicion, letra) -> None:
        self.posicion = posicion
        self.letra = letra
    def __repr__(self) -> str:
        return f'{self.letra}: {self.posicion}'
    
