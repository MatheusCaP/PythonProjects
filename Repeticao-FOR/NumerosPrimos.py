#recebe um numero e define se ele e primo ou nao com base em quantas vezes ele é divisivel
num = int(input('Insira um numero para saber se ele é primo: '))
contp = 0
for c in range(1, num + 1, 1):
    if (num % c == 0):
        contp = contp + 1

if(contp <= 2):
    print(c)
    print('O numero {} foi divisivel {} vezes \nE por isso ele E PRIMO!'.format(num, contp))
elif(contp > 2):
    print(c)
   # contp = contp + 1
    print('O numero {} foi divisivel {} vezes \nE por isso ele NAO E PRIMO!'.format(num, contp))

