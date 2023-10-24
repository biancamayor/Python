
import os
os.system('cls')

n = int(input('Insira quantos termos você deseja ver na sequência de Fibonacci:'))

t1 = 0
t2 = 1 #seuqência começa no 0 e o segundo termo é o 1

cont = 3 #começa no terceiro termo pois já sabemos os 2 primeiros

print('{} -> {} -> '.format(t1, t2), end='')

while :
    t3 = t1 + t2
    if t3 == 500: 
        break
    print('{} -> '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont = cont + 1 #para testar o próximo número
