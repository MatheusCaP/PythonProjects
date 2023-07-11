#Jogo que simula o impar ou par atraves de um valor sorteado pelo computador onde o algoritmo compara
# a entrada do usuario com o valor sorteado e diz quem ganhou. Se ganhar continua acaba
from random import randint
pc = randint(0, 10)
print('-=-' * 20)
print('JOGO DO IMPAR OU PAR ')
print('Ganhe o maximo que puder, se perder acaba.')
print('-=-' * 20)
num = 0
jogada = 0
print('~' * 20)
contvitoria = 0
contderrota = 0
while True:
    num = int(input('Insira um valor de acordo com os dedos das mãos (ate 10): '))
    jogada = input('PAR OU IMPAR [P/I]? '.upper())
    result = num + pc #soma do pc + jogador pra saber se é par ou Impar.
    if result % 2 == 0:
        print(f'Voce jogou {num} e o computador jogou {pc}. Total de {result}, DEU PAR')
    else:
        print(f'Voce jogou {num} e o computador jogou {pc}. Total de {result}, DEU IMPAR')
    if jogada == 'P' and result % 2 == 0:
        print('~' * 20)
        print('Você Ganhou!!')
        print('~' * 20)
        contvitoria += 1
    elif jogada == 'I' and result % 2 != 0:
        print('~' * 20)
        print('Você Ganhou!!')
        print('~' * 20)
        contvitoria += 1
    elif jogada == 'P' and result % 2 != 0:
        print('~' * 20)
        print('Você Perdeu!!')
        print('~' * 20)
        contderrota += 1
    elif jogada == 'I' and result % 2 == 0:
        print('~' * 20)
        print('Você Perdeu!!')
        print('~' * 20)
        contderrota += 1
    if contderrota == 1:
        print(f'GAME OVER! Voce venceu {contvitoria} vezes')
        break
