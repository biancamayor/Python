arquivo = float(input('Insira o tamanho do arquivo para download (em MB): '))
#1 MB = 8 mb
arquivo = arquivo * 8
velocidade_link = float (input('Insira a velocidade do link de internet (em mbps): '))
tempo_download = (arquivo/velocidade_link)/60
print('A velocidade de download é de: {:.2f} minutos'.format(tempo_download))