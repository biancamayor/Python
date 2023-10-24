import os
os.system('cls')

n = int(input('Digite um número para ver a sua tabuada:'))

for i in range (1, 11):
   print('{} * {} = {}'.format(i, n, i*n))