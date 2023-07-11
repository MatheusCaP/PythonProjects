a = [2, 3, 4, 7, 8]
'''
 (b = a) ---> Quando igualamos listas dessa forma, nos nao criamos copias e sim fazemos uma paridade entre as listas
onde tudo que for mudado na lista b sera mudado na lista A e vice e versa. Por isso quando queremos criar copias,
precisamos usar o b = a[:], para copiar todos os valores da lista, e nao fazer uma paridade. Assim poderemos alterar
uma, sem alterar a outra.
'''

b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')