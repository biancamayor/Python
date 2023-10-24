pessoas = {}
galera = []
soma = media = 0

while True:
    pessoas.clear()
    pessoas['nome'] = input('Digite seu nome: ')

    while True:
        pessoas['sexo'] = input('Digite seu sexo (M/F): ').upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        else:
            print('Por favor, digite um sexo válido, M ou F!')
    pessoas['idade'] = int(input('Digite sua idade: '))
    soma = soma + pessoas['idade']

    galera.append(pessoas.copy())

    while True:
        resp = input('Quer continuar? [S/N]').upper()[0]
        if resp in 'SN':
            break
        print('Erro! Digite apenas S/N.')
    if resp == 'N':
        break

media = soma/len(galera)

print(galera)
print(f'Ao todo temos {len(galera)} pessoas cadastradas!')
print(f'A média de idades é de {media: 5.2f} anos.')
print('As mulheres cadastradas foram:', end='' )
for p in galera:
    if p['sexo'] == 'F':   
        print(f'{p["nome"]}', end ='')

print('Pessoas com idade acima da média: ')
for p in galera:
    if p['idade'] > media:
        print(f'{p["nome"]}', end='')
        