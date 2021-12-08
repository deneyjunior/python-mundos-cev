print('='*10, 'Desafio 59', '='*10)
# Variaveis 
programa = True
op = 0
# Saida para o usuário
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
print('='*32)
print('''Selecione uma opção:
          [1] Somar
          [2] Subtrair
          [3] Multiplicar
          [4] Divir
          [5] Novos numeros
          [6] Encerrar''')
print('='*32)
# Funcionamento do programa
while programa == True:
    opcao = int(input('Digite a sua opção: '))
    if opcao > 0 and opcao < 7:
        if opcao == 1:
            op = n1 + n2
            print('A soma de {} mais {} é {}.'.format(n1, n2, op))
            print('='*32)
        elif opcao == 2:
            op = n1 - n2
            print('A subtração de {} menos {} é {}.'.format(n1, n2, op))
            print('='*32)
        elif opcao == 3:
            op = n1 * n2
            print('A multriplicação de {} por {} é {}.'.format(n1, n2, op))
            print('='*32)
        elif opcao == 4:
            op = n1 / n2
            print('A divisão de {} por {} é {:.2f}.'.format(n1, n2, op))
            print('='*32)
        elif opcao == 5:
            n1 = int(input('Digite o primeiro numero: '))
            n2 = int(input('Digite o segundo numero: '))  
            print('='*32)
        elif opcao == 6:
            break       
    else:
        print('Opção inválida. Tente novamente.')
print('='*13, 'Fim!', '='*13)
print('='*10, 'Desafio 59', '='*10)