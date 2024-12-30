lista = []
par = []
impar = []
continuar = 's'

while True:
    lista.append(int(input('Digite um número: ')))
    continuar = str(input('Quer continuar? [S/N]: ')).strip()
    if continuar not in 'Ss':
        break

for n in lista:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print(lista)
print(par)
print(impar)
