from Punto3D import Punto3D 


#herencia
class Cubo(Punto3D):
    def __init__(self, x, y, xy, color):
        super().__init__(x, y, xy)
        self._color = color

    #Encapsulamiento
    @property
    def color(self):
        return self._color

    def volumen(self):
        vol = self.x * self.y * self.xy
        return vol

    def area_superficie(self):
        area_superf = 6 * self.x + self.y
        return area_superf

    #Polimorfismo
    def info(self):
        return f"El cubo de puntos {self.x},{self.y},{self.xy} y es de color {self._color}"

    