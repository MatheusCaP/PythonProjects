#Progama que le o peso de 5 pessoas e avalia qual e mais pesado e qual e mais leve
for c in range (1, 6, 1):
    peso = float(input('Insira o peso da {}° Pessoa: '.format(c)))
    if (c == 1):
        menorpeso = peso
        maiorpeso = peso
    elif (peso > maiorpeso):
        maiorpeso = peso
    elif (peso < menorpeso):
        menorpeso = peso

print('O maior peso lido foi de {} kg'.format(maiorpeso))
print('O menor peso lido foi de {} kg'.format(menorpeso))