from Empleado import Empleado
from Departamento import Departamento

#Herencia
class Gerente(Empleado):
    
    def __init__(self, nombre, edad, dni, salario, cargo:str):
        super().__init__(nombre, edad, dni, salario, cargo)

    @property
    def departamento(self):
        return self._departamento

    #Polimorfismo
    def info(self):
        return f"Nombre: {self.nombre}\nCargo: {self.cargo}"