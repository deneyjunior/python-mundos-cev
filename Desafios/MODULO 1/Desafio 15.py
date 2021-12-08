print('='*10, 'Desafio 15', '='*10)
dias = int(input('Quantos dias o carro ficou alugado?'))
km = float(input('Quantos quilometros foram rodados?'))
pago1 = dias * 60
pago2 = km * 0.15
pago = pago1 + pago2
print('O total a pagar é R$ {:.2f}.'.format(pago))