#Programa que simula JOKENPO através da biblioteca Random que faz por sorteio aleatorio o PC "imaginar" 1 numero.
from random import randint
from time import sleep #Biblioteca de temporizadores
comput = randint(1, 3) #Faz o computador "Pensar" em um numero
print('{:*^40}'.format('PEDRA, PAPEL OU TESOURA'))
print('Suas opcoes sao: ')
print('[ 1 ] PEDRA')
print('[ 2 ] PAPEL')
print('[ 3 ] TESOURA')
jogada = int(input('Qual é sua jogada? '))
print('-=-' * 20)
print('JO')
sleep(1) #Comando que faz o computador esperar pela quantidade de secundos impostos nos parenteses
print('KEN')
sleep(1)
print('PO!!')
print('-=-' * 20)
#------------------------------------------------
#EMPATES
if(comput == 1 and jogada == 1):
    print('Computador jogou PEDRA \nJogador jogou PEDRA')
    print('-=-' * 20)
    print('O Jogo empatou!')
elif(comput == 2 and jogada == 2):
    print('Computador jogou PAPEL \nJogador jogou PAPEL')
    print('-=-' * 20)
    print('O Jogo empatou!')
elif(comput == 3 and jogada == 3):
    print('Computador jogou TESOURA \nJogador jogou TESOURA')
    print('-=-' * 20)
    print('O Jogo empatou!')
#------------------------------------------------
#VITORIAS E DERROTAS
if(comput == 1 and jogada == 2):
    print('Computador jogou PEDRA \nJogador jogou PAPEL')
    print('-=-' * 20)
    print('JOGADOR VENCE!!')
elif(comput == 1 and jogada == 3):
    print('Computador jogou PEDRA \nJogador jogou TESOURA')
    print('-=-' * 20)
    print('COMPUTADOR VENCE!!')
elif(comput == 2 and jogada == 1):
    print('Computador jogou PAPEL \nJogador jogou PEDRA')
    print('-=-' * 20)
    print('COMPUTADOR VENCE!!')
elif(comput == 2 and jogada == 3):
    print('Computador jogou PAPEL \nJogador jogou TESOURA')
    print('-=-' * 20)
    print('JOGADOR VENCE!!')
elif(comput == 3 and jogada == 1):
    print('Computador jogou TESOURA \nJogador jogou PEDRA')
    print('-=-' * 20)
    print('JOGADOR VENCE!!')
elif(comput == 3 and jogada == 2):
    print('Computador jogou TESOURA \nJogador jogou PAPEL')
    print('-=-' * 20)
    print('COMPUTADOR VENCE!!')

