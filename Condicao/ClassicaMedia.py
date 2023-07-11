#Verifica a media final do aluno com base nas duas notas que ele insere
from datetime import date
data = date.today()
print(data)
print('----------------------------------')
print('Consulta de media final')
print('----------------------------------')
print(' ')

#Definicao de variaveis
nota1 = float(input('Insira a 1° nota: '))
nota2 = float(input('Insira a 2° nota: '))
print(' ')

media = float(nota1 + nota2) / 2

#processamento de variaveis
if(media <= 4.9):
    print('Primeira nota: {} \nSegunda nota: {} \nMedia final: {}'.format(nota1, nota2, media))
    print('Resultado: Aluno REPROVADO ')
elif(media >4.9 and media <6):
    print('Primeira nota: {} \nSegunda nota: {} \nMedia final: {}'.format(nota1, nota2, media))
    print('Resultado: Aluno em RECUPERACAO ')
elif(media >6):
    print('Primeira nota: {} \nSegunda nota: {} \nMedia final: {}'.format(nota1, nota2, media))
    print('Resultado: Aluno APROVADO')

