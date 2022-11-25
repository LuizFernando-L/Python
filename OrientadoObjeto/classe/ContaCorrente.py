class ContaCorrente:
    def __init__(self):
        self.saldo = None
    def depositar(self, valor):
        self._saldo += valor
    def consultar_saldo(self):
        return self._valor
