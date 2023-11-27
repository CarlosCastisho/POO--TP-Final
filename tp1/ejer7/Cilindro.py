from Punto3D import Punto3D 
import math

class Cilindro(Punto3D):
    def __init__(self, x, y ,xy, radio, altura):
        super().__init__(x, y ,xy)
        self.radio = radio
        self.altura = altura

    def volumen(self):
        volum_esfera = math.pi * self.altura * (self.radio ** 2)
        return volum_esfera

    def area_super(self):
        area_cilindro = (2*math.pi*self.radio * (self.altura + self.radio))
        return area_cilindro