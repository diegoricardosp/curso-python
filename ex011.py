alt = float(input('Digite a altura da parede: '))
larg = float(input('Digite a largura da parede: '))
area = alt * larg
tinta = area / 2
print('Você precisará de {:.0f} latas de tintas para pintar sua parede.'.format(tinta))