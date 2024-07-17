dist = float(input('Digite a distância da sua viagem: '))
if dist < 200:
    passagem = dist * 0.50
    print('Você pagará R${:.2f} pela sua viagem'.format(passagem))
else:
    passagem = dist * 0.45
    print('Você pagará R${:.2f} pela sua viagem'.format(passagem))
