#1 - diigitar os numeros por extenso na tupla
#2 - pedir ao usuario um valor
#3 - definir os limites do valor e mensagem de erro
#4 - imprimir o valor por extenso (0 - 20)

extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:     
    num = int(input('Digite um número entre 0 e 20:'))
    if 0<= num <=20:
        break
    print('Tente novamente. ', end='')

print(f'Você digitou o número {extenso [num]}.')
