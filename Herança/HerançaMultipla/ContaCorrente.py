#In 17
class ContaCorrente:
    def __init__(self, nome):
        self.nome = nome
        self.email = None
        self.telefone = None
        self._saldo = 0
    def _checar_saldo(self, valor):
        return self._saldo >= valor
    def depositar(self, valor):
        self._saldo += valor
    def sacar(self, valor):
        if self._checar_saldo(valor):
            self._saldo -= valor
            return True
        else:
            return False
    def obter_saldo(self):
        return self._saldo
#In 18
class ContaPF(ContaCorrente):
    def __init__(self, nome, cpf):
        super().__init__(nome)
        self.cpf = cpf
    def solicitar_emprestimo(self, valor):
        return self.obter_saldo()>=500
#In 19
class ContaPJ(ContaCorrente):
    def __init__(self, nome, cnpj):
        super().__init__(nome)
        self.cnpj = cnpj
    def sacar_emprestimo(self, valor):
        return valor <=5000
#In20
conta_pf1 = ContaPF(input("Digite seu Nome: "), input("Digite seu CPF: "))
conta_pf1.depositar(int(input("Quanto deseja depositar: ")))

print(f"Seu saldo é {conta_pf1.obter_saldo()}")
print(f"Receberá emprestimo = {conta_pf1.solicitar_emprestimo(2000)}")

conta_pf1.sacar((int(input("Quanto deseja sacar? "))))
print(f"Saldo atual é {conta_pf1.obter_saldo()}")
print(f"Receberá empréstimo = ", conta_pf1.solicitar_emprestimo(2000))