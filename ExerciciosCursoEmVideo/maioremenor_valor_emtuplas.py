from random import randint
tupla = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

organizado = (sorted(tupla))

print(f'Os valores gerados foram: {tupla}')
print(f'O menor valor sorteado foi {organizado[0]}.')
print(f'O maior valor sorteado foi {organizado[4]}.')