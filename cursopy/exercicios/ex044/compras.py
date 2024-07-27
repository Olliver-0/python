preco = float(input('Digite o preço do produto R$'))
print('Escolha sua forma de pagamento')
print('''À vista dinheiro/cheque [ 1 ]
À vista cartão [ 2 ]
Até 2x no cartão [ 3 ]
3x ou mais no cartão [ 4 ]''')
meio = int(input())

if meio == 1:
    print('Você pagará R${}'.format(preco - preco * 0.1))
elif meio == 2:
    print('Você pagará R${}'.format(preco - preco * 0.05))
elif meio == 3:
    print('Você pagará R${}'.format(preco))
elif meio == 4:
    print('Você pagará R${}'.format(preco * 1.2))
else:
    print('Forma de pagamento inválida.')
