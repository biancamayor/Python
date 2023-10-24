
def maior(*núm):
    cont = maior = 0
    print('Analisando os valores passados...')
    
    for valor in núm:
        print(f'{valor}', end = '')
        if cont == 0:
            maior = valor
        else:
            valor > maior
            maior = valor
        cont = cont + 1 

print(f'Foram informados {cont} valores ao todo.')
print(f'O maior valor informado foi {maior}')