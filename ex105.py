def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n:uma ou mais notas dos alunos (aceita várias).
    :param sit:valor opcional, indincando se deve ou não adicionar a situação.
    :return:dicionário com vários informações da turma.
    """
    print('-' * 30)
    aluno = dict()
    aluno['total'] = len(n)
    aluno['maior'] = max(n)
    aluno['menor'] = min(n)
    aluno['média'] = sum(n) / len(n)
    if sit:
        if aluno['média'] <= 6.00:
            aluno['situação'] = 'RECUPERAÇÃO'
        elif aluno['média'] >= 7.00:
            aluno['situação'] = 'BOA'
        else:
            aluno['situação'] = 'RAZOÁVEL'
    return aluno


# Programa Principal
resp = notas(1, 5, 10, 10, sit=True)
print(resp)
help(notas)



