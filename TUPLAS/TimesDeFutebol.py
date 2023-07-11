times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atletico - PR', 'Bahia', 'Sao Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitoria', 'Coritiba', 'Avai', 'Ponte preta', 'Atletico - GO')
print('-~' * 25)
print(f'Lista de times do Brasileirao {times}')
print('-~' * 25)
print(f'Os 5 primeiros sao: {times[0:5]}')#O python exclui o ultimo digito por isso precisa ser de 0 a 5
print('-~' * 25)
print(f'Os ultimos 4 colocados sao: {times[-4:]}') #-4: significa "mostre tudo a partir do -4, no caso a partir do 'coritiba'
print(f'Times em ordem alfabetica: {sorted(times)}')
print(f'O chapecoense esta na {times.index("Chapecoense")}° posicao')
