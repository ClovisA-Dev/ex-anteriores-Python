from time import sleep
def esc():
    print('=-' * 30)


def contador():
    esc()
    print('Contagem de 1 até 10 de 1 em 1')
    esc()
    for c in range(1, 11):
        print(c, end=' '), sleep(0.5)
    sleep(0.5)
    print('FIM')
    sleep(0.5)
    esc()
    print('Contagem de 10 até 0 de 2 em 2')
    esc()
    for d in range(10, -1, -2):
        print(d, end=' '), sleep(0.5)
    sleep(0.5)
    print('FIM')
    esc()
    print('Agora é sua vez de personalizar a contagem! ')
    inicio = int(input('Início: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    for e in range(inicio, fim, passo):
        print(e, end=' ')
        sleep(0.5)
    sleep(0.5)
    print('FIM')
esc()
contador()