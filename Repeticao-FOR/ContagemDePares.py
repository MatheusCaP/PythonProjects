#Conta quantos numeros pares existem ate o intervalo desejado
from time import sleep
n1 = int(input('Ate qual numero quer contar? '))
print('Os numeros pares de 1 a {} são: '.format(n1))
for c in range (1, n1 + 1):
    if c % 2 == 0:
        sleep(1)
        print(c)
