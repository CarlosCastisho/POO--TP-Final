from Empleado import Empleado

class Trabajador(Empleado):
    def __init__(self, nombre, edad, salario, departamento, pers_acargo, años_trabajo):
        super().__init__(nombre, edad, salario, departamento, pers_acargo)
        self.años_trabajo = años_trabajo

    def acciones_empleado(self, acc_trab):
        return super().acciones_empleado(acc_trab)

    def info_empleado(self):
        return super().info_empleado()
