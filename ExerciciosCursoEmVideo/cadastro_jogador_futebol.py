jogador = {}
partidas = []
jogador['Nome'] = input('Digite o nome:')
total = int(input(f'Quantas partidas o {jogador["Nome"]} jogou?'))
for c in range (0,total):
    partidas.append(int(input(f'Quantos gols o jogador {jogador["Nome"]} fez na partida {c+1}?')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
for k, v in jogador.items():
    print(f"O campo {k} tem valor {v}.")