valores = list()
for cont in range(0, 5):
    valores.append(int(input('Insira um valor: '))) #Append serve para adicionar dados a lista, e é possivel coloca-lo como input

for c, v in enumerate(valores):
    print(f'Na posicao {c} encontrei o valor {v}! ')
print('Cheguei ao final da lista. ')
