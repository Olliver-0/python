num = int(input('Digite um número para calcular seu Fatorial: '))
fat = num
print('{}! = '.format(num), end = '')
while num != 0:
    print('{}'.format(num), end = '')
    print(' x ' if num > 1 else ' = {}'.format(fat), end = '')
    fat *= num - 1
    num -= 1

#Ou...
# from math import factorial
# num = int(input('Digite um número para calcular seu Fatorial: '))
# fat = factorial()
# print('O fatorial de {} é {}'.format(num, fat))
