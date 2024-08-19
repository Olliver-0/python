s = ''
while s != 'M' and s != 'F':
    s = str(input('Digite seu gênero: ')).upper()
    if s != 'M' and s != 'F':
        print('Esse gênero é inválido! Tente novamente.')
if s == 'M':
    print('Seu gênero é masculino.')
else:
    print('Seu gênero é feminino.')
