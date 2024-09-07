primeiro = int(input('Digite um número para fazer PA: '))
razao = int(input('Digite a razão: '))
termo = primeiro
c = 1
while c < 11:
    print('{} -> '.format(termo), end = '')
    termo += razao
    c += 1
print('FIM')
