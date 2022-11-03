from ast import match_case
from difflib import Match

#Neste exercício só estamos testando a estrutura match case
#Após o exercício 50, faremos todos novamnete com aplicações reais
cod = input('Digite o código do produto: ')
def conversor(cod):
    match cod:
        case '100':
            print("Detergente R$ 1,59")
        case '200':
            print("Arroz R$ 15,69")
        case '300':
            print("Feijão R$ 8,00")
        case _:
            print('Não existe esse produto na loja')
print(conversor(cod))