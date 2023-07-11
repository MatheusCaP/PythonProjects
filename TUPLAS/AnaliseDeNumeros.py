numeros = (int(input('Insira um numero: ')),
           int(input('Insira outro numero: ')),
           int(input('Insira mais um numero: ')),
           int(input('Insira o ultimo numero: ')))
print(f'Você digitou os valores {numeros}')
print('=-' * 30)
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
print('=-' * 30)
if 3 in numeros:
    print(f'O valor 3 esta na posicao {numeros.index(3)}° ')
else:
    print('O valor 3 nao foi encontrado nos numeros inseridos. ')
print('=-' * 30)
print(f'Os valores pares são: ')
  
for n in numeros:
    if n % 2 == 0:
        print(n, ', ', end=' ')

#Mesmo Programa com variaveis individuais armazenadas em uma variavel composta
'''
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite mais um numero: '))
n4 = int(input('Digite o ultimo numero: '))
numeros = (n1, n2, n3, n4)
print(f'Você digitou os valores {numeros}')
'''
