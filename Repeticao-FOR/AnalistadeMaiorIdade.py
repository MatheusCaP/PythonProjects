#Programa que recebe 7 idades e identifica quantos sao maiores e menores de idade
from datetime import date
data = date.today()
anoatual = date.today().year
contmaior = 0
contmenor = 0

#--------------------------------------------------------------------------------
for c in range (1, 8, 1):
    ano = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    if(ano == 0):
        print('Erro de insercao de dados, tente novamente')
        exit()
    idade = anoatual - ano
    if (idade < 18):
        contmenor = contmenor + 1
    elif (idade >= 18):
        contmaior = contmaior + 1

print('+-+' * 30)
print('Ao total foram cadastradas:\n{} Pessoas Maiores de Idade \n{} pessoas menores de idade'.format(contmaior, contmenor))
print('+-+' * 30)
