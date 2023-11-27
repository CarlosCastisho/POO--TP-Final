from Gato import Gato
from Pajaro import Pajaro
from Perro import Perro

list_animales = [Gato("gato","Chimu", 3, 12), Pajaro("Loro", "Rio", 4, "Amarrillo"), Perro("Perro", "Firulays", 5, "Perro")]

for animales in list_animales:
    print(animales.info())


gato1 = Gato("gato","Chimu", 3, 12)
print(gato1.info_gato())
print(gato1.accion("caminar"))
print(gato1.comida("atun"))
print(gato1.sonido())

pajaro1 = Pajaro("Loro", "Rio", 4, "Amarrillo")
print(pajaro1.info_pajaro())
print(pajaro1.accion("volar"))
print(pajaro1.comida("Pan"))
print(pajaro1.sonido())

perro1 = Perro("Perro", "Firulays", 5, "Perro")
print(perro1.info_perro())
print(perro1.accion("caminar"))
print(perro1.comida("Carne"))
print(perro1.sonido())