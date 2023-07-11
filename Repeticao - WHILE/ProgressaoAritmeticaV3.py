#exibe os 10 primeiros termos de uma progressao aritmetica de acordo com o primeiro termo e a razao informada pelo usuario
#Com opcao de escolha de quantos termos o usuario precisa
pt = int(input('Insira o primeiro termo para a progressao aritmetica: '))
razao = int(input('Insira a razao de intervalo entre os termos: '))
cont = 0
print(' ')
print('Dado o primeiro termo ({}) e a razao ({}) aqui estao os 10 primeiros termos desta progressao'.format(pt, razao))
quant = 10
novon = 0 #Novo numero
while quant != 0:
    novon += quant
    while cont != novon:
        print('{}'.format(pt), end=' -> ')
        pt += razao
        cont += 1
    print(' PAUSA ')
    quant = int(input('Quantos termos voce precisa A MAIS nesta progressao? '))

