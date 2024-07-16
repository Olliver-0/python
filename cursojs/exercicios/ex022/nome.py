nome = str(input('Digite seu nome completo: '))
print('O seu nome com letras maiúsculas fica {}'.format(nome.upper()))
print('O seu nome com letras minúsculas fica {}'.format(nome.lower()))
print('O seu nome tem um total de {} letras'.format(len(nome.replace(' ', ''))))
primeiro_nome = nome.split()
print('Seu primeiro nome tem {} letras'.format(len(primeiro_nome[0]))) # ou...


nome = str(input('Digite seu nome completo: ')).strip()
print('O seu nome com letras maiúsculas fica {}'.format(nome.upper()))
print('O seu nome com letras minúsculas fica {}'.format(nome.lower()))
print('O seu nome tem um total de {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' '))) 
