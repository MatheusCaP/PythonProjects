#Programa que recebe dois numeros e pergunta qual operacao voce quer fazer
n1 = int(input('Insira o primeiro numero: '))
n2 = int(input('Insira o segundo numero: '))
print(' ')
print('Suas opcoes sao: ')
print('[1] SOMAR \n[2] SUBTRAIR \n[3] MULTIPLICAR \n[4] DIVIDIR \n[5] QUAL E O MAIOR \n[6] INSERIR NOVOS DADOS [8] SAIR DO PROGRAMA')
opcao = int(input('O que deseja? '))


while opcao != 8:
    if opcao == 1:#SOMA
        soma = n1 + n2
        print('*' * 30)
        print('Você escolheu SOMA')
        print('=-=' * 30)
        print('A soma entre {} e {} e igual a: {}'.format(n1, n2, soma))
        print('=-=' * 30)
        print('Pressione 7 para mostrar novamente as opcoes')
        opcao = int(input('O que deseja agora? '))

    elif opcao == 2:#SUBTRACAO
            sub = n1 - n2
            print('*' * 30)
            print('Você escolheu SUBTRACAO')
            print('=-=' * 30)
            print('A Subtracao entre {} e {} e igual a: {}'.format(n1, n2, sub))
            print('=-=' * 30)
            print('Pressione 7 para mostrar novamente as opcoes')
            opcao = int(input('O que deseja agora? '))

    elif opcao == 3:# MULTIPLICACAO
        mult = n1 * n2
        print('*' * 30)
        print('Você escolheu MULTIPLICACAO')
        print('=-=' * 30)
        print('O resultado da multiplicacao entre {} e {} e igual a: {}'.format(n1, n2, mult))
        print('=-=' * 30)
        print('Pressione 7 para mostrar novamente as opcoes')
        opcao = int(input('O que deseja agora? '))

    elif opcao == 4:# DIVISAO
        mult = n1 / n2
        print('*' * 30)
        print('Você escolheu DIVISAO')
        print('=-=' * 30)
        print('O resultado da multiplicacao entre {} e {} e igual a: {}'.format(n1, n2, mult))
        print('=-=' * 30)
        print('Pressione 7 para mostrar novamente as opcoes')
        opcao = int(input('O que deseja agora? '))


    elif opcao == 5:  # QUAL E MAIOR
        if n1 > n2:
            print('*' * 30)
            print('Você escolheu QUAL E O MAIOR')
            print('=-=' * 30)
            print('O maior numero entre {} e {} e: {}'.format(n1, n2, n1))
            print('=-=' * 30)
            opcao = int(input('O que deseja agora? '))
        else:
            print('=-=' * 30)
            print('O maior numero entre {} e {} e: {}'.format(n1, n2, n2))
            print('=-=' * 30)
            print('Pressione 7 para mostrar novamente as opcoes')
            opcao = int(input('O que deseja agora? '))


    elif opcao == 6:#insere novos dados
        print('*' * 30)
        print('Você escolheu INSERIR NOVOS DADOS')
        print('=-=' * 30)
        n1 = int(input('Insira o primeiro numero, de novo: '))
        n2 = int(input('Insira o segundo numero, de novo: '))
        print('[1] SOMAR \n[2] SUBTRAIR \n[3] MULTIPLICAR \n[4] DIVIDIR \n[5] QUAL E O MAIOR \n[6] INSERIR NOVOS DADOS [8] SAIR DO PROGRAMA')
        opcao = int(input('O que deseja agora? '))

    elif opcao == 7:# Mostra opcoes
        print('*' * 30)
        print('Você escolheu MOSTRAR AS OPCOES NOVAMENTE')
        print('=-=' * 30)
        print('Suas opcoes sao: ')
        print('[1] SOMAR \n[2] SUBTRAIR \n[3] MULTIPLICAR \n[4] DIVIDIR \n[5] QUAL E O MAIOR \n[6] INSERIR NOVOS DADOS [8] SAIR DO PROGRAMA')
        opcao = int(input('O que deseja agora? '))

if opcao == 8:#agradece e sai
        print('*' * 30)
        print('Você escolheu SAIR DO PROGRAMA')
        print('Obrigado por utilizar nosso menu de opcoes.')
        exit()