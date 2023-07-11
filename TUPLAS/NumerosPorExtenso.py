extenso = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

num = int(input('Insira um numero entre 0 e 20: '))
#Este while true serve para nao permitir que haja erros na insercao de dados
while True:
    if num < 0 or num > 20:
        num = int(input('Tente novamente. Insira um numero entre 0 e 20:  '))
    else:
        posicao = num
        print(f'O numero inserido por extenso e: {extenso[posicao]}')
        continuacao = input('Quer continuar [S/N]? ')
        if continuacao == 's':
            num = int(input('Insira outro numero entre 0 e 20: '))
        else:
            print(' ')
            print('ENCERRANDO...')
            break




