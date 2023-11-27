from Forma import Forma

class Circulo(Forma):
    def __init__(self, nombre:str, color):
        super().__init__(nombre, color)

    def area(self, radio):
        return super().area(radio)

    def perimetro(self, radio):
        return super().perimetro(radio)