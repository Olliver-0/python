km = float(input('Quantos Km o carro rodou? '))
dias = int(input('Por quantos dias ele ficou alugado? '))
print('O preço a pagar pelo aluguel é R${:.2f}'.format((dias * 60) + (km * 0.15)))
