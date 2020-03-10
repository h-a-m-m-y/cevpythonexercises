larguraparede = float(input('Largura da parede: '))
alturaparede = float(input('Altura da parede: '))
demaos = float(input('Número de demãos recomendado: '))
areaparede = larguraparede * alturaparede
rendimento = 18
litrostinta = areaparede * demaos / rendimento
if demaos > 1:
    print('Para pintar uma parede de {:.2f}m² com {:.0f} demãos de tinta, você irá precisar de {:.1f} litros de tinta.'.format(areaparede, demaos, litrostinta))
elif demaos == 1:
    print('Para pintar uma parede de {:.2f}m² com {:.0f} demão de tinta, você irá precisar de {:.1f} litros de tinta.'.format(areaparede, demaos, litrostinta))
elif demaos < 1:
    print('Para pintar uma parede você precisa de pelo menos uma demão de tinta.')