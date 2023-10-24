import os
os.system('cls')

reais = float(input('Digite quantos reais você tem em sua carteira:'))
dol = reais/3.27 
print('Você tem {:.2f} dólares.'.format(dol))