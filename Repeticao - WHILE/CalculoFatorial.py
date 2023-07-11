num = int(input('Digite o numero para calcular o Fatorial: '))
fatorial = num
antecessor = num
while fatorial != 1:
    fatorial -= 1
    antecessor *= fatorial
print('Calculando {}! = {}'.format(num, antecessor))