print('='*10, 'Desafio 36', '='*10)
valor_da_casa = float(input('O valor do imovel: R$ '))
salario_comprador = float(input('O salário do comprador: R$ '))
anos_financiamento = int(input('Anos de financiamento: '))
parcela = valor_da_casa / (anos_financiamento * 12)
print('Para pagar uma casa de R$ {:.2f} em {} anos, a prestação será de R$ {:.2f}.'.format(valor_da_casa, anos_financiamento, parcela))
if parcela <= 0.3 * salario_comprador:
    print('\033[1;32mEmpréstimo APROVADO!\033[0;0m')
else:
    print('\033[1;31mEmpréstimo REPROVADO!\033[0;0m')
print('='*10, 'Desafio 36', '='*10)
