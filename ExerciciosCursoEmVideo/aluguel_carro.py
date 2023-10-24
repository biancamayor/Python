import os
os.system ('cls')

km = float(input('Digite a quantidade de km rodados com o carro:'))
dias = int (input('Digite a quantidade de dias em que o carro estará alugado:'))

vf = (km * 0.15) + (60 * dias)

print(f'O valor final a ser pago pelo aluguel do carro é de {vf} reais. ')