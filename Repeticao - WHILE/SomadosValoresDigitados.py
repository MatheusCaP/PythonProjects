#Programa que recebe varios valores ate que seja digitado 0, faz a soma desses valores e apresenta para o usuario

num = int(input('Digite um numero [000 para parar o acumulo]: '))
cont = 0
soma = num

while num != 0:
    num = int(input('Digite um numero [000 para parar o acumulo]: '))
    cont += 1
    soma += num
print('Voce digitou {} numeros e a soma entre eles foi {}'.format(cont, soma))
