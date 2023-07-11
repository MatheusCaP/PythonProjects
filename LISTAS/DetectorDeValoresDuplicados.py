#Recebe numeros e nao deixa a entrada ser repetida, no final os valores unicos deverao ser apresentados em ordem crescente.
valores = list()
while True:
    n = int(input('Insira um numero para completar sua lista: '))
    if n not in valores:
        valores.append(n)
        print('=-=' * 15)
        print('Valor adicionado a lista com sucesso...')
        print('=-=' * 15)
    else:
        print('=-=' * 15)
        print('ESTE VALOR JA FOI INSERIDO E NAO PODE SER INSERIDO NOVAMENTE!')
        print('=-=' * 15)
    continuacao = input('Quer continuar? [S/N]: ')
    while continuacao not in 'SsNn':
        print('Resposta inválida!')
        continuacao = input('Quer continuar? [S/N]: ')
    if continuacao in 'Nn':
        break
valores.sort()
print()
print('--' * 35)
print(f'Os valores que foram registrados para a formacao da lista foram:\n{valores}')
print('--' * 35)