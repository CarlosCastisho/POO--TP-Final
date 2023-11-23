from Carrito_Compra import Carrito_Compra

class Cliente():
    def __init__(self, nombre, dni, dirección, carrito_compra):
        self.nombre = nombre
        self.dni = dni
        self.dirección = dirección
        self.carrito_compra = Carrito_Compra()

    def info(self):
        return f"Nombre: {self.nombre}\nDirección: {self.dirección}"