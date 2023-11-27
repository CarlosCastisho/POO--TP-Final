from Cubo import Cubo
from Esfera import Esfera
from Cilindro import Cilindro

cubo1 = Cubo(4,5,6,"Rojo")
esfera1 = Esfera(5,7,4,8,"Azul")
cilindro1 = Cilindro(8,3,6,5,10)

#Info del cubo
print(cubo1.volumen())
print(cubo1.area_superficie())
print(cubo1.info())

#Info de la Esfera
print(esfera1.volumen())
print(esfera1.area_super())

#ingo de cilindro
print(cilindro1.volumen())
print(cilindro1.area_super())