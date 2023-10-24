
def contador(inicio, fim, passo):
    if passo < 0:
        passo = passo * (-1)
    if passo == 0: 
        passo = 1
    
    print(f'A contagem de {inicio} até {fim} de {passo} em {passo}:')

    if (inicio < fim):
        cont = inicio
        while cont <= fim:
            print(f'{cont}')
            cont = cont + passo
    else:
        cont = inicio
        while (cont >= fim):
            print(f"{cont}")
            cont = cont - passo

contador(1,10,1)  
contador(10, 0, 2)

print(f'Agora é sua vez de personalizar o contador:')
i = int(input('Digite o valor inicial:'))
f = int(input('Digite o valor final:'))
p = int(input('Digite o passo:'))

contador(i, f, p)
