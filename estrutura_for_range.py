texto = input('Digite um texto:')
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')


print()

#range (start, stop, step)

for numero in range(0,10):
    print(numero, end=' ')

for tabuada in range(0,51, 5):
    print(tabuada, end=' ')