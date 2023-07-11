#Programa que recebe nome, idade e sexo e compara essas informações entre os dados recebidos.
hmaisv = 0
mabaixo20a = 0 #Contador de mulheres abaixo dos 20 anos
for c in range (1, 5, 1):
    print('----- {} PESSOA -----'.format(c))
    nome = input('NOME: ')
    idade = int(input('IDADE: '))
    sexo = input('SEXO [m/f]: ')
    #condicao de idade dentro do loop
    if (c == 1):
        idade1 = idade
    elif (c == 2):
        idade2 = idade
    elif (c == 3):
        idade3 = idade
    elif (c == 4):
        idade4 = idade
     #condicao de homem mais velho dentro do loop
    if (c == 1 and sexo == 'm'):
        hmaisv = idade
        nhmaisv = nome
    if (sexo == 'm' and idade > hmaisv):
        hmaisv = idade
        nhmaisv = nome
     #condicao de mulheres abaixo de 20 anos dentro do loop
    if (idade < 20 and sexo == 'f' ):
        mabaixo20a = mabaixo20a + 1

media = (idade1 + idade2 + idade3 + idade4) / 4
print('A media de idade do grupo e de {} anos'.format(media))
print('O homem mais velho do grupo tem {} anos e se chama {}. '.format(hmaisv, nhmaisv))
print('Neste grupo existem {} mulheres com menos de 20 anos.'.format(mabaixo20a))