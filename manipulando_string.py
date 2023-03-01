curso = "pYthon"

print(curso.upper())

print(curso.lower())

print(curso.title())

curso_2 = "   Python  "

#REMOVE ESPAÇO EM BRANCO DA ESQUERDA E DA DIREITA
print(curso_2.strip() + '.') 

#REMOVE SOMENTE O DA ESQUERDA

print(curso_2.lstrip() + '.')
#REMOVE SOMENTE O DA DIREITA
print(curso_2.rstrip() + '.')

curso_3 = "Python"



print(curso_3.center(10, "#")) # centraliza e mantem com 10 caracteres

print(".".join(curso_3))# cada iteração ele adiciona o argumento "."