num = int(input('Digite um valor [999 para encerrar o acumulo]: '))
cont = 0
soma = num
while True:
    num = int(input('Digite um valor [999 para encerrar a soma]: '))
    cont += 1
    if num == 999:
        break
    soma += num
print(f'A soma dos {cont} numeros digitados e: {soma}')