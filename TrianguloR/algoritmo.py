import math
catetoA = float(input("Digite o Cateto Adjacente ou 0: "))
catetoO = float(input("Digite o cateto oposto ou 0: "))
hipot = float(input("Digte o hipotenusa ou 0: "))
if catetoA == 0:
    x = + (math.pow(hipot, 2)) - (math.pow(catetoO, 2))
    print(f"Cateto Adjacente {x}, Cateto Oposto {catetoO}, hipotenusa {hipot} ")
elif catetoO == 0:
    x = + (math.pow(hipot, 2)) - (math.pow(catetoA, 2))
    print(f"Cateto Adjacente {catetoA}, Cateto Oposto {x}, hipotenusa {hipot} ")
elif hipot == 0:
    x = (math.pow(catetoO, 2)) + (math.pow(catetoA, 2))
    print(f"Cateto Adjacente {catetoA}, Cateto Oposto {catetoO}, hipotenusa {x} ")
else:
    print("Algum valor invalido")
#h2 = ca2 + co2
#c02 = h2 - ca2