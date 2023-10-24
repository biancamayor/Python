from random import randint
from operator import itemgetter

jogo = {'Jogador1': randint(1,6), 
        'Jogador2': randint(1,6),
        'Jogador3': randint(1,6),
        'Jogador4': randint(1,6)}

for k,v in jogo.items():
    print(f'O {k} tirou o número {v} no dado.')

ranking = {}
ranking = sorted(jogo.items(), key = itemgetter(1))
print(ranking)
print('O vencedor é:', ranking[3][0])