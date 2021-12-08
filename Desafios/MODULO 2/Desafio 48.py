print('='*10, 'Desafio 48', '='*10)
soma = 0
cont = 0
for mult in range(1, 501, 2):
    if mult % 3 == 0:
        soma = soma + mult
        cont = cont + 1 
print('A soma dos {} numeros solicitados é {}.'.format(cont, soma))
print('='*10, 'Desafio 47', '='*10)