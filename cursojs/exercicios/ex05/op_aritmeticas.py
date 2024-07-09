# print(pow(5, 2))
# print(81 ** (1/2))
# print(25 ** (1/3))
# print('=' * 100)

# nome = input('Qual é o seu nome? ')
# print('Prazer em te conhecer, {:20}!'.format(nome))
# print('Prazer em te conhecer, {:>20}!'.format(nome))
# print('Prazer em te conhecer, {:<20}!'.format(nome))
# print('Prazer em te conhecer, {:^20}!'.format(nome))
# print('Prazer em te conhecer, {:=^20}!'.format(nome))
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
mo = n1 % n2
e = n1 ** n2
print('A soma é {}, a subtração é {}, \n o produto é {}, a divisão é {:.3f}, a divisão inteira é {}, o módulo é {}, e a potência é {}'.format(s, su, m, d, di, mo, e), end = ' ')
print('Operadores')
