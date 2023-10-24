from datetime import datetime


from datetime import datetime
dados = {}
dados['nome'] = input ('Digite seu nome:')
ano_nascimento = int(input('Digite seu ano de nascimento:'))
dados['idade'] = datetime.now().year - ano_nascimento
dados['ctps'] = int(input('Carteira de trabalho: (OBS: Caso não tenha = 0)'))
if dados['ctps'] != 0:
    dados['ano de contratação'] = int(input('Digite o ano da contratação:'))
    dados['salário'] = float(input('Digite seu salário:'))
    dados['Aposentadoria'] = dados['idade'] + (dados['ano de contratação'] + 35) - datetime.now().year
print(dados)