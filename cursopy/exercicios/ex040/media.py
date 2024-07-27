n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print('REPROVADO')
elif 7 > media >= 5:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
