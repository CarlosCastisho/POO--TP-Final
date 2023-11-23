from Forma import Forma

class Rectangulo(Forma):
    def __init__(self, nombre:str, color):
        super().__init__(nombre, color)

    def area(self, base:float, altura:float):
        return super().area(base, altura)

    def perimetro(self, base:float, altura:float):
        return super().perimetro(base, altura)