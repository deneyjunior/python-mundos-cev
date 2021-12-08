print('='*10, 'Desafio 43', '='*25)
peso = float(input('Qual o seu peso em quilos? '))
altura = float(input('Qual a sua altura em metros? '))
imc = peso / (altura ** 2)
print("Se você tem {} metros e pesa {} quilos,\nentão o seu IMC é igual a {:.1f}.".format(altura, peso, imc))
if imc <= 18.5:
    print('Você está ABAIXO DO PESO.')
elif imc <= 24.9:
    print('Você está com o PESO IDEAL.')
elif imc <= 30:
    print('Você está com SOBREPESO.')
elif imc <= 40:
    print('Você está com OBESIDADE.')
else:
    print('Você está com OBESIDADE MÓRBIDA.')
print('='*10, 'Desafio 43', '='*25)

