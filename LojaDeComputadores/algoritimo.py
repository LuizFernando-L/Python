#uma loja de informática recebeu componentes usados de um computador
# para avaliar se estão com defeito. As peças que não estiverem
# com defeito podem ser colocadas à venda.
# Como, então, podemos criar uma solução em Python para resolver esse problema?
def creat_report():
    componentes_verificados = set(['caixas de som', ' coole', 'dissipador de calor', 'CPU', 'HD', 'establizador', 'gabinete'
                                   'hub', 'impressora', 'joystick', 'memória ram', 'microfone', 'modem',  'monitor', 'mouse',
                                   'no-break', 'placa de captura', 'placa de som', 'placa de vídeo', 'placa mãe', 'scanner',
                                   'teclado', 'webcam' ])
    componentes_com_defeito = set(['hd', 'monitor', 'placa de som', 'scanner'])
    qtde_componentes_verificados = len(componentes_verificados)
    qtde_componentes_com_defeito = len(componentes_com_defeito)
    componente_ok = componentes_verificados.difference(componentes_com_defeito)
    print(f"Foram verificado {qtde_componentes_verificados} componentes \n")
    print(f"{qtde_componentes_com_defeito} componenetes apresentaram defeitos. \n")
    print("Os componentes que podem ser vendidos são: ")
    for item in componente_ok:
        print(item)
creat_report()