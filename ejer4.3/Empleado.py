from abc import ABC, abstractmethod

class Abst_Empleado(ABC):
    
    @abstractmethod
    def acciones_empleado(self):
        pass
    @abstractmethod
    def info_empleado(self):
        pass

class Empleado(Abst_Empleado):
    def __init__(self, nombre, edad, salario, departamento, pers_acargo, acc_empleado):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.departamento = departamento
        self.pers_acargo = pers_acargo
        self.acc_empleado = acc_empleado

    def acciones_empleado(self):
        return f"El empleado {self.nombre} esta en el departamento {self.departamento} realizando {self.acc_empleado} "

    def info_empleado(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nSalario: {self.salario}\nDepartamento: {self.departamento}\nPersonas acargo: {self.pers_acargo}"