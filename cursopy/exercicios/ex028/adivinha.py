from random import choice
numlist = [0, 1, 2, 3, 4, 5]
num = choice(numlist)
print('Eu pensei num número de 0 a 5, que número é esse?')
escolha = int(input())
if escolha == num:
    print('Parabéns, você acertou!')
else:
    print('Errado! O número que pensei é {}'.format(num))
