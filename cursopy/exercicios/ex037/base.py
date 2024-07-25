num = int(input('Digite um número: '))
print('''Escolha uma dessas bases para conversão
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opt = int(input('Sua opção: '))

if opt == 1:
    print('{} convertido para binário é {}'.format(num, bin(num)[2:]))
elif opt == 2:
    print('{} convertido para octal é {}'.format(num, oct(num)[2:]))
elif opt == 3:
    print('{} convertido para hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
