from vehiculo import Vehiculo

class Coche(Vehiculo):

    def __init__(self, marca, modelo, vel_max, caballo_fuerza):
        super().__init__(marca, modelo, vel_max)
        self.caballo_fuerza = caballo_fuerza

    def girar_dere(self):
        return f"El vehiculo {self.marca} de modelo {self.modelo} esta girando a la derecha"
    
    def girar_izq(self):
        return f"El vehiculo {self.marca} de modelo {self.modelo} esta girando a la izquierda"

    def detenerse(self):
        return f"El vehiculo {self.marca} de modelo {self.modelo} se esta deteniendo a una velocidad maxima de {self.vel_max}"
