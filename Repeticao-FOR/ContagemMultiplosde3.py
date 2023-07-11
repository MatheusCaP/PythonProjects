#Conta quantos multiplos de 3 impares existem ate o intervalo desejado
from time import sleep
cont = 0
soma = 0
n = int(input('Ate qual numero sera o intervalo de soma? '))
print('Os numeros impares multiplos de 3, de 1 a {} são: '.format(n))
print('Processando...')
sleep(1.5)
for c in range (1, n + 1):
    if c % 3 == 0:
        if c % 2 == 1:
            cont = cont + 1
            soma = soma + c
print('A soma dos {} valores solicitados é de: {} '.format(cont, soma))
