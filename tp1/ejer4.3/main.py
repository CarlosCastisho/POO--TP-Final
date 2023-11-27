from Gerente import Gerente
from Trabajador import Trabajador


lista_empleados = [Trabajador("Jose", 30, 200000, "Administrativo", 0, "nada", 2), Gerente("Carlos", 31, 400000, "Sistemas", 10, "Cafe")]

for lista in lista_empleados:
    print(lista.info_empleado())
    print(lista.acciones_empleado())
