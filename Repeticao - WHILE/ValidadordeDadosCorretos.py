#Programa que recebe o sexo do usuario e enquanto nao for digitado corretamente ele pede uma nova entrada
sexo = str(input('Informe seu sexo [M/F]: '.upper()))#.Upper para converter a entrada para maiuscula
while sexo not in 'MmFf':
    sexo = input('DADOS INVALIDOS! Por favor insira novamene. Informe seu sexo [M/F]: '.upper())
print('Dados de sexo cadastrados com Sucesso. Obrigado')
exit()
