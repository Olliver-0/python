nome = str(input('Digite seu nome completo: ')).strip()
nome_separado = nome.split()
print('Seu primeiro nome é {}'.format(nome_separado[0]))
print('Seu último nome é {}'.format(nome_separado[len(nome_separado) - 1]))
