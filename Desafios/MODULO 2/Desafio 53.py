print('='*10, 'Desafio 53', '='*10)
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
print('Você digitou a frase {}.'.format(frase))
print('O inverso da frase é {}.'.format(inverso))
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
if inverso == junto:
    print('A FRASE É UM PALINDROMO!')
else:
    print('A FRASE NÃO É UM PALINDROMO!')
print('='*10, 'Desafio 52', '='*10)
