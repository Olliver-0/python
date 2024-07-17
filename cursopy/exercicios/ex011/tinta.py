altura = float(input('Digite a altura de uma parede: '))
largura = float(input('Digite a largura de uma parede: '))
area = (altura * largura) ** (1/2)
print('A parede tem {:.2f}m² \nVocê precisará de {:.2f} litros de tinta'.format(area, (area / 2)))
