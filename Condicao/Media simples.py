#teste para lembrar conhecimentos em Python

print('Calculadora de media simples, insira as notas para calculo da média')
nota1 = int(input('Insira a primeira nota: '))
nota2 = int(input('Insira a segunda nota: '))
nota3 = int(input('Insira a terceira nota: '))
media = (nota1 + nota2 + nota3)/3


if(media >= 5):
    print(f'Aluno foi aprovado com a media {media}')
elif(media <= 4):
    print(f'Aluno foi reprovado com a media {media}')