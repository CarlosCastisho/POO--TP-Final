from Cliente import Cliente
from Producto import Producto
from Carrito_Compra import Carrito_Compra

product1 = Producto("Ala", 3000, 18, "Nuevo", "Lavado", "Add-d33")
product2 = Producto("AlaLiquido", 2000, 11, "Nuevo", "Lavado", "Add-d35")
product3 = Producto("Queso", 450, 9, "Nuevo", "Lacteo", "Afg-d35")


carrito1 = Carrito_Compra()
carrito1.agregar(product1)
carrito1.agregar(product2)
carrito1.agregar(product3)

carrito1.eliminar(product2)


cliente1 = Cliente("Carlos", 12345, "aaaaaa", carrito1)

print(carrito1.total_product())
print(carrito1.info())


