from datetime import date
def voto(ano):
    anoatual = date.today().year
    idade = anoatual - ano
    voto = print(f'Com {idade} anos: ',end='')
    if idade <= 17:
        print('NÃO VOTA.')
    elif idade >= 18 and idade <= 59:
        print('VOTO OBRIGATÓRIO!')
    elif idade >= 60:
        print('VOTO OPCIONAL!')


print('-'*20)
nasc = int(input('Em que ano que você nasceu? '))
print(voto(nasc))









