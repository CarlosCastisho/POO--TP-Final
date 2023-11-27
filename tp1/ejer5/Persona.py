class Persona():
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self._dni = dni

   # Emcapsulamiento
    @property
    def dni(self):
        return self._dni

    def info(self):
        pass