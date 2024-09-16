c = n = soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        c += 1
        soma += n
print(f'Você digitou {c} números e a soma entre eles é {soma}')
