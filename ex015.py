diasalugados = float(input('Por quantos dias o veículo foi alugado? '))
kmrodados = float(input('Quantos KMs rodados? '))
diarias = diasalugados * 60
distanciapercorrida = kmrodados * 0.15
total = diarias + distanciapercorrida
print('O custo total do aluguel é R${:.2f}.'.format(total))