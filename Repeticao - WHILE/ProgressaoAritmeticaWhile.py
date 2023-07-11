#exibe os 10 primeiros termos de uma progressao aritmetica de acordo com o primeiro termo e a razao informada pelo usuario. versao WHILE
pt = int(input('Insira o primeiro Termo desejado para progressao: '))
razao = int(input('Insira a razao de intervalo de saltos para progressao: '))
dect = pt + (10 - 1) * razao #Formula matematica para progressao aritmetica
print('Dado o primeiro termo ({}) e a razao ({}) o resultado da progressao aritmetica e: '.format(pt, razao))
while pt != (dect + razao):
    print('{} '.format(pt), end=' -> ')
    pt += razao
print('FIM DA PROGRESSAO')