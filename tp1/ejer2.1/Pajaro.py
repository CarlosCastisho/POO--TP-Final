from Animal import Animal

class Pajaro(Animal):
    def __init__(self, tipo_animal, nombre, edad, color_plumas):
        super().__init__(tipo_animal, nombre, edad)
        self.color_plumas = color_plumas
    
    def accion(self, accion_pajaro):
        return super().accion(accion_pajaro)

    def comida(self, comida_pajaro):
        return super().comida(comida_pajaro)

    def info_pajaro(self):
        return f"Nombre de Especie: {self.tipo_animal}\nNombre: {self.nombre}\nEdad: {self.edad}\nColor de plumas: {self.color_plumas}\n______________________________ "