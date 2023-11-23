from Gerente import Gerente

class Departamento(Gerente):
    def __init__(self, nombre, piso):
        self.nombre = nombre
        self.piso = piso
        self.lista_emp = []

    def agregar(self, datos_empleado):
        self.lista_emp.append(datos_empleado)

    def eliminar(self, datos_empleado):
        self.lista_emp.remove(datos_empleado)

    def consultar(self):
        info_lista = ""
        for listas in self.lista_emp:
            info_lista += listas.info()
        return info_lista
