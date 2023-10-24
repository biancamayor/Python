import os
os.system('cls')

pares = 0
impares = 0

for i in range (10):
    if int(input('Digite um número inteiro:')) % 2 == 0: 
        pares = pares + 1
    
    else:
        impares = impares + 1

print('A quantidade de números ímpares é de: {}\n A quantidade de números pares é de: {}'.format(impares, pares))


