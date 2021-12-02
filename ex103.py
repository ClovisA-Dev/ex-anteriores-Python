def ficha(a, b):
    if a == '':
        a = '<desconhecido>'
    if b == '':
        b = 0
    return f'O jogador {a} fez {b} gol(s) no campeonato. '


# Programa Principal
nome = str(input('Nome do Jogador: ')).strip().capitalize()
gols = int(input('Número de Gols: '))
print(ficha(nome, gols))
