from Empleado import Empleado

class Trabajador(Empleado):
    def __init__(self, nombre, edad, salario, departamento, pers_acargo,acc_empleado, años_trabajo):
        super().__init__(nombre, edad, salario, departamento, pers_acargo,acc_empleado)
        self.años_trabajo = años_trabajo

    def acciones_empleado(self):
        return super().acciones_empleado()

    def info_empleado(self):
        return super().info_empleado()
