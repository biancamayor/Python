matriz = [[0, 0, 0], 
          [0, 0, 0],
          [0, 0, 0]]
somapar = somacoluna3 = slinha2 =  0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}{c}]: '))

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]: ^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar = somapar + matriz[l][c]
    print()

for c in range(0,3):
    slinha2 = slinha2 + matriz[1][c]

    
for l in range(0,3):
    somacoluna3 = somacoluna3 + matriz[l][2]

print(f'Soma dos valores pares = {somapar}')
print(f'Soma dos valores na linha 2 = {slinha2}')
print(f'Soma dos valores na coluna 3 = {somacoluna3}')
