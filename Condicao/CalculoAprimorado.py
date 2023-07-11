print('--------------------------------------------')
print('CALCULADORA COM OPÇÃO DE RESPOSTA APRIMORADA')
print('--------------------------------------------')

n1 = int(input('Vamos começar! Insira o primeiro numero: '))
n2 = int(input('Boa! Agora, insira o segundo numero: '))
#
conta = str(
    input('Qual operação você deseja fazer?\n (Soma - A)\n (Subtração - B)\n (Multiplicação - C)\n (Divisão - D)\n'))

# coloque a entrada de dados entre aspas na condição se sua entrada for um texto!!!!!!!!!
if conta == "a" or conta == "A":
    result = n1 + n2
    print('A soma entre os valores {} e {} é: {}'.format(n1, n2, result))
else:
    if conta == "b" or conta == "B":
        result = n1 - n2
        print('A Subtração entre os valores {} e {} é: {}'.format(n1, n2, result))
    else:
        if conta == "c" or conta == "C":
            result = n1 * n2
            print('A multiplicação entre os valores {} e {} é: {}'.format(n1, n2, result))
        else:
            if conta == "d" or conta == "D":
                result = n1 / n2
                print('A divisão entre os valores {} e {} é: {}'.format(n1, n2, result))
print('-----------------------------------------------')
print('Obrigado por realizar o teste de nosso produto.')