dia = float(input("Quantos dias você ficou com o carro? "))
km = float(input("Quantos km você rodou? "))
total = (dia*60)+(km*0.15)
print("O valor a ser pago é de R$ {:.2f}".format(total))