menor = maior = media = c = n = 0
continuar = 'S'
while continuar == 'S':
    n = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? [S/N]')).strip().upper() [0]
    c += 1
    media += n
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('Você digitou {} números e a média é {:.2f}'.format(c, (media / c)))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))