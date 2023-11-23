from vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, marca, modelo, vel_max, peso_persona):
        super().__init__(marca,modelo,vel_max)
        self.peso_persona = peso_persona

    def girar_dere(self):
        return f"La moto {self.marca} de modelo {self.modelo} esta girando a la derecha"
    
    def girar_izq(self):
        return f"La moto {self.marca} de modelo {self.modelo} esta girando a la izquierda"

    def detenerse(self):
        return f"La moto {self.marca} de modelo {self.modelo} se esta deteniendo a una velocidad maxima de {self.vel_max}"

    def capacidad_carga(self):
        if self.peso_persona < 160:
            return f"La carga de la moto {self.marca} de modelo {self.modelo} es {self.peso_persona} kg"
        else:
            return f"La carga de la moto {self.marca} de modelo {self.modelo} esta asu maximo"