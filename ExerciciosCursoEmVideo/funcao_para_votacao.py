import os
os.system('cls')

def voto(ano):
    from datetime import date

    atual = date.today().year
    idade = atual - ano 

    if idade < 16:
        print(f'Você tem {idade} anos. Voto negado')
    elif 16 <= idade < 18 or idade>65 :
        print(f'Você tem {idade} anos. Voto opcional.')
    else:
        print(f'Você tem {idade} anos. Voto obrigatório')

a = int(input('Digite seu ano de nascimento:'))

voto(a)
