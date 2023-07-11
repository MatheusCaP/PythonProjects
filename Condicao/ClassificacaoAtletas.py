#Verifica a categoria que o atleta esta classificado de acordo com sua idade
from datetime import date
data = date.today()
print(data)
print('----------------------------------')
print('Classificacao de Categorias atleticas')
print('----------------------------------')
print(' ')
#-------------------------------------------------------------------------------------------
nascimento = int(input('Qual seu ano de nascimento? '))
anoatual = date.today().year
idade = anoatual - nascimento
#-------------------------------------------------------------------------------------------
print('Quem nasceu em {} tem {} anos de idade em {}'.format(nascimento, idade, anoatual))
print(' ')
#-------------------------------------------------------------------------------------------
if(idade <= 9 ):
    print('Você está classificado na categoria MIRIM (ATÉ OS 9 ANOS DE IDADE')
elif(idade > 9 and idade <= 14):
    print('Voce esta incluso na categoria INFANTIL (9 AOS 14 ANOS DE IDADE)')
elif(idade > 14 and idade <= 19):
    print('Voce esta incluso na categoria JUNIOR (14 AOS 19 ANOS DE IDADE)')
elif(idade > 19 and idade <= 25):
    print('Voce esta incluso na categoria SENIOR (19 AOS 25 ANOS DE IDADE)')
elif(idade > 25 ):
    print('Voce esta incluso na categoria MASTER (ACIMA DE 25 ANOS DE IDADE)')
