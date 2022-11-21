def procurar_valor(lista, valor):
    tamanho_lista = len(lista)
    for i in range(tamanho_lista):
        if valor == lista[i]:
            return i
        return None
vogais = 'aeiou'
esc = str(input("Digite uma vogal: "))
resultado = procurar_valor(lista=vogais, valor=esc)
if resultado != None:
    print(f"Valor encontrado na posição {resultado}")
else:
    print("Valor não encontrado")
