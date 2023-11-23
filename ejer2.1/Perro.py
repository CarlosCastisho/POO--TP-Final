from Animal import Animal

class Perro(Animal):
    def __init__(self, tipo_animal, nombre, edad, raza):
        super().__init__(tipo_animal, nombre, edad)
        self.raza = raza
    
    def accion(self, accion_perro):
        return super().accion(accion_perro)

    def comida(self, comida_perro):
        return super().comida(comida_perro)

    def info_perro(self):
        return f"Nombre de Especie: {self.tipo_animal}\nNombre: {self.nombre}\nEdad: {self.edad}\nRaza: {self.raza}\n______________________________ "