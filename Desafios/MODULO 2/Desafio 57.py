print('='*10, 'Desafio 57', '='*10)
sexo = str((input('Digite seu sexo [M/F]: '))).strip().upper()[0]
while sexo not in 'MmFm':
    sexo = str((input('Dados inválidos. Digite seu sexo [M/F]: '))).strip().upper()[0]
print('Sexo registrado com sucesso.')
print('='*10, 'Desafio 56', '='*10)