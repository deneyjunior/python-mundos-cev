print('='*10, 'Desafio 34', '='*10)
salario = float(input('Qual o valor do salário do funcionário? '))
print('O seu salário atual é R$ {:.2f}.'.format(salario))
if salario > 1250:
    novo_salario = salario * 1.1
    print('O seu novo salário é R$ {:.2f}.'.format(novo_salario))
else:
    novo_salario = salario * 1.15
    print('O seu novo salario é R$ {:.2f}.'.format(novo_salario))

print('='*10, 'Desafio 34', '='*10)
