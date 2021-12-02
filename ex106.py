from time import sleep
def mini_sistema():
    sleep(1)
    print('\033[7;32;40m~'*30)
    print('\033[7;32;40mSISTEMA DE AJUDA PyHELP')
    print('\033[7;32;40m~' * 30)
    print('\033[m')
    while True:
        funcao = str(input('Função ou Biblioteca > '))
        if funcao != 'fim':
            sleep(1)
            print('\033[0;30;45m')
            help(funcao)
            print('\033[m')
            sleep(1)
        if funcao.upper() == 'FIM':
            sleep(1)
            print('\033[0;30;41mATÉ LOGO!')
            break


mini_sistema()
