#recebe o preco de produtos e depois retorna informacao sobre o total da compra e qual foi o item mais barato e o mais caro.
totalcompra = 0
pm1000 = 0
totalitem = 0
nomeproduto = str(input('Nome do produto: '))
totalitem += 1
nprodmaisbarato = nomeproduto
preco = float(input('PRECO: R$ '))
totalcompra += preco
prodmaisbarato = preco
continuacao = input('Quer continuar? ')
while True:
    nomeproduto = str(input('Nome do produto: '))
    totalitem += 1
    preco = float(input('PRECO: R$ '))
    if preco < prodmaisbarato:
        prodmaisbarato = preco
        nprodmaisbarato = nomeproduto
    totalcompra += preco
    continuacao = input('Quer continuar? ')
    if preco > 1000:
        pm1000 += 1
    if continuacao == 'n':
        print('{:-^40}'.format('FIM DO PROGRAMA'))
        print(f'Foram comprados {totalitem} itens')
        print(f'O total da compra foi de R${totalcompra:.2f}')
        print(f'Temos {pm1000} custando a cima de R$1000.00 ')
        print(f'O produto mais barato foi {nprodmaisbarato} que custa R${prodmaisbarato:.2f}')
        break