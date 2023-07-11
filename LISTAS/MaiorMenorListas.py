valores = list()
for cont in range (0, 5):
    valores.append(input(f'Insira um valor para a posicao {cont}°: '))
print('-=' * 30)
print(f'Voce digitou os valores: {valores}')
print('-=' * 30)
print(f'O MAIOR valor digitado foi: {max(valores)}, nas posic'
      f''
      f'oes ', end=' ')
for pos, v in enumerate(valores): #para cada posicao e valor da lista valores, se o valor procurado for igual ao maior valor da lista, print a posicao dele.
    if v == max(valores):
        print(f'{pos}... ', end='')
print()
print(f'O MENOR valor digitado foi: {min(valores)}, nas posicoes', end=' ')
for pos, v in enumerate(valores): #para cada posicao e valor da lista valores, se o valor procurado for igual ao menor valor da lista, print a posicao dele.
    if v == min(valores):
        print(f'{pos}... ', end='')

