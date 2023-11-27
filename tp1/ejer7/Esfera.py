from Punto3D import Punto3D 
import math

class Esfera(Punto3D):
    def __init__(self, x, y, xy, radio, color):
        super().__init__(x, y, xy)
        self.radio = radio
        self._color = _color

    @property
    def color (self):
        return self._color

    def volumen(self):
        vol_esfera = (4/3)*(math.pi)*(r**3)
        return vol_esfera

    def area_super(self):
        area_esfera = (4)*math.pi*(r**2)
        return area_esfera