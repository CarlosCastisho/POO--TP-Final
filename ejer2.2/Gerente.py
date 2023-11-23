from Empleado import Empleado 

class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, departamento, pers_acargo):
        super().__init__(nombre, edad, salario, departamento, pers_acargo)

    def acciones_empleado(self, acc_gerente):
        return super().acciones_empleado(acc_gerente)

    def info_empleado(self):
        return super().info_empleado()