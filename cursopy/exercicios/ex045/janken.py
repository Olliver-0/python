from random import randint
from time import sleep
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL      
[ 2 ] TESOURA''')
computador = randint(0, 2)
jogador = int(input('Qual a sua jogada? '))

if computador == 0:
    computador = 'Pedra'
elif computador == 1:
    computador = 'Papel'
else:
    computador = 'Tesoura'

if jogador == 0:
    jogador = 'Pedra'
elif jogador == 1:
    jogador = 'Papel'
else:
    jogador = 'Tesoura'

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)

print('-=-' * 8)
print('Computador jogou {}'.format(computador))
print('Jogador jogou {}'.format(jogador))
print('-=-' * 8)

if computador == 'Pedra' and jogador == 'Papel':
    print('JOGADOR VENCE')
elif computador == 'Pedra' and jogador == 'Tesoura':
    print('COMPUTADOR VENCE')
elif computador == 'Papel' and jogador == 'Pedra':
    print('COMPUTADOR VENCE')
elif computador == 'Papel' and jogador == 'Tesoura':
    print('JOGADOR VENCE')
elif computador == 'Tesoura' and jogador == 'Pedra':
    print('JOGADOR VENCE')
elif computador == 'Tesoura' and jogador == 'Papel':
    print('COMPUTADOR VENCE')
else:
    print('EMPATE')
