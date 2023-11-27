import math
from abc import ABC, abstractmethod

class Abst_Forma(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def info_forma(self):
        pass


class Forma(Abst_Forma):
    def __init__(self, nombre:str, color):
        self.nombre = nombre
        self.color = color

    def area(self, radio=None, base=None, altura=None):
        nomb_fig = self.nombre.upper()
        if nomb_fig == "CIRCULO":
            area_circulo = math.pi*radio*radio
            return f"El area del {self.nombre} es {area_circulo}"
        elif nomb_fig == "RECTANGULO":
            area_rect = (base*altura)
            return f"El area del {self.nombre} es {area_rect}"

    def perimetro(self, radio=None, base=None, altura=None):
        nomb_fig = self.nombre.upper()
        if nomb_fig == "CIRCULO":
            per_circulo = 2*math.pi*radio
            return f"El perimetro del {self.nombre} es: {per_circulo}"
        elif nomb_fig == "RECTANGULO":
            per_rect = 2*(base+altura)
            return f"El perimetro del {self.nombre} es: {per_rect}"

    def info_forma(self):
        return f"Nombre de la figura: {self.nombre}\n Color:{self.color}"