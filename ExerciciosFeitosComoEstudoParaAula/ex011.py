
dinheiro_por_hora = float(input('Quanto você ganha por hora?'))
horas_trab = int(input('Quantas horas você trabalha no mês?'))
salario_bruto = dinheiro_por_hora * horas_trab
inss = salario_bruto * 0.08 #desconto do salario para o inss
ir = salario_bruto * 0.11 #desconto do salario para o imposto de renda
sindicato = salario_bruto * 0.05 #desconto do salario para o sindicato
salario_liquido = salario_bruto - inss - ir - sindicato

print('Seu salário líquido é de || R$ {}'.format(salario_liquido),
'\n Seu salário bruto é de || R$ {}'.format(salario_bruto),
'\n O valor pago para o inss foi de || R$ {}'.format(inss),
'\n O valor descontado para o imposto de renda foi de || R$ {}'.format(ir),
'\n O valor pago para o sindicato foi de || R$ {}'.format(sindicato))
