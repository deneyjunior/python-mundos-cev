print('='*10, 'Desafio 71', '='*10)
print('{:^32}'.format('Banco CEV'))
print('='*32)
valor = int(input('Quanto você quer sacar? '))
total = valor
total_cedula = 0
ced = 50
while True:
    if total >= ced:
        total -= ced 
        total_cedula += 1
    else: 
        if total_cedula > 0:
            print(f'Total de {total_cedula} de cédulas de R$ {ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if total == 0:
            break