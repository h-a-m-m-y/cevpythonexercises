from math import pow, sqrt
catetooposto = float(input('Digite o comprimento do cateto oposto: '))
catetoadjacente = float(input('Digite o comprimento do cateto adjacente: '))
quadradohipotenusa = pow(catetooposto, 2) + pow(catetoadjacente, 2)
hipotenusa = sqrt(quadradohipotenusa)
print('Para um triângulo retângulo de cateto oposto de medida {} e cateto adjacente medida {}, a hipotenusa tem medida {}.'.format(catetooposto, catetoadjacente, hipotenusa))