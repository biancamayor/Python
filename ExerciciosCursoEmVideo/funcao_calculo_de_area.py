def area(larg,comp):
    a = larg * comp
    print(f'A área do terreno {larg:,.1f}x{comp:,.1f} é de {a:,.1f}m2.')

l = float(input('Por favor, insira a largura do terreno (m):'))

c = float(input('Por favor, insira o comprimento do terreno (m):'))

area(l,c)