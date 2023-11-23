from abc import ABC, abstractclassmethod

class AbstAnimal(ABC):
    @abstractclassmethod
    def accion(self):
        pass

    @abstractclassmethod
    def comida(self):
        pass

class Animal(AbstAnimal):
    def __init__(self, tipo_animal, nombre, edad):
        self.tipo_animal=tipo_animal
        self.nombre = nombre
        self.edad = edad

    def accion(self, accion_animal:str):
        conv_accion_animal = accion_animal.upper()
        if conv_accion_animal == "VOLAR":
            return f"El {self.tipo_animal} de nombre {self.nombre} esta volando"
        elif conv_accion_animal== "CAMINAR":
            return f"El {self.tipo_animal} de nombre {self.nombre} esta caminando"
        else:
            return f"El {self.tipo_animal} de nombre {self.nombre} esta nadando"

    def comida(self, nom_comida):
        return f"El {self.tipo_animal} de nombre {self.nombre} esta comiendo {nom_comida}\n______________________________"

    