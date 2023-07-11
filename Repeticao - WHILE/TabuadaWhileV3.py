#Programa que apresenta a tabuada de qualquer numero que o usuario inserir.
num = 0
while True:
    print('~' * 40)
    print('[Insira 000 para finalizar]')
    print('-' * 40)
    num = int(input('Insira um numero para retornar a tabuada: '))
    if num == 000:
        break
    print('-' * 40)
    for c in range(0, 10, 1):
        c += 1
        result = num * c
        print(f'{num} X {c} = {result}')