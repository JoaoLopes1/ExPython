def notas():
    """
    Recebe Nota;
    Adiciona no dicionário;
    Adicona na lista;
    Limpa o dicionário;
    Repete;
    Pergunta situação;
    Faz a verificação;
    Mostra Situação de cada nota;
    :return: Dados sobre as notas;
    """
    while True:
        dados['Nota'] = int(input('Notas:'))
        bd.append(dados['Nota'])
        dados.clear()
        verifica = str(input('Continuar: [S/N]')).strip().upper()
        if verifica in 'NNAONÃO':
            break
    situacao = str(input('Deseja mostrar a situação para cada nota: [S/N]')).strip().upper()
    if situacao in 'SSIM':
        for c in range(0, len(bd)):
            if bd[c] <= 5:
                print(f'A nota {bd[c]} te deixa de REPROVADO.')
            if 5 < bd[c] < 7:
                print(f'A nota {bd[c]} te deixa de RECUPERAÇÃO.')
            if bd[c] >= 7:
                print(f'A nota {bd[c]} te deixa APROVADO.')
    return (print(f'A quantidade de notas digitadas foi {len(bd)}'),
            print(f'A média da turma foi {(sum(bd)/(len(bd))):.2f}.'),
            print(f'A nota mais alta da turma foi {max(bd)}'),
            print(f'A menor nota da turma foi {min(bd)}')
            )


dados = dict()
bd = list()
notas()
print(bd)