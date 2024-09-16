from random import random
c = 0

while True:
    print('=-' * 15)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('=-' * 15)

    n1 = int(input('Diga um valor: '))
    pi = str(input('Par ou Ímpar? [P/I]')).strip().lower()
    print('-' * 30)

    n2 = int(random() * 10)
    resultado = 'PAR' if (n1 + n2) % 2 == 0 else 'ÍMPAR'
    print(f'Você jogou {n1} e o computador {n2}. Total de {n1 + n2} DEU {resultado}')
    print('-' * 30)

    if (resultado == 'PAR' and pi == 'p') or (resultado == 'ÍMPAR' and pi == 'i'):
            print('Você VENCEU!')
            print('Vamos Jogar Novamente...')
            c += 1
    else:
            print('Você PERDEU')
            print('=-' * 15)
            print(f'GAME OVER! Você venceu {c} vezes')
            break
