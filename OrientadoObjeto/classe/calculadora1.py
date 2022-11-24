class Calculadora:
    def somar(self, n1, n2):
        return n1+n2
    def subtrair(selfself, n1, n2):
        return n1-n2
    def multiplicar(self, n1, n2):
        return n1*n2
    def dividir(self, n1, n2):
        return n1/n2
    def dividir_resto(self, n1, n2):
        return n1%n2

calc = Calculadora()

print(f'Soma: {calc.somar(3, 4)}')
print(f"Subtração: {calc.subtrair(13, 7)}")
print(f"Multiplicação: {calc.multiplicar(2, 4)}")
print(f"Dividir: {calc.dividir(16, 5)}")
print(f"Resto: {calc.dividir_resto(4, 2)}")
