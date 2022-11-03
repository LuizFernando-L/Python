#Vamos desenvolver uma solução que envolve cálculo de uma compra.
def calcular_valor(valor_prod, qtd, moeda="real", desconto = None, acrescimo=None):
    v_bruto=valor_prod*qtd
    if desconto:
        v_liquido = v_bruto - (v_bruto*(desconto/100))
    elif acrescimo:
        v_liquido = v_bruto+(v_bruto*(acrescimo/100))
    else: 
        v_liquido=v_bruto
    
    if moeda == 'real':
        return v_liquido
    elif moeda == 'dolar':
        return v_liquido * 5
    elif moeda == 'euro':
        return v_liquido * 5.7
    else:
        print("Moeda não cadastrada!")
        return 0
valor_a_pagar = calcular_valor(valor_prod=32, qtd = 5, desconto = 5)
print(f'O valor final da conta é {valor_a_pagar}')
