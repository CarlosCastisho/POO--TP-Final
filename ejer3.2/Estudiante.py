from abc import ABC, abstractmethod

class Abst_Estudiante(ABC):
    
    @abstractmethod
    def info(self):
        pass


class Estudiante(Abst_Estudiante):
    def __init__(self, nombre, edad, dni, calificaciones:list):
        self.nombre = nombre
        self.edad = edad
        self._dni = dni
        self._calificaciones = calificaciones

    @property
    def dni(self):
        return self._dni

    @property
    def calificaciones(self):
        return self._calificaciones

    def info(self):
        return f"Nombre: {self.nombre}\nEdad:{self.edad}\nDNI: {self.dni}\nCalificaciones:{self.calificaciones}"