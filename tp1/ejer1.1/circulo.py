"""Importacion de las funciones matematicas y FigGeometrica"""
import math
from fig_geometrica import FigGeomatrica


class Circulo(FigGeomatrica):
    """Clase del circulo"""
    def __init__(self, rad):
        self.rad = rad

    def area (self):
        """Clacular el area del circulo"""
        return math.pi * (self.rad**2)

    def perimetro (self):
        """Calcular el perimetro del circulo"""
        return 2*math.pi*self.rad