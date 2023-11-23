from Animal import Animal

class Gato(Animal):
    def __init__(self, tipo_animal, nombre, edad, cantidad_bigotes):
        super().__init__(tipo_animal, nombre, edad)
        self.cantidad_bigotes = cantidad_bigotes

    def accion(self, accion_gato):
        return super().accion(accion_gato)

    def comida(self, comida_gato):
        return super().comida(comida_gato)

    def info_gato(self):
        return f"Nombre de Especie: {self.tipo_animal}\nNombre: {self.nombre}\nEdad: {self.edad}\nCatidad de bigotes: {self.cantidad_bigotes}\n______________________________ "