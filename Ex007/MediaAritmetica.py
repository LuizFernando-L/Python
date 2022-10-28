qtd = int(input("Quantas notas deseja inserir? "))
n = 1
soma = 0
while n<=qtd:
    nota = float(input(f"Digite a {n}° nota: "))
    n=n+1
    soma = soma + nota
media = soma / qtd
print(media)