from Empleado import Empleado 

class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, departamento, pers_acargo, acc_empleado:str):
        super().__init__(nombre, edad, salario, departamento, pers_acargo, acc_empleado)

    def acciones_empleado(self):
        may_acc_gerente = self.acc_empleado.upper()
        if may_acc_gerente == "CAFE":
            return f"El empleado esta tomando cafe"
        else:
            return f"El empleado no esta haciendo nada"

    def info_empleado(self):
        return super().info_empleado()