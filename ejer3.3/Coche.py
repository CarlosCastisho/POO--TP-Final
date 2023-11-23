from abc import ABC,abstractmethod

class Abst_Coche(ABC):

    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def registrar_km(self):
        pass

class Coche(Abst_Coche):
    def __init__(self, marca, modelo, velocidad, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self._velocidad = velocidad
        self.kilometraje = kilometraje

    @property
    def velocidad(self):
        return self._velocidad

    def acelerar(self):
        self._velocidad += 10
        return self._velocidad

    def registrar_km(self):
        self.kilometraje += 1
        return f"El kilometraje es: {self.kilometraje}"
