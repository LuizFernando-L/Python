from ast import match_case
from difflib import Match


print('---Coneversor de medidas---')
print('(M) metros')
print('(C) centimetros')
print('(L) litros')
tipo = input("O que deseja converter? ")
def conversor(tipo):
    match tipo:
        case 'm':
            print("Faremos a conversão")
        case 'c':
            print("Aguarde")
        case 'l':
            print("Em andamento")
        case _:
            print('Não posso fazer este tipo de conversão')
