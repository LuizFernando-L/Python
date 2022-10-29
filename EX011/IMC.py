
print("------Calculando seu IMC------")
print("Menor que 18.5         Magreza")
print("Entre 18.5 e 24.9       Normal")
print("Entre 25.0 e 29.9    Sobrepeso")
print("Entre 30.0 e 39.9    Obesidade")
print("Maior que 40.0 Obesidade Grave")
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso/(altura*altura)
def indice(imc):
    if imc<=18.5:
        print("Você está magro")
    elif imc>18.5 and imc<=24.9:
        print("Você está no seu peso ideal")
    elif imc>24.9 and imc<=29.9:
        print("Você está com sobrepeso")
    elif imc>29.9 and imc<=39.9:
        print("Você está obeso")
    elif imc>39.9:
        print("Sua obesidade é grave, procure um médico")
    else:
        print("Não foi possível identificar seu imc, confira os dados!")
print(indice(imc))