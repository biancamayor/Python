#Pedir o nome do aluno
#pedir a média
#salvar também a situação do aluno
#salvar todas as informações em um dicionário
#exibir na tela

alunos = {'nome':'', 'media':'', 'situação': ''}
alunos['nome'] = input ('Insira seu nome:')
alunos['media'] = float(input('Digite sua média:'))
if alunos['media'] >= 6:
    alunos['situação'] = 'Aprovado'
else:
    alunos['situação'] = 'Reprovado'

print(alunos)
