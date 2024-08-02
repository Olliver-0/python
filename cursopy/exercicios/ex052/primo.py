n = int(input('Digite um número: '))
primo = True
for c in range(2, n):
    if n <= 1:
        primo = False
    else:
        if n % c == 0:
            primo = False
        else:
            primo = True
if primo == True:
    print('Este número é primo')
else:
    print('Este número não é primo')
