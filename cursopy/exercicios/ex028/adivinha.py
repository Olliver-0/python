from random import randint
from time import sleep

num = randint(0, 5)

print('-=-' * 17)
print('Eu pensei num número de 0 a 5, que número é esse?')
print('-=-' * 17)

escolha = int(input())
print('PROCESSANDO...')
sleep(2)

if escolha == num:
    print('Parabéns, você acertou!')
else:
    print('Errado! O número que pensei é {}'.format(num))
