# lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# # print(lanche[1])
# # print(lanche[-1])
# # print(lanche[1:3])
# # print(lanche[2:])
# # print(lanche[:4])
# # print(lanche)
# # #for pos, comida in enumerate(lanche):
# #     # print(f'Eu vou comer {comida} na posição {pos}')
# # for cont in range(0, len(lanche)):
# #     print(lanche[cont])

# print(sorted(lanche))

# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = a + b
# print(c.count(5))
# print(c.index(8))
# print(c.index(5, 1))

# pessoa = ('Gustavo', 39, 'M', 99.88)
# print(pessoa)
# del(pessoa)

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    while num < 0 or num > 20:
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))

    print(f'Você digitou o número {extenso[num]}')
    continuar = str(input('Quer continuar? [s/n]')).strip().lower()
    if continuar == 'n':
        break
