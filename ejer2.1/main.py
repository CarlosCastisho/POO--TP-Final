from Gato import Gato
from Pajaro import Pajaro
from Perro import Perro

gato1 = Gato("gato","Chimu", 3, 12)
print(gato1.info_gato())
print(gato1.accion("caminar"))
print(gato1.comida("atun"))

pajaro1 = Pajaro("Loro", "Rio", 4, "Amarrillo")
print(pajaro1.info_pajaro())
print(pajaro1.accion("volar"))
print(pajaro1.comida("Pan"))

perro1 = Perro("Perro", "Firulays", 5, "Perro")
print(perro1.info_perro())
print(perro1.accion("caminar"))
print(perro1.comida("Carne"))
