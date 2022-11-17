import random
#TESTANDO lISTA
nome1 = str(input("Digite o 1° nome: "))
nome2 = str(input("Digite o 2° nome: "))
nome3 = str(input("Digite o 3° nome: "))
lista = [nome1, nome2, nome3]
escolhido = random.choice(lista)
print("O nome escolhido foi: {}".format(escolhido))