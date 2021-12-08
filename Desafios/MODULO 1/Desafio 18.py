import math
print('{}{}{}'.format('=' * 10, ' Desafio 18 ', '='*10))
angulo = float(input('Digite um angulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('Para o angulo {}, \n o SENO é {:.4}, \n o COSSENO é {:.4} \n e a TANGENTE é {:.4}.'.format(angulo,seno,cosseno,tangente))