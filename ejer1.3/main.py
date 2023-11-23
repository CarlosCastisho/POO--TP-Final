from coche import Coche
from bicicleta import Bicicleta
from moto import Moto

coche1 = Coche("VW", "Amarok", 120, 44)
print(coche1.girar_dere())
print(coche1.girar_izq())
print(coche1.detenerse())

bici1 = Bicicleta("www", "asdddd", 68)
print(bici1.girar_dere())
print(bici1.girar_izq())
print(bici1.detenerse())

moto1 = Moto("Rouser", "200", 200, 80)
print(moto1.girar_izq())
print(moto1.girar_dere())
print(moto1.detenerse())
print(moto1.capacidad_carga())