#Verifica a categoria que o atleta esta classificado de acordo com sua idade
from datetime import date
data = date.today()
print(data)
print('----------------------------------')
print('Calculo de IMC (Indisse de Massa Corporal)')
print('----------------------------------')
print(' ')
#------------------------------------------------------
peso = float(input('Qual seu Peso? (kg) '))
altura = float(input('Qual sua Altura? (m)'))
print('*************************************')
imc = peso / (altura * altura)
#------------------------------------------------------
if (imc <= 18.5):
    print('Seu IMC é de {:.1f}. \nSTATUS: Abaixo do Peso! '.format(imc))
elif (imc > 18.5 and imc <= 25 ):
    print('Seu IMC é de {:.1f}. \nSTATUS: Peso Ideal! '.format(imc))
elif (imc > 25 and imc <= 30):
    print('Seu IMC é de {:.1f}. \nSTATUS: Sobrepeso! '.format(imc))
elif (imc > 30 and imc <= 40):
    print('Seu IMC é de {:.1f}. \nSTATUS: Obesidade! '.format(imc))
elif (imc > 40):
    print('Seu IMC é de {:.1f}. \nSTATUS: Obesidade morbida! '.format(imc))
#-------------------------------------------------------
