#coleção que nao utiliza objeto repetido. utilizamos em conjuntos matematicos ou eliminar itens duplicado
#de um iteravel

#ele elimina os itens duplicados
print(set([1,2,3,4,3,2,4,1]))

print(set("abacaxi"))


#CONJUNTOS EM PYTHON NAO SUPORTAM INDEXACAO E NEM FATIAMENTO. CASO QUEIRA, É NECESSARIO CONVERTER EM LISTA

linguagem = {'python', 'java', 'python'} # criando o set(conjunto de dados)
print(linguagem) 

converte_em_lista = list(linguagem)

print(converte_em_lista[0])

#para percorrer vc utiliza um for e pode usar um enumerate para saber o indice correspondente

#METODOS DO SET - > UNION, INTERSECTION, DIFFERENCE, SYMMETRIC_DIFFERENCE, ISSUBSET, ISDISJOINT, ADD,
#COPY, DISCARD, CLEAR, POP(AQUI TIRA O DA FRENTE!=DA LISTA), REMOVE, LEN, IN

conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b))

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.intersection(conjunto_b))

#DIFFERENCE
print(conjunto_a.difference(conjunto_b))#o que tem em a que é diferente que tem em b
print(conjunto_b.difference(conjunto_a)) #o que tem em b que é diferente q tem em a

#SYMMETRIC_DIFFERENCE
#QUERO TUDO QUE TEM EM A E B MENOS A INTERSEÇÃO ENTRE ELES.

print(conjunto_a.symmetric_difference(conjunto_b))

#ISSUBSET, ou seja, é um subconjunto de.

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 4, 5, 3}

print(conjunto_a.issubset(conjunto_b))#todos elementos de a estam em b
print(conjunto_b.issubset(conjunto_a))#todos elementos de b estao em a

#ISDISJOINT nao faz parte de. quando nao possue interseção

conjunto_a = {1, 2, 3}
conjunto_b = {4 ,5 ,6}
conjunto_c = {1, 0}

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))
print(conjunto_b.isdisjoint(conjunto_c))

sorteio = {11, 20}
sorteio.add(25)
sorteio.add(26)
sorteio.add(27)
sorteio.add(27)
sorteio.add(30)

print(sorteio)

#DISCARD SE CHAMAR UM ELEMENTO QUE NAO EXISTE ELE NAO GERA ERRO

sorteio.discard(25)#ele procura e descarta somente esse valor
print(sorteio)

#pop -> tira o primeiro item do conjunto de dados

print(sorteio.pop())
print(sorteio)
print(sorteio.pop())
print(sorteio)

#REMOVE GERA ERRO SE CHAMAR UM ELEMENTO QUE NAO EXISTE, DIFERENTE DO DISCARD

sorteio.remove(26)
print(sorteio)

#IN

print(27 in sorteio)