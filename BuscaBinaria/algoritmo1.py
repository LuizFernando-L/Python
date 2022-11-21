def executar_busca_binaria(lista, valor):
    minimo = 0
    maximo = len(lista)-1
    while minimo <= maximo:
        # Encontra o elemneto que divide a lista no meio
        meio = (minimo + maximo)//2
        #Verifica se o valor procurado está a esquerda ou a direita do valor central
        if valor < lista[meio]:
            maximo = meio -1
        else:
            return True #se o valor for encontrado para aqui
    return False # Se chegar até aqui, significa que o valor não foi encontrado
lista =list(range(1, 50))
print(lista)

print("\n", executar_busca_binaria(lista=lista, valor=10))
print("\n", executar_busca_binaria(lista=lista, valor=200))
