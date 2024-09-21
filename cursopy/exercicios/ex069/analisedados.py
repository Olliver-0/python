continuar = 's'
maioridade = homens = mulheres = 0
while continuar == 's':
    print('-' * 15)
    print('CADASTRE PESSOAS!')
    print('-' * 15)
    idade = int(input('Digite uma idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().lower()
    continuar = str(input('Quer continuar? [S/N]: ')).strip().lower()
    maioridade += 1 if idade >= 1 else 0
    homens += 1 if sexo == 'm' else 0
    mulheres += 1 if sexo == 'f' and idade >= 20 else 0
    if sexo != 'm' and sexo != 'f' or continuar != 's': break
print(f'Há {maioridade} pessoas com mais de 18 anos, {homens} homens, e {mulheres} mulheres com mais de 20 anos') 
