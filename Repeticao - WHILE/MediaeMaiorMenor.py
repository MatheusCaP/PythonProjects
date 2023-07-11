#Programa que recebe numeros do usuario, faz a media entre eles e diz qual foi o maior digitado e o menor digitado.
num = float(input('Digite um numero: '))
cont = 1
media = 0
resposta = input('Quer continuar [S/N]?  ')
soma = num
maior = num
menor = num
while resposta == 's' or resposta == 'S':
    num = float(input('Digite um numero: '))
    cont += 1
    soma += num
    media = (media + soma) / cont
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    resposta = input('Quer continuar [S/N]? ')
print('Você digitou {} numeros. \nA media entre eles e: {}.'.format(cont, media))
print('O maior numero inserido foi {}, e o menor numero inserido foi {}'.format(maior, menor))
