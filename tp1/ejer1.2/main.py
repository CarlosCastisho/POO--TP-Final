from libro import Libro
from libreria import Libreria

libro1 = Libro("Harry Potter", "J. K Rowling", 2000)
libro2 = Libro("100 años de soledad", "Gabriel García Marquez", 1500)
print(libro1.agre_titulo())
print(libro2.agre_titulo())

libreria_compra = Libreria()
libreria_compra.agregar_libros(libro1)
libreria_compra.agregar_libros(libro2)
print(libreria_compra.sumar_total())