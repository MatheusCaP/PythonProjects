#recebe seis numeros inteiros e faz a soma somente daqueles que sao pares
soma = 0
cont = 0
for c in range (1, 7):
    num = int(input('Digite um numero até que nao seja mais pedido: '))
    if (num % 2 == 0):
        soma = soma + num
        cont = cont + 1

print(' ')
print('A soma sera feita somente se os numeros forem pares. ')
print('=-=' * 20)
print('Dos numeros digitados apenas {} sao pares. \nA soma entre esses numeros e: {} '.format(cont, soma))
#-------------------------------------------------------------------

