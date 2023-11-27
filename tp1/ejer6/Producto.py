from abc import ABC, abstractmethod

class Abst_Producto(ABC):
    
    @abstractmethod
    def info(self):
        pass

#Abstr
class Producto(Abst_Producto):
    def __init__(self, nombre, precio, cantidad, estado, categoria, codigo_prod):
        self.nombre =  nombre
        self.precio = precio
        self.cantidad = cantidad
        self.estado = estado
        self.categoria = categoria
        self._codigo_prod = codigo_prod
    #Encap
    @property
    def codigo_prod(self):
        return self._codigo_prod

    def info(self):
        return f"Nombre: {self.nombre}\nPrecio:{self.precio}\n----------------------------\n"

    def restar_stock(self):
        self.cantidad -= 1
        return self.cantidad