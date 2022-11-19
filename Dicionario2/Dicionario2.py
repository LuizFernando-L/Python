cadastro = {
    'nome' : ['João', 'Ana', 'Pedro', 'Marcela'],
    'cidade' : ['São Paulo', 'São Paulo', 'Rio de Janeiro', 'Curitiba'],
    'idade' : [25, 33, 37, 18]
}
print("len(cadastro)",len(cadastro))
print("\n cadastro.keys() = \n", cadastro.keys())
print("\n cadastro.values() = \n", cadastro.values())
print("\n cadastro.items() = \n", cadastro.items())

print("\n cadastro['nome'] = ", cadastro['nome'])
print("\n cadstro['nome'][2] = ", cadastro['nome'][2])
print("\n cadasto['idade'][2:] ", cadastro['idade'][2:])

print(len(cadastro['nome']))
print(len(cadastro['cidade']))
print(len(cadastro['idade']))

qtde_itens = sum([len(cadastro[chave]) for chave in cadastro])

print(f"\n\n Quantidade de elementos no dicionário = {qtde_itens}")