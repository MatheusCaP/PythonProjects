from datetime import date
data = date.today()
print(data)
print('{:=^40}'.format('LOJAS GUANABARA'))
#--------------------------------------------------
preco = int(input('Insira o preço das compras: R$ '))
avistaDP = preco - (0.10 * preco)
avistaDC = preco - (0.05 * preco)
parcela2X = preco / 2
credito2X = preco
credito3X = preco + (0.20 * preco)
#--------------------------------------------------
print(' ')
print('FORMAS DE PAGAMENTO: ')
print('[1] á vista dinheiro/pix')
print('[2] á vista credito/debito')
print('[3] Credito 2x')
print('[4] Credito 3x ou mais')
opcao = int(input('Qual a opcao para pagamento? '))
print(' ')
#--------------------------------------------------
if(opcao == 1):
    print('Nesta forma de pagamento voce recebe um desconto de 10%')
    print('O valor da compra sera de R${:.2F} '.format(avistaDP))
elif(opcao == 2):
    print('Nesta forma de pagamento voce recebe um desconto de 5%')
    print('O valor da compra sera de R${:.2F} '.format(avistaDC))
elif(opcao == 3):
    print('Nesta forma de pagamento nao ha descontos nem acrescimos')
    print('O valor da compra sera de R${:.2F} '.format(credito2X))
    print('Sua compra sera parcelada em 2X de R${:.2F} SEM JUROS '.format(parcela2X))
elif(opcao == 4):
    nparcelas = int(input('Em quantas parcelas seria o pagamento? '))
    divida = (credito3X / nparcelas)
    print('Nesta forma de pagamento voce recebe juros de 20%')
    print('O valor da compra sera de R${:.2F} '.format(credito3X))
    print('A compra sera em {}X de R${:.2F}'.format(nparcelas, divida))
else:
    print('OPCAO INVALIDA! Tente novamente.')
