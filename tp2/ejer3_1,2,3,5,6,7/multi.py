class Mult:
    def __init__(self, multiplicando, multiplicador):
        self.multiplicando = multiplicando
        self.multiplicador = multiplicador
        self.resultado = 0

    def multiplicar(self):
        self.resultado = self.multiplicando * self.multiplicador
        return self.resultado