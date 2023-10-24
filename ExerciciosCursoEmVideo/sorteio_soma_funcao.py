from random import randint

def sorteia(lista):
    for cont in range(0,5):
        n = randint(0,10)
        lista.append(n)



def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma = soma + valor
    print(f'Somando os valores da lista {lista}, temos {soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)
