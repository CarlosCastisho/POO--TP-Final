from fig_geometrica import FigGeomatrica

class Rectangulo(FigGeomatrica):
    """Clase Rectangulo"""
    def __init__(self, base, alt):
        super().__init__(base, alt)
        
    def area(self):
        """Funcion para calcular el area"""
        return self.base * self.alt

    def perimetro(self):
        """Funcion para calcular el perimetro"""
        return 2*(self.base + self.alt)

    