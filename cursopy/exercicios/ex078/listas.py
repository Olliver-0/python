num = [2, 5, 9, 1]
num[2] = 3 #altera valor
num.append(7) #adiciona novo valor
num.sort() #põe em ordem
num.sort(reverse = True) #põe em ordem reversa
num.insert(2, 0) #insere, na posição 2, um 0
num.pop() #elimina o último valor
num.pop(2) #elimina o índice 2
num.remove(3) #remove a primeira ocorrência desse valor
if 4 in num:
    num.remove(4)
print(f'Essa lista tem {len(num)} elementos')

valores = [] #ou valores = list() ~ lista vazia
valores.append(5)
valores.append(9)
valores.append(4)
for c, v in enumerate(valores):
    print(f'Na posição {c}, encontrei o valor {v}!')

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))


a = [2, 3, 4, 7]
b = a
b[2] = 8 #nesse caso, o python fez uma ligação entre as duas listas porque igualei elas, alterar uma, altera a outra
print(a)
print(b)
b = a[:] #aqui B está recebendo todos os valores de A, e não A especificamente, então não há uma ligação, é uma cópia
b[3] = 1
print(a)
print(b)
