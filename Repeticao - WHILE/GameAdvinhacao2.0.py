#Jogo que voce tenta advinhar em qual numero o pc "pensou"
#com a melhoria de caso errar ele da mais tentativas e dicas para voce acertar contabilizando o numero de tentativas que foi executado
from random import randint
print(' ')
print('Acabei de pensar em um numero entre 0 e 10. Voce consegue advinhar qual foi? ')
comput = randint(0, 10)
tentativa = int(input('Qual seu palpite? '))
contTentativa = 1
while tentativa != comput:
    contTentativa = contTentativa + 1
    if tentativa < comput:
        print('Um pouco mais... tente novamente')
        tentativa = int(input('Qual seu palpite? '))
    elif tentativa > comput:
        print('Um pouco menos... Tente novamente')
        tentativa = int(input('Qual seu palpite? '))

if contTentativa == 1:
    print('UAU! Você acertou de primeira!')
else:
    print('Acertou com {} tentativas! Parabens. '.format(contTentativa))