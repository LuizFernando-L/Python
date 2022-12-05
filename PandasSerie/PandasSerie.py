import pandas as pd

pd.Series(data=5) #Cria uma Serie com o valor a

dtype: int64

lista_nomes = 'Howard Ian Peter Jonah Kellie'.split()
pd.Series(lista_nomes) #Cria uma Serie com uma lista de nomes

dtype: object
dados = {'nome1':'Howard',
         'nome2':'Ian',
         'nome3':'Peter',
         'nome4':'Jonah',
         'nome5':'Kellie'}
pd.Series(dados)#Cria uma Serie com um dicionário
