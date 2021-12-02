def valores():
    v1 = float(input('LARGURA(m): '))
    v2 = float(input('COMPRIMENTO(m): '))
    tot = v1 * v2
    print(f'A área de um terreno {v1:.1f}x{v2:.1f} é de {tot:.1f}m².')


print('Controle de terrenos')
print('-'*20)
valores()
