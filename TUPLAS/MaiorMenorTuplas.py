from random import sample
comput = tuple(sample(range(10), 5))
print(f'Os valores sorteados foram: {comput}')
print(f'O maior valor sorteado foi: {max(comput)}\nO menor valor sorteado foi: {min(comput)}')


