from Circulo import Circulo
from Rectangulo import Rectangulo

circulo1 = Circulo("Circulo", "Rojo")
print(circulo1.info_forma())
print(circulo1.area(4))
print(circulo1.perimetro(4))

rectangulo1 = Rectangulo("Rectangulo", "Naranja")
print(rectangulo1.info_forma())
print(rectangulo1.area(2,5))
print(rectangulo1.perimetro(2,5))