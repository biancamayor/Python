import os
os.system('cls')

alt = float(input('Digite a altura da parede que será pintada:'))
larg = float(input('Digite a largura da parede que será pintada:'))

area = larg * alt
print(f'Área = {area} metros quadrados')

#1 litro pinta 2m^2

tinta = area/2

print(f'A quantidade de tinta necessária é de {tinta} litros.')