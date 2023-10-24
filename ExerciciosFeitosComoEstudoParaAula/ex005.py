import os
os.system ('cls')

resp = 's'
maior = menor = quantidade_numeros = soma = 0
while resp in 's':
    n = int(input('Digite um número:'))
    quantidade_numeros = quantidade_numeros + 1
    soma = soma + n

    if(quantidade_numeros == 1):
        maior = menor = n

    elif (n > maior):
        maior = n

    elif (n < menor):
        menor = n   
    resp = input('Quer continuar? [s/n]: ').lower()[0]
    
media = soma/quantidade_numeros
print(f'Maior valor: {maior},\n menor valor: {menor},\n media: {media}')
