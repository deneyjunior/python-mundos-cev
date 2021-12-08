print('='*10, 'Desafio 42', '='*20)
l1 = float(input('Digite o tamanho do primeiro lado: '))
l2 = float(input('Digite o tamanho do segundo lado: '))
l3 = float(input('Digite o tamanho do terceiro lado: '))
print('O lado 1 mede {}, o lado 2 mede {}, o lado 3 mede {}.'.format(l1, l2, l3))
# critério de formação do triângulo
# a soma de dois lados deve ser maior que o terceiro
if l1 + l2 > l3 and  l1 + l3 > l2 and l2 + l3 > l1:
    print('O triângulo apresenta os critérios de formação.')
    # analisando o triângulo
    if l1 == l2 and l2 == l3:
        print('O triângulo é equilátero.')
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print('O triângulo é escaleno.')
    else:
        print('O triângulo é isóceles.')
else:
    print('O triângulo não apresenta os critérios de formação.')

print('='*10, 'Desafio 41', '='*20)
