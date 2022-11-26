import re

string = 'meuArquivo_20-01-2020.py'

padrao = "[a-zA-Z]*"

texto1 = re.search(padrao, string).group()

texto2 = re.match(padrao, string).group()

texto3 = re.split("_", string)[0]

print(texto1)

print(texto2)

print(texto3)