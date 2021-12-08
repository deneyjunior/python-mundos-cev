print('='*10, 'Desafio 40', '='*10)
n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
media = (n1 + n2) / 2
print('Se a primeira nota é {:.2f} e a segunda nota é {:.2f}, então a média é {:.2f}.'.format(n1, n2, media))
if media < 5:
    print('ALUNO ESTÁ REPROVADO')
elif media >= 5 and media <= 6.9:
    print('ALUNO ESTÁ DE RECUPERAÇÃO')
elif media >= 7:
    print('ALUNO ESTÁ APROVADO')
print('='*10, 'Desafio 40', '='*10)
