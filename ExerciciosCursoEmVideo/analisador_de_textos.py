#Pedir o nome completo da pessoa

nome = input('Digite seu nome completo:').strip()  #remove os espaços antes e depois da frase

#Mostrar o nome com todas as letras maiusculas

nome_maiusculo = nome.upper()

#O nome com todas letras minusculas

nome_minusc = nome.lower()

#A quantidade de caracteres, sem considerar os espaços

caracteres = len(nome) - nome.count(' ')  # remove espaço entre as palavras, dentro da frase.

#Quantas letras tem o primeiro nome

letras_pn = nome.find(' ')  #procura a posição do primeiro espaço, fim do primeiro nome

print('Analisando seu nome...')
print(f'''Seu nome maiúsculo é {nome_maiusculo},
Seu nome minúsculo é {nome_minusc}
A quantidade de caracteres do seu nome é de {caracteres} letras
O seu primeiro nome possuí {letras_pn} letras.''')





