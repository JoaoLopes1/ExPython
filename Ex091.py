from random import randint
from time import sleep
from operator import itemgetter
dados = {'Jogador 1': randint(1, 6),
         'Jogador 2': randint(1, 6),
         'Jogador 3': randint(1, 6),
         'Jogador 4': randint(1, 6)
         }
ranking = list()
print('Valores sorteados:')
for j, d in dados.items():
    print(f'O jogador{j} tirou {d} no dado.')
    sleep(0.5)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('Ranking vencedor:')
#for c in range(1, 5):
    #print(f'{c}o lugar: {ranking[c-1][0]} com {ranking[c-1][1]}')
for p, v in enumerate(ranking):
    print(f'{p+1}o lugar: {v[0]} com {v[1]} no dado.')
    sleep(0.5)