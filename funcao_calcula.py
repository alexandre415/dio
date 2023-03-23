def calcular_total(numero):
    return sum(numero)

def retorna_antecessor_e_sucessor(numero):

    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

print(calcular_total([10,20,34]))
print(retorna_antecessor_e_sucessor(10))