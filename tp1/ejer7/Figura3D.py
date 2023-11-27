from abc import ABC, abstractmethod

#Abstraccion
class Figura(ABC):
    @abstractmethod
    def volumen(self):
        pass

    @abstractmethod
    def area_super(self):
        pass