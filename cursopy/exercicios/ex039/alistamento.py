from datetime import date
ano = date.today().year
nasc = int(input('Digite seu ano de nascimento: '))
idade = ano - nasc

if idade < 18:
    print('Ainda não está na hora de se alistar, faltam {} anos.'.format(18 - idade))
elif idade == 18:
    print('Já está na hora de se alistar.')
else:
    print('Já passou {} anos do seu alistamento.'.format(idade - 18))
