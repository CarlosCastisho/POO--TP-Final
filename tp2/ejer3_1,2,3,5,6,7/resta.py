class Resta:
    def __init__(self, minuendo, restando):
        self.minuendo = minuendo
        self.restando = restando
        self.resultado = 0

    def restar(self):
        self.resultado = self.minuendo - self.restando
        return self.resultado