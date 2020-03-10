from math import radians, sin, cos, tan
angulo = float(input('Digite um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O seno de um ângulo de {:.2f}° é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}.'.format(angulo, seno, cosseno, tangente))