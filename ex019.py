from random import choice
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome de outro aluno: ')
aluno3 = input('Digite o nome de outro aluno: ')
aluno4 = input('Digite o nome do último aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
sorteado = choice(lista)
print('O aluno sortedo para apagar o quadro foi {}!'.format(sorteado))