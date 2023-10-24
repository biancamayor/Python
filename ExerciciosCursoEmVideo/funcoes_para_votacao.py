from datetime import datetime

def votacao(ano):
    idade = datetime.today().year - ano 
    if idade < 16:
        print('Voto negado!')

    elif idade >= 16 and idade <18 or idade > 65:
        print('Voto opcional!')
    
    elif idade >= 18:
        print('Voto obrigatório!')

    

ano_nascimento = int(input('Digite seu ano de nascimento:'))
votacao(ano_nascimento)