from Gerente import Gerente
from Trabajador import Trabajador

trabajador1 = Trabajador("Jose", 30, 200000, "Administrativo", 0, 2)
print(trabajador1.info_empleado())
print(trabajador1.acciones_empleado("Trabaja"))
print("-----------------------------------------------------------------")


gerente1 = Gerente("Carlos", 31, 400000, "Sistemas", 10)
print(gerente1.info_empleado())
print(gerente1.acciones_empleado("Delega"))