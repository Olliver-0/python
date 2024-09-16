c = 1
n = 0
while n >= 0:
    n = int(input('Digite um número para ver a tabuada: '))
    while c < 11:
        if n >= 0:
            print(f'{n} x {c} = {n * c}')
            c += 1
        if n < 0:
            break
    c = 1
