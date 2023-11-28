class Suma:
    def __init__(self, sumando1, sumando2):
        self.sumando1 = sumando1
        self.sumando2 = sumando2
        self.resultado = 0

    def sumar(self):
        self.resultado = self.sumando1 + self.sumando2
        return self.resultado