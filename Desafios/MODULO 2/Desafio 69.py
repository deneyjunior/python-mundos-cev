print('='*10, 'Desafio 69', '='*10)
repeticao = 'S'
maior_idade = 0
homem = 0
mulher = 0
cont = 0
sexo = ' '
while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [H/M]: ')).upper().split()
    cont += 1
    if idade >= 18:
        maior_idade += 1
    if sexo == 'M' or sexo:
        homem += 1
    repeticao = str(input('Você quer cadastrar outra pessoa? [S/N]')).upper().split()
    if repeticao == 'N':
        break
print(f'Você cadastrou {cont} pessoas.')
print(f'Das {cont}, {maior_idade} são maiores de idade')
print(f'Das {cont}, {homem} são homens.')
print(f'Das {cont}, {mulher} são mulheres.')

    