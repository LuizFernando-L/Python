#Exemplo 1 -  Criação do dicionário vazio, com atribuição posterior de chave e valor
dici_1 = {}
dici_1['Nome'] = "João"
dici_1['idade'] = 30
#Exemplo 2 - Criação de dicionário usando um par elementos na forma, chave : valor
dici_2 = {'Nome': 'João', 'idade':30}
#Exemplo 3 - Criação de dicionário com uma lista de tuplas. Cada tupla representa um par chave : valor
dici_3 = dict([('Nome', "João"), ('idade', 30)])
#Exemplo 4 - Criação de dicionário com a função built-in zip() e duas listas, uma com as chaves, outra com os valores.
dici_4 = dict(zip(['Nome', 'idade'], ["João", 30]))
print(dici_1==dici_2==dici_3==dici_4)#Testando se as diferentes construções tem os mesmos resultados
