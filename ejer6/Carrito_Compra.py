from Producto import Producto
 #Herencia
class Carrito_Compra(Producto):
    def __init__(self):
        self.list_productos = []

    def agregar(self, product):
        self.list_productos.append(product)
        product.restar_stock()

    def eliminar(self, product):
        self.list_productos.remove(product)

    def total_product(self):
        total = 0
        for cantidad in self.list_productos:
            total += 1
        return f"El total de productos es: {total}"

    #Polimorfismo
    def info(self):
        info_prods = ""
        for prods in self.list_productos:
            info_prods += prods.info()
        return info_prods
            