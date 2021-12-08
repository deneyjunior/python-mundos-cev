print('='*10, 'Desafio 44', '='*25)
valor_real = float(input('Qual o valor do produto? R$ '))
print('''Modo de Pagamento: 
[1] à vista dinheiro / cheque;
[2] à vista cartão;
[3] em até 2x no cartão;
[4] 3x ou mais no cartão.''')
modo_pagamento = int(input('Qual será o modo de pagamento? '))
if modo_pagamento == 1:
    novo_valor = 0.9 * valor_real
    print('O novo valor é R$ {}.'.format(novo_valor))
elif modo_pagamento == 2:
    novo_valor = 0.95 * valor_real
    print('O novo valor é R$ {}.'.format(novo_valor))
elif modo_pagamento == 3:
    novo_valor = valor_real
    print('O novo valor é R$ {}.'.format(novo_valor))
elif modo_pagamento == 4:
    novo_valor = 1.2 * valor_real
    print('O novo valor é R$ {}.'.format(novo_valor))
else:
    print('Escolha um modo de pagamento válido.')
print('='*10, 'Desafio 44', '='*25)

