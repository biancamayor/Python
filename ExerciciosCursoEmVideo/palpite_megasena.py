from random import randint
cada_jogo = []
todos_jogos = []


quant = int(input('Quantos jogos eu devo sortear?'))
total = 1

while total <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in cada_jogo:
            cada_jogo.append(num)
            cont = cont + 1
        if cont >=6:
            break
    
    cada_jogo.sort()
    todos_jogos.append(cada_jogo[:])
    cada_jogo.clear()
    total = total + 1

print('=-'*3, f'SORTEANDO {quant} JOGOS', '=-'*3)
for i in range (quant):
    print(todos_jogos[i])
