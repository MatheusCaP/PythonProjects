#exibe os 10 primeiros termos de uma progressao aritmetica de acordo com o primeiro termo e a razao informada pelo usuario.
pt = int(input('Insira o primeiro termo desejado para progressao: '))
razao = int(input('Insira a razao do intervalo entre os termos da progressao (Nao pode ser Zero): '))
dect = pt + (10 - 1) * razao #FORMULA DA PROGRESSAO ARITMETICA PARA CHEGAR ATE O TERMO QUE QUEREMOS, NO CASO, 10.
print('Dado o primeiro termo ({}), e a razao desejada ({}) este e o resultado da progressao: '.format(pt, razao))
for c in range(pt, dect + razao, razao):#ADICAO DE DECIMO TERMO + RAZAO PORQUE O PYTHON SUBTRAI 1, LOGO PRECISAMOS QUE ELE ANDE MAIS UM NUMERO PARA ALCANÇARMOS OS 10 TERMOS.
    print('{} '.format(c), end= ' -> ')
print('FIM DA PROGRESSAO')