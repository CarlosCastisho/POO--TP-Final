from vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    
    def __init__(self, marca, modelo, vel_max):
        super().__init__(marca, modelo, vel_max)

    def girar_dere(self):
        return f"La bicicleta {self.marca} de modelo {self.modelo} esta girando a la derecha"
    
    def girar_izq(self):
        return f"La bicicleta {self.marca} de modelo {self.modelo} esta girando a la izquierda"

    def detenerse(self):
        return f"La bicicleta {self.marca} de modelo {self.modelo} se esta deteniendo a una velocidad {self.vel_max}"
