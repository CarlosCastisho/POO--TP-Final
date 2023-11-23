from Persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, edad, dni, salario, cargo:str):
        super().__init__(nombre, edad, dni)
        self.salario = salario
        self.cargo = cargo

    def cal_salario_cargo(self):
        may_cargo = self.cargo.upper()
        if may_cargo == "ANALISTA":
            self.salario += 50000
        elif may_cargo == "PROGRAMADOR":
            self.salario += 10000 
        elif may_cargo == "GERENTE":
            self.salario += 90000

    def consulta_salario(self):
        return self.salario

    #Abstraccion
    def info(self):
        return f"Nombre: {self.nombre}\nCargo: {self.cargo}"