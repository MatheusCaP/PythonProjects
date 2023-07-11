#Recebe um numero e exibe sua tabuada através do laço for
from time import sleep
n = int(input('Insira um numero para que retorne a sua Tabuada: '))
print('Processando...')
print('Aqui esta a tabuada do numero {}: '.format(n))
sleep(1)
for c in range (1, 10 + 1):
    tab = n * c
    print('{} X {} = {}'.format(n, c, tab))
print(' ')
print('Obrigado por utilizar a tabuada automatica :) .')
