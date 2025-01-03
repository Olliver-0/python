expressao = str(input('Digite uma expressão: '))
parentesesEsquerdos = expressao.count('(')
parentesesDireitos = expressao.count(')')
if parentesesEsquerdos != parentesesDireitos:
    print('Sua expressão é inválida!')
else:
    print('Sua expressão é válida')
