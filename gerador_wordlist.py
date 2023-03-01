import itertools

string = input('Digite a string a se permutada: ')
#resultado = itertools.permutations('abc', 3) # (qq caracter, tamanho q vai trabalhar)
resultado = itertools.permutations(string, len(string))
a=0
for i in resultado:
    print(''.join(i))
    a+=1
print(a)
