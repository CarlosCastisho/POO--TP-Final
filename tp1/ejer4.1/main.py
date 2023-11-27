from circulo import Circulo
from rectangulo import Rectangulo
from triangulo import Triangulo

list_fig = [Circulo(4), Rectangulo(4,5), Triangulo(4,5,6,8)]

for listas in list_fig:
    print(listas.area())
    print(listas.perimetro())