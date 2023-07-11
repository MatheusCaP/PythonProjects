#Programa que recebe dois numeros e pergunta qual operacao voce quer fazer
n1 = int(input('Insira o primeiro numero: '))
n2 = int(input('Insira o segundo numero: '))
print(' ')
print('Suas opcoes sao: ')
print('[1] SOMAR \n[2] MULTIPLICAR \n[3] QUAL E MAIOR \n[4] INSERIR NOVOS NUMEROS\n[5] SAIR DO PROGRAMA')
opcao = int(input('O que deseja? '))


while opcao != 5:
    if opcao == 1:#soma
        soma = n1 + n2
        print('=-=' * 30)
        print('A soma entre {} e {} e igual a: {}'.format(n1, n2, soma))
        print('=-=' * 30)
        print('Suas opcoes sao: ')
        print('[1] SOMAR \n[2] MULTIPLICAR \n[3] QUAL E MAIOR \n[4] INSERIR NOVOS NUMEROS\n[5] SAIR DO PROGRAMA')
        opcao = int(input('O que deseja agora? '))

    elif opcao == 2:#multiplica
        mult = n1 * n2
        print('=-=' * 30)
        print('O resultado da multiplicacao entre {} e {} e igual a: {}'.format(n1, n2, mult))
        print('=-=' * 30)
        print('Suas opcoes sao: ')
        print('[1] SOMAR \n[2] MULTIPLICAR \n[3] QUAL E MAIOR \n[4] INSERIR NOVOS NUMEROS\n[5] SAIR DO PROGRAMA')
        opcao = int(input('O que deseja agora? '))
    elif opcao == 3:#qual e maior
        if n1 > n2:
            print('=-=' * 30)
            print('O maior numero entre {} e {} e: {}'.format(n1, n2, n1))
            print('=-=' * 30)
        else:
            print('=-=' * 30)
            print('O maior numero entre {} e {} e: {}'.format(n1, n2, n2))
            print('=-=' * 30)
        print('Suas opcoes sao: ')
        print('[1] SOMAR \n[2] MULTIPLICAR \n[3] QUAL E MAIOR \n[4] INSERIR NOVOS NUMEROS\n[5] SAIR DO PROGRAMA')
        opcao = int(input('O que deseja agora? '))
    elif opcao == 4:#insere novos dados
        print('=-=' * 30)
        n1 = int(input('Insira o primeiro numero, de novo: '))
        n2 = int(input('Insira o segundo numero, de novo: '))
        print('Suas opcoes sao: ')
        print('[1] SOMAR \n[2] MULTIPLICAR \n[3] QUAL E MAIOR \n[4] INSERIR NOVOS NUMEROS\n[5] SAIR DO PROGRAMA')
        opcao = int(input('O que deseja? '))
if opcao == 5:#agradece e sai
        print('Obrigado por utilizar nosso menu de opcoes.')
        exit()