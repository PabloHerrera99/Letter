from letra import Letra

class Palabra:
    
    def __init__(self) -> None:
        self.letras = []
    
    def encode(self, palabra):
        letra= []
        for i in palabra:
            pos = []
            if not i in letra:
                letra.append(i)
                for j in range(len(palabra)):
                    if i == palabra[j]:
                        pos.append(j+1)
                l = Letra(pos, i)
                self.letras.append(l)
    
    def __repr__(self) -> str:
        return f'{self.letras}'
            
