from multi import Mult as m # importación absoluta - Alias
from resta import Resta as r # importación absoluta - Alias
import suma as s #Sin usar from - Alias
from mi_pack.imprimir import imprimir

mul1 = m(5,2)
imprimir(mul1.multiplicar())

resta1 = r(5,3)
imprimir(resta1.restar())

suma1 = s.Suma(4,8)
imprimir(suma1.sumar())

