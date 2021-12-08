print('='*10, 'Desafio 64', '='*10)
num = soma = cont = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num != 999:
        soma += num
        cont += 1
print('Você digitou {} numeros. A soma detodos os numeros é {}.'.format(cont, soma))
print('Fim!')
print('='*10, 'Desafio 64', '='*10)
