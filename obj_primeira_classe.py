def somar(a, b):
    return a + b

def subtrair(a , b):
    return a - b

def exibir(a, b, funcao):

    resultado = funcao(a, b)

    print(f"O resultado da operacao é: {resultado}")

exibir(10, 10, somar)
exibir(10, 10, subtrair)

op = somar

print(op(1, 20))
