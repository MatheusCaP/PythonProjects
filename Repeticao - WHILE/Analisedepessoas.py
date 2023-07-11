#recebe idade e sexo de pessoas ate que o usuario nao queira mais e retorna informacoes sobre o grupo cadastrado.
idade = 0
sexo = 0
continuacao = 0
contmais18 = 0
conthomem = 0
contmulhermenos20 = 0

while True:
    if idade >= 18:
        contmais18 += 1
    if sexo == 'm':
        conthomem += 1
    if sexo == 'f' and idade < 20:
        contmulhermenos20 += 1
    print('=' * 25)
    print('CADASTRE UMA PESSOA')
    print('=' * 25)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    print('~' * 25)
    continuacao = str(input('Quer continuar? [S/N] '))
    print('~' * 25)
    if continuacao == 'n':
        print(f'O total de pessoas com mais de 18 anos e: {contmais18}')
        print(f'Ao todo temos {conthomem} homens cadastrados')
        print(f'Temos {contmulhermenos20} mulheres com menos de 20 anos ')
        break