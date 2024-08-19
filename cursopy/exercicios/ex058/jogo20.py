from random import randint
from time import sleep

num = randint(0, 10)

print('-=-' * 17)
print('Eu pensei num número de 0 a 10, que número é esse?')
print('-=-' * 17)

escolha = 0
c = 0
while escolha != num:
    escolha = int(input())
    print('PROCESSANDO...')
    sleep(2)
    if escolha != num:
        print('Errado! Tente novamente.')
    c += 1
print('Parabéns, você acertou! Você precisou de {} tentaivas'.format(c))
