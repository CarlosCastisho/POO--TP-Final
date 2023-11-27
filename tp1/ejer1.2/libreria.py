from abc import ABC,abstractmethod
class Libreria_Abstracta(ABC):
    @abstractmethod
    def agregar_libros(self,libro):
        pass
    
    @abstractmethod
    def sumar_total (self): 
        pass

class Libreria(Libreria_Abstracta):
    def __init__ (self):
        self.libros=[]

    def agregar_libros(self,libro):
        self.libros.append(libro)

    def sumar_total (self): 
        total=0
        for libro in self.libros:
            total+= libro.precio
        return f"El total a pagar:{total}"
