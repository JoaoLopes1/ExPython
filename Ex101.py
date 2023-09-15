from datetime import date
def voto(nascimento):
    if 16 <= idade < 18 or idade >= 70:
        return 'Opcional'
    elif 18 <= idade < 70:
        return 'Obrigatório'
    else:
        return 'Negado'


while True:
    ano = int(input('Digite um ano:'))
    idade = date.today().year - ano
    print(f'A pessoa que nasceu no ano {ano} tem {idade} anos e tem o voto {voto(ano)}')
    print('==='*20)
    d = str(input('Deseja continuar: [S/N]')).strip().upper()
    if d in 'NNAONÃO':
        break
print(f'{"FIM":=^40}')