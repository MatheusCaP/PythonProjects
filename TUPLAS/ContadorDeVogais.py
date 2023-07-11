while True:
    print('*-' * 35)
    print('Pense em 4 palavras!')
    print('*-' * 35)
    palavras = (input(('Insira a 1° palavra: ')),
                input('Insira a 2° palavra: '),
                input('Insira a 3° palavra: '),
                input('Insira a 4° palavra: '))
    print(' ')
    for p in palavras:
        print(f'\nNa palavra {p} temos as vogais: ', end='')
        for letra in p:
            if letra.lower() in 'aeiou': #Continuacao.lower para, se entrar maiuscula, transformar em minuscula
                print(letra, end=' ')
    continuacao = input('\nQuer continuar [S/N] ? ')
    if continuacao.upper() in 'N': #Continuacao.upper para, se entrar minuscula, transformar em maiusculas
        break
