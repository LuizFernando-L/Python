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

    #Nas linhas 2 e 3,  inicializamos as variáveis que contêm o primeiro e o último indíce da lista. No começo da execução, esses valores são o índice 0 para o mínimo e o último índice, que é o tamanho da lista menos 1. Essas variáveis serão atualizadas dentro do loop, conforme condição.
	#° Na linha 4 usamos o while como estrutura de repetição, pois não sabemos quantas vezes a repetição deverá ser executada. Esse while fará com que a execução seja feita para todos os campos binários.
	#° Na linha 6, usamos uma equação matemática (a média estatística) para encontrar o meio da lista
	#° Na linha 8, checamos se o valor que estamos buscando é menor que o valor que se encontra no meio da lista
	#° Caso seja, então vamos para linha 9, na qual atualizando o índice máximo. Nesse cenário, vamos excluir metade superior da lista original
	#° Caso o valor não seja menor que o do meio da lista, então vamos para a linha 10, na qual testamos se ele é maior. Se for, então atualizamos o menor índice excluindo assim a metade inferior.
	#° Se o valor procurando não for nem menor nem maior e ainda estivermos dentro do loop, então ele é igual e o valor é True é retornado pelo comando na linha 13.
	#° Porém, se já fizermos todos os testes e não encontrarmos o valor, ent´~ao é retornado False na linha 14
