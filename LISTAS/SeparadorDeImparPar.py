valores = list()
impares = list()
pares = list()
while True:
    valores.append(int(input('Insira um numero para conclusao da lista: ')))
    print('-=-' * 15)
    print('Valor Adicionado com Sucesso! ')
    print('-=-' * 15)
    continuacao = input('Quer continuar [S/N]? ')
    while continuacao not in 'SsNn':
        print('RESPOSTA INCORRETA! Tente novamente')
        continuacao = input('Quer continuar [S/N]? ')
    print('~~~' * 15)
    if continuacao in 'Nn':
        break
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('***' * 15)
print(f'A lista completa e: {valores}')
print(f'A lista com numeros Pares e: {pares}')
print(f'A lista com numeros impares e: {impares}')
