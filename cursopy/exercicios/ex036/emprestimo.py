val = float(input('Digite o valor da casa: '))
sal = float(input('Digite seu salário: '))
tempo = int(input('Digite em quantos anos irá pagar: '))

prestacao = val / (tempo * 12)

if prestacao < sal * 0.3:
    print('O valor das suas prestações mensais será R${:.2f}'.format(prestacao))
else:
    print('Empréstimo negado. O valor das prestações excede 30% do seu salário.')
