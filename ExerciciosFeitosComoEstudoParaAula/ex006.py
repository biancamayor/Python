sal = float(input('Digite seu salário para saber de quanto será seu reajuste:'))
if (sal <= 280):
    aumento = 0.2

elif (sal < 700):
    aumento = 0.15

elif (sal < 1500):
    aumento = 0.1

else:
    aumento = 0.05


novo_sal = sal + sal * aumento
valor_aumento = aumento * sal

print('Salário antes do reajuste || R${}'.format(sal))
print('Porcentagem do aumento realizado: {} %'.format(aumento))
print('O novo salário é de || R${}'.format(novo_sal))
print('O valor do aumento é de || R${}'.format(valor_aumento))
