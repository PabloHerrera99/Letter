from palabra import Palabra

class Phrase:
    def __init__(self) -> None:
        self.palabras = []

    def encode(self, frase):
        palabras = frase.split(' ')
        for i in palabras:
            a = Palabra()
            a.encode(i)
            self.palabras.append(a)
    def __repr__(self) -> str:
        return str(self.palabras)

    