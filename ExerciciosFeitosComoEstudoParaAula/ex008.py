import os
os.system('cls')

n = int(input('Digite um número de 0 a 10 para ver sua tabuada:'))
for i in range (0,11):
    resultado = i * n
    print('{} * {} = {}'.format(n, i, resultado ))


