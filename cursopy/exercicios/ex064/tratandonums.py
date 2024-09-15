c = n = soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        c += 1
        soma += n
print('Você digitou {} números e a soma entre eles é {}'.format(c, soma))
