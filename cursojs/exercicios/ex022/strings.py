frase = '   Curso em Vídeo Python  '
print(frase[3])

print(frase[3:13]) #Da terceira até a décima terceira letra, excluindo a décima terceira.

print(frase[:13]) #Do início até o 13.

print(frase[3:13])

print(frase[13:]) #Do 13 até o final

print(frase[1:15:2]) #Da 1 até 15 pulando de 2 em 2, sempre pegando pulo 2.

print(frase[1::2]) #Do 1 até o final pulando de 2 em 2.

print(frase[::2]) #Do início ao fim pulando de 2 em 2.

print(frase.count('O')) #Não tem "O" maiúsculo então retorna 0.

print(frase.upper().count('O')) #Vai elevar tudo para maiúsculo, então retornará a quantidade de "O" maiúsculo.

print(len(frase)) #Retorna a quantidade de caracteres, o comprimento da string.

print(len(frase.strip())) #Retorna o comprimento após remover os espaços das extremidades.

print(frase.replace('Python', 'Android')) #Trocará a palavra "Python" por "Android".

#frase[0] = 'j' Não funciona reatribuir um índice da string porque ela é imutável.

frase.replace('Python', 'Android') #Não irá fazer nada, a string continuará igual, não podendo substituir.

frase = frase.replace('Python', 'Android') #Mas assim funciona.

print('Curso' in frase) #Verifica se a palavra "Curso" existe dentro de frase.

print(frase.find('video')) #Retorna o índice de onde começa o trecho que estou procurando, mas se ele não existir, retorna -1

print(frase.split()) #Retorna uma lista com cada índice sendo uma palavra da string.

print("""abc
defg
      hijklm""") #Com 3 aspas duplas consigo imprimir quebrando linha.


dividido = frase.split()
print(dividido[0]) #Imprime a palavra "Curso".
print(dividido[2] [3]) #Imprime a letra de índice 3 da palavra de índice 2, no caso a letra "e" da palavra "Vídeo".