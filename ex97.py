def escreva():
    quant = 0
    pos = 0
    palavras = ['Gustavo Guanabara', 'Curso de Python no Youtube', 'CeV']
    for c in palavras:
        quant = len(palavras[pos]) + 4
        print('~' * quant)
        print(f'  {palavras[pos]}')
        print('~' * quant)
        pos += 1



escreva()
