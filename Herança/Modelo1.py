class Pessoa:
    def __init__(self):
        self.cpf = None
        self.nome = None
        self.endereco = None

class Funcionario(Pessoa):
    def __init__(self):
        self.matricula = None
        self.salario = None
    def bater_ponto(self):
        #código aqui
        pass
    def fazer_login(self):
        #código aqui
        pass

class Cliente(Pessoa):
    def __init__(self):
        self.codigom= None
        self.dataCadastro = None
    def fazer_compras(self):
        #código aqui
        pass
    def pagar_conta(self):
        #código aqui
        pass
#testes

f1 = Funcionario()
f1.nome = "FuncionarioA"

print(f1.nome)

c1 = Cliente()

c1.cpf = "111.111.111-11"

print(c1.cpf)
