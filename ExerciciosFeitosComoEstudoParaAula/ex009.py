nota1 = float(input('Digite sua nota da prova 1:'))
nota2 = float(input('Digite sua nota da prova 2:'))
media = (nota1 + nota2)/ 2

if media <=4: 
 print("Opa! Você foi reprovado! Suas notas da prova 1 e prova 2 foram {} e {}, nessa ordem. \n Sua média foi {} e seu conceito foi 'E'".format(nota1, nota2, media))


if media >= 9 and media <= 10 :
    print("Parabéns! Você foi aprovado com nota máxima! Suas notas da prova 1 e prova 2 foram {} e {}, nessa ordem. \n Sua média foi {} e seu conceito foi 'A'".format(nota1, nota2, media))

elif media >= 7.5 and media <=9 :
    print("Parabéns! Você foi aprovado! Suas notas da prova 1 e prova 2 foram {} e {}, nessa ordem. \n Sua média foi {} e seu conceito foi 'B'".format(nota1, nota2, media))

elif media >= 6 and media <=7.5:
    print("Parabéns! Você foi aprovado! Suas notas da prova 1 e prova 2 foram {} e {}, nessa ordem. \n Sua média foi {} e seu conceito foi 'C'".format(nota1, nota2, media))

elif media <= 6 and media >=4:
    print("Opa! Você foi reprovado! Suas notas da prova 1 e prova 2 foram {} e {}, nessa ordem. \n Sua média foi {} e seu conceito foi 'D'".format(nota1, nota2, media))

else:
    print("Opa! Você foi reprovado! Suas notas da prova 1 e prova 2 foram {} e {}, nessa ordem. \n Sua média foi {} e seu conceito foi 'E'".format(nota1, nota2, media))
 
   