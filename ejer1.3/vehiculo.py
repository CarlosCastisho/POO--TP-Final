from abc import ABC,abstractmethod

class Vehiculo:
    def __init__(self, marca, modelo, vel_max):
        self.marca = marca
        self.modelo = modelo
        self.vel_max = vel_max

    @abstractmethod
    def girar_dere(self):
        pass
    
    @abstractmethod
    def girar_izq(self):
        pass

    @abstractmethod
    def detenerse(self):
        pass