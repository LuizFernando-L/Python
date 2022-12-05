#in 1

import pandas as pd

#in 2

pd.Series(data=5) # Cria uma Series com o valor a
dtype: int

#In [3]:

lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
pd.Series(lista_nomes) # Cria uma Series com uma lista de nomes

#In [5]:

cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()
pd.Series(lista_nomes, index=cpfs)
dtype: object

#in 6

series_dados = pd.Series(lista_nomes, index=cpfs)
series_dados.loc['111.111.111-11']

#in 7
series_dados = pd.Series([10.2, -1, None, 15, 23.4])


print('Quantidade de linhas = ', series_dados.shape) # Retorna uma tupla com o número de linhas

print('Tipo de dados', series_dados.dtypes) # Retorna o tipo de dados, se for misto será object

print('Os valores são únicos?', series_dados.is_unique) # Verifica se os valores são únicos (sem duplicações)

print('Existem valores nulos?', series_dados.hasnans) # Verifica se existem valores nulos

print('Quantos valores existem?', series_dados.count()) # Conta quantas valores existem (excluí os nulos)

print('Qual o menor valor?', series_dados.min()) # Extrai o menor valor da Series (nesse caso os dados precisam ser do mesmo tipo)

print('Qual o maior valor?', series_dados.max()) # Extrai o valor máximo, com a mesma condição do mínimo

print('Qual a média aritmética?', series_dados.mean()) # Extrai a média aritmética de uma Series numérica

print('Qual o desvio padrão?', series_dados.std()) # Extrai o desvio padrão de uma Series numérica

print('Qual a mediana?', series_dados.median()) # Extrai a mediana de uma Series numérica

print('\nResumo:\n', series_dados.describe()) # Exibe um resumo sobre os dados na Series

#in 8

lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()

lista_cpfs = '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split()

lista_emails = 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split()

lista_idades = [32, 22, 25, 29, 38]

#in 9

pd.DataFrame(lista_nomes, columns=['nome'])

#in 10

pd.DataFrame(lista_nomes, columns=['nome'], index=lista_cpfs)


