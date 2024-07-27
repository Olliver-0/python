from datetime import date
nasc = int(input('Digite seu ano de nascimento: '))
ano = date.today().year
idade = ano - nasc

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')