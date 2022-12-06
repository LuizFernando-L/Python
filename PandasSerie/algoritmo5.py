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

#in 11

dados = list(zip(lista_nomes, lista_cpfs, lista_idades, lista_emails)) # cria uma lista de tuplas

pd.DataFrame(dados, columns=['nome', 'cpfs', 'idade', 'email'])

#in 12
dados = {

    'nomes': 'Howard Ian Peter Jonah Kellie'.split(),

    'cpfs' : '111.111.111-11 222.222.222-22 333.333.333-33 444.444.444-44 555.555.555-55'.split(),

    'emails' : 'risus.varius@dictumPhasellusin.ca Nunc@vulputate.ca fames.ac.turpis@cursusa.org non@felisullamcorper.org eget.dictum.placerat@necluctus.co.uk'.split(),

    'idades' : [32, 22, 25, 29, 38]

}

pd.DataFrame(dados)

#in3

df_dados = pd.DataFrame(dados)

print('\nInformações do DataFrame:\n')

print(df_dados.info()) # Apresenta informações sobre a estrutura do DF

print('\nQuantidade de linhas e colunas = ', df_dados.shape) # Retorna uma tupla com o número de linhas e colunas

print('\nTipo de dados:\n', df_dados.dtypes) # Retorna o tipo de dados, para cada coluna, se for misto será object

print('\nQual o menor valor de cada coluna?\n', df_dados.min()) # Extrai o menor de cada coluna

print('\nQual o maior valor?\n', df_dados.max()) # Extrai o valor máximo e cada coluna

print('\nQual a média aritmética?\n', df_dados.mean()) # Extrai a média aritmética de cada coluna numérica

print('\nQual o desvio padrão?\n', df_dados.std()) # Extrai o desvio padrão de cada coluna numérica

print('\nQual a mediana?\n', df_dados.median()) # Extrai a mediana de cada coluna numérica

print('\nResumo:\n', df_dados.describe()) # Exibe um resumo

df_dados.head() # Exibe os 5 primeiros registros do DataFrame

#in 4

df_uma_coluna = df_dados['idades']
print(type(df_uma_coluna))
print('Média de idades = ', df_uma_coluna.mean())
df_uma_coluna

#in 15
colunas = ['nomes', 'cpfs']
df_duas_colunas = df_dados[colunas]
print(type(df_duas_colunas))
df_duas_colunas

#in 16

import requests

texto_string = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html').text

print(texto_string[:100])
