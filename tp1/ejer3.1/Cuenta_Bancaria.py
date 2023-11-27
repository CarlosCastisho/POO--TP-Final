from abc import ABC, abstractmethod

class Abst_Cuenta_Bancaria(ABC):

    @abstractmethod
    def depositar(self):
        pass

    @abstractmethod
    def retirar(self):
        pass

    @abstractmethod
    def consultar(self):
        pass

class Cuenta_Bancaria(Abst_Cuenta_Bancaria):
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, depo_cuenta):
        estado = self.saldo + depo_cuenta
        return estado

    def retirar(self, importe_retiro):
        if importe_retiro > 0:
            estado_retiro = self.saldo - importe_retiro
            return estado_retiro
        else:
            return "Retire un saldo mayor que cero"

    def consultar(self):
        return self.saldo