cont = 0
dados = list()
pessoas = list()
while True:
    dados.append(input('NOME: '))
    dados.append(float(input('PESO: ')))
    cont += 1
    if len(pessoas) == 0:
        maiorP = dados[1]
        menorP = dados[1]
    else:
        if dados[1] > maiorP:
            maiorP = dados[1]
        elif dados[1] < menorP:
            menorP = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    continuacao = input('Quer continuar [S/N]? ')
    if continuacao in 'Nn':
        print('***' * 15)
        print(f'Foram cadastradas (pessoa/peso): {pessoas}')
        print('***' * 15)
        print(f'Ao todo você cadastrou {cont} pessoas.')
        print(f'O maior p'
              f''
              f'eso é: {maiorP}')
        print(f'O menor peso e: {menorP}')
        break





