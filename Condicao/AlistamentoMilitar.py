#Verifica se é do sexo masculino ou feminino e avalia data de alistamento

print('----------------------------------')
print('Consulta de alistamento militar')
print('----------------------------------')
print(' ')
#Definicao de variaveis

#Para pegar a data do sistema é necessario importar a biblioteca datetime, e coloca-la na seguinte sintaxe:
from datetime import date
anoatual = date.today().year


#Verificacao de sexo
sexo = int(input('Qual seu sexo? \nInsira: 1 {Masculino} OU 2 {Feminino} '))
if(sexo == 2):
    print('Por ser do sexo feminino seu servico militar nao e obrigatorio. ')
    print('FINALIZANDO...')
    exit()


nascimento = int(input('Insira seu ano de nascimento: '))
idade = anoatual - nascimento
menordeidade = 18 - idade
maiordeidade = idade - 18
anoalistamento = nascimento + 18

#Manipulacao de variaveis
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, anoatual))

#processamento de variaveis
if( idade == 18 ):
    print('Voce deve se alistar esse ano!')
    print('Seu ano de alistamento é: {}'.format(anoalistamento))
else:
    if ( idade < 18 ):
        print('Ainda faltam {} anos para o seu alistamento militar.'.format(menordeidade))
        print('Seu alistamento será em {} '.format(anoalistamento))
    else:
        if (idade >18):
            print('Voce ja deveria ter se alistado há {} ano(s)'.format(maiordeidade))
            print('Seu alistamento foi em {}'.format(anoalistamento))



