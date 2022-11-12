operacao = input("Qual operação deseja fazer:  abaixar ou subir ").lower()
if operacao == 'subir':
    reajuste = float(input("Digite qual será o reajuste: "))
    salario = float(input("Digite qual será o salário: "))
    valorf = ((salario * reajuste)/100)+salario
    print("O sálario final é R$ {:.2f}".format(valorf))
elif operacao == 'abaixar':
    reajuste = float(input("Quantos % é o reajuste: "))
    salario = float(input("Digite qual será o salário: "))
    valorf = salario - ((salario * reajuste) / 100)
    print("O sálario final é R$ {:.2f}".format(valorf))
else:
    print("Argumento invalido")