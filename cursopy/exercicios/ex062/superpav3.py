
primeiro = int(input('Digite um número para fazer PA: '))
razao = int(input('Digite a razão: '))
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print('{} -> '.format(termo), end = '')
        termo += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
