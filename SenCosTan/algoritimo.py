import math
angulo = int(input("Digite o angulo: "))

def conversor(angulo):
    match angulo:
        case '0':
            print("Seno: 0 Cosseno: 1  Tangente: 2 ")
        case '30':
            print("Seno: 0,5 Cosseno: 0,86 Tangente: 0,57 ")
        case '45':
            print("Seno: 0,71  Cosseno: 0,71 Tangente: 1 ")
        case '60':
            print("Seno: 0,86 Consseno: 0,5 Tangente: 1,73 ")
        case '90':
            print("Seno: 1 Cosseno: 0 Tangente:  ")
        case _:
            print("Angulo invalido")
print(conversor(angulo))
