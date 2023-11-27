from Empleado import Empleado
from Departamento import Departamento
from Gerente import Gerente

#Instancio las class
empleado1 = Empleado("Carlos" ,31 , 12345, 200000, "Analista")
empleado2 = Empleado("Alan" ,31 , 123456, 10000, "Programador")
gerente1 = Gerente("Dani", 34, 1234567, 500000, "Gerente")

dep_sistemas = Departamento("sistemas", 3)

#Agrego al departamento de sistemas los empleados y gerentes
dep_sistemas.agregar(empleado1)
dep_sistemas.agregar(empleado2)
dep_sistemas.agregar(gerente1)

#Bonus por cargo y consulta de salario
empleado1.cal_salario_cargo()
print(empleado1.consulta_salario())

empleado2.cal_salario_cargo()
print(empleado2.consulta_salario())

gerente1.cal_salario_cargo()
print(gerente1.consulta_salario())

#Consulta de empleados en sistemas

print(dep_sistemas.consultar())

