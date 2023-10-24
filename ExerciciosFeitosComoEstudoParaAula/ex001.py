valor_da_conta = float(input('Qual o valor da conta?'))
qntd_de_pessoas = int(input('Digite a quantidade de pessoas na mesa:'))
valor_total = valor_da_conta * 1.1 + 10 * qntd_de_pessoas
print(f'O valor total da conta é de R$ {valor_total} reais')
