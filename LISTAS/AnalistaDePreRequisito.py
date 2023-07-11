#Programa que le quantos numeros foram inseridos e retorna a analise dos valores de acordo com os requisitos programados.
valores = list()
cont = 0
while True:
    n = int(input('Insira um numero para acrescimo na lista: '))
    valores.append(n)
    cont += 1
    continuacao = input('Quer continuar [S/N]? ')
    while continuacao not in 'SsNn':
        print('RESPOSTA INCORRETA! Tente novamente:')
        continuacao = input('Quer continuar [S/N]? ')
    if continuacao in 'Nn':
        break
valores.sort(reverse=True)
print()
print('-=-' * 25)
print(f'Voce digitou {cont} elementos. ')
print(f'Os valores em ordem decrescente são {valores} ')
if 5 in valores:
    print('O valor 5 Faz parte da lista! ')
else:
    print('O valor 5 Nao foi encontrado na lista! ')
print('-=-' * 25)

