#####ESTRUTURA MUTÁVEL

letras = list("Python") #chama o construtor
print(letras)
numero = list(range(10)) #chama o construtor
print(numero)

matriz = [
    [0,1,2],
    [5,8,7]]

print(matriz[0])
print(matriz[0][2])

print(letras[2:])
print(letras[0:2])
print(letras[1:3])
print(letras[0:3:2])
print(letras[::])
print(letras[::-1])


carros = ["gol", 'Alfa Romeu', 'Tempra']

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f' {indice}: {carro}')



#IDENTIFICANDO SE UM NUMERO É PAR EM LISTAS

numeros = [129, 30, 128, 50, 33]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)

#ou pode ser feito da seguinte forma:

pares_= [ numero for numero in numeros if numero % 2 == 0 ]
print(pares_)

numeros2 = [129, 30, 128, 50, 33]
quadrado = [ numero ** 2 for numero in numeros2]
print(quadrado)

quadrado.clear() #ESVAZIA A LISTA
print(quadrado)

numeros3 = [129, 30, 128, 50, 33]

numero_copy = numeros3.copy()

print(numero_copy)
print(id(numero_copy), id(numeros3)) # O QUE FAÇO NA COPIA NAO REFLETE NO ORIGINAL

cores = ['vermelho', 'azul','amarela', 'bege', 'vermelho']

print(cores.count('vermelho'))

linguagens = ['python', 'js', 'react']

print(linguagens)

linguagens.extend(["java", "js"])# recebe mais de um argumento.
print(linguagens)
linguagens.append('java') # recebe somente um argumento
print(linguagens)

#INDEX -> PROCURAMOS A PRIMEIRA OCORRENCIA DE UM OBJETO

print(linguagens.index('python'))

linguagens.pop() # retira o ultimo item da lista. VOCE PODE PASSAR O INDICE DIRETO EX.: LINGUAGENS.POP(0)
print(linguagens)

linguagens.remove("js")#AQUI ELE RETIRA O primeiro item que achar
print(linguagens)

linguagens.reverse()# inverte a ordem dos elementos da lista
print(linguagens)

linguagens.sort()#ordena a lista
linguagens.sort(reverse=True)# primeiro ordena depois inverte

linguagens.sort(key=lambda x:len(x))# ele conta a quantidade de caracter de cada string e ordena em seguida
print(linguagens)

#pode combinar ambos!

linguagens.sort(key=lambda x:len(x), reverse=True)
print(linguagens)

sorted(linguagens, key=lambda x: len(x))
