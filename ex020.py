from random import shuffle
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome de outro aluno: '))
aluno3 = str(input('Digite o nome de outro aluno: '))
aluno4 = str(input('Digite o nome do último aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem final é: {}, {}, {} e por último {}.'.format(lista[0], lista[1], lista[2], lista[3]))
