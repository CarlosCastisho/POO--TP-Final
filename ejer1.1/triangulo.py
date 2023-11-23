from fig_geometrica import FigGeomatrica

class Triangulo(FigGeomatrica):
    """Clase Triangulo"""
    def __init__(self, base, alt, lado1, lado2):
        self.base=base
        self.alt = alt
        self.lado1 = lado1
        self.lado2 = lado2

    def area(self):
        """Calcular el area del triangulo"""
        return (self.base * self.alt)/2

    def perimetro(self):
        """Calcular el perimetro del triangulo"""
        return self.base + self.lado1 + self.lado2