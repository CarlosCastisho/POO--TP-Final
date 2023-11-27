from abc import ABC, abstractmethod


class Abst_FigGeomatrica(ABC):
    """Clase para calcular el area y el perimetro"""

    @abstractmethod
    def area (self):
        """Calculo del area"""
        pass
    
    @abstractmethod
    def perimetro(self):
        """Calculo del perimetro"""
        pass

class FigGeomatrica(Abst_FigGeomatrica):
    def __init__(self, base, alt):
        self.base = base
        self.alt = alt

    def area(self):
        return "Estamos calculando el area"

    def perimetro(self):
        return "EStamos calculando el perimetro"

