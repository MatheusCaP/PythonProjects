#Programa que apresenta a sequencia de FIBONACCI de acordo com o numero de termos pedido pelo usuario
print('-' * 30)
print('SEQUENCIA DE FIBONACCI')
print('-' * 30)
print(' ')
ntermos = int(input('Quantos termos voce precisa? '))
print('~' * 30)
t1 = 0
t2 = 1
#tprox = (t1 - 1) + (t2 - 2)
cont = 3
tprox = 0
print('{} -> {}'.format(t1, t2), end= '')
while cont <= ntermos:
    tprox = t1 + t2
    t1 = t2
    t2 = tprox
    cont += 1
    print(' -> {} '.format(tprox), end= '')
print('FIM')


