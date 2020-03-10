algo = input('Digite algo: ')
if algo == 'algo':
    print('engraçadão hein fera')
else:
    print('O tipo primitivo de {} é {}.'.format(algo,type(algo)))
    print('Possui apenas caracteres alfanuméricos? ', algo.isalnum())
    print('Possui apenas números? ', algo.isnumeric())
    print('Possui apenas espaços? ', algo.isspace())
    print('Possui apenas caracteres alfabéticos? ', algo.isalpha())
    print('Está apenas em letras maiúsculas? ', algo.isupper())
    print('Está apenas em letras minúsculas? ', algo.islower())
    print('Apenas a primeira letra de cada palavra é maiúscula? ', algo.istitle())
