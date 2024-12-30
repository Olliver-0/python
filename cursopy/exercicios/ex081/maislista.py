lista = []
continuar = 's'

while True:
    lista.append(int(input('Digite um número: ')))
    continuar = str(input('Quer continuar? [S/N]: ')).strip()
    if continuar not in 'Ss':
        break
lista.sort(reverse = True)
print(f'Você digitou {len(lista)} números')
print(lista)
if 5 in lista:
    print('O valor 5 foi digitado')
else:
    print('O valor 5 não foi digitado')
