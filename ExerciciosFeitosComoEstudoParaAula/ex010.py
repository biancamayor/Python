a = float(input('Digite o valor do lado 1 do triângulo:'))
b = float(input('Digite o valor do lado 2 do triângulo:'))
c = float(input('Digite o valor do lado 3 do triângulo:'))
 
while (a + b < c) or (b + c < a) or (a + c < b):
    print('Os valores digitados não constituem um triângulo. Por favor, digite outros valores para os lados')
    a = float(input('Digite o valor do lado 1 do triângulo:'))
    b = float(input('Digite o valor do lado 2 do triângulo:'))
    c = float(input('Digite o valor do lado 3 do triângulo:'))

if (a==b) and (b==c):
    print('Triângulo equilátero')

elif (a==b) or (a==c) or (b==c):
    print('Triângulo isósceles')

else:
    print('Triângulo escaleno')