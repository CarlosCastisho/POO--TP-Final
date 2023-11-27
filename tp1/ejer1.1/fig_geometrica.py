from abc import ABC, abstractmethod


class FigGeomatrica(ABC):
    """Clase para calcular el area y el perimetro"""

    @abstractmethod
    def area (self):
        """Calculo del area"""
        pass
    
    @abstractmethod
    def perimetro(self):
        """Calculo del perimetro"""
        pass
