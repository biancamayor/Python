import os
os.system('cls')

horas = int(input('Digite o número de horas trabalhadas:'))
valor = float(input('Digite o valor ganho por hora de trabalho:'))
sal_bruto = horas * valor 
sindicato = sal_bruto * 0.03
fgts = sal_bruto * 0.11

if (sal_bruto <= 900):
    desc = 0

elif (sal_bruto <= 1500):
    desc = 0.05

elif (sal_bruto <= 2500):
    desc = 0.10

else:
    desc = 0.20  

ir = sal_bruto * desc
sal_liquido = sal_bruto - sindicato - ir
total_descontos = ir + sindicato 

print('Salár(io bruto: {} * {} = R$ {}'.format(horas, valor, sal_bruto))
print('- ir ({}) = R$ {}'.format(desc, ir))
print('- sindicato (0.03) = R$ {}'.format(sindicato))
print('fgts (11%) = R$ {}'.format(fgts))
print('Total de descontos = R$ {} '.format(total_descontos))
print('Salário líquido = R$ {}'.format(sal_liquido))

