while True:
    print('*-' * 35)
    print('Pense em 4 palavras!')
    print('*-' * 35)
    palavras = (input('Insira a 1° palavra: '),
                input('Insira a 2° palavra: '),
                input('Insira a 3° palavra: '),
                input('Insira a 4° palavra: '))
    contletra = 0
    print(' ')
    verificaLetra = input('Você quer ver vogais ou consoantes? [V/C] ')
    for p in palavras:
        if verificaLetra.lower() == 'v':
            print(f'\nNa palavra {p} temos as vogais: ')
            for letra in p:
                if letra.lower() in 'aeiouãêéíôóú': #Continuacao.lower para, se entrar maiuscula, transformar em minuscula
                    print(letra, end= ' ')
        if verificaLetra.lower() == 'c':
            print(f'\nNa palavra {p} temos as consoantes: ')
            for letra in p:
                if letra.lower() in 'bcçdfghjklmnpqrstvwxyz': #Continuacao.lower para, se entrar maiuscula, transformar em minuscula
                    print(letra, end=' ')
    continuacao = input('\nQuer continuar [S/N] ? ')
    if continuacao.upper() in 'N': #Continuacao.upper para, se entrar minuscula, transformar em maiusculas
        break

