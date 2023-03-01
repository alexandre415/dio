#CONJUNTO NAO-ORDENADO DE PARES CHAVE:VALOR, ONDE AS CHAVES SAO UNICAS EM UMA DADA INSTANCIA DE DICIONARIO
#SÃO DELIMITADOS POR CHAVES {}
#E CONTEM UMA LISTA DE PARES CHAVES:VALOR  SEPARADAS POR VIRGULA

#o dicionario sobreescreve quando é atribuido valor em uma chave ja existente.

pessoa = {"nome": "Alexandre", "idade": 39}
print(pessoa)

pessoa = dict(nome="Alexandre", idade=39) # chama o construtor do dicionario
print(pessoa)

pessoa["telefone"] = "3333-3333" #ja tem o dict. criado e esta add uma nova chave:valor

print(pessoa)

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["telefone"],'\n')

pessoa["nome"] = "José Aldo"
pessoa["idade"] = 29
pessoa["telefone"] = "1234-2345"

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["telefone"])


contatos = {
        "alicesgrc@gmail.com": {"nome": "Alice Cardoso", "idade": 10, "telefone": "9608-3772"},
        "beatrizsdgrc@gmail.com": {"nome": "Beatriz Cardoso", "idade": 10, "telefone": "97117-1061"}
}
for chave, valor in contatos.items():
    print(chave, valor)

########################METODOS##################
#CLEAR, COPY, fromkeys, get

diciorario = dict.fromkeys(["nome", "telefone"])
print(diciorario)

print(diciorario.fromkeys(["nome", "telefone"], "vazio"))#todos os campos sao preenchidos com o valor "vazio"

#contatos["chave"]        gera erro por nao existir essa chave
print(contatos.get("chave"))
print(contatos.get("chave",{}))
print(contatos.get("alicesgrc@gmail.comu"))

#popitems remove os itens que o pop faz na lista. do ultima pro primeiro.
print('Valor pop item', contatos.popitem())
print(contatos)

#keys

print(contatos.keys())

#POP
print(contatos.pop("alicesgrc@gmail.com"))
print(contatos.pop("alicesgrc@gmail.com", "Valor nao encontrado"))

print(contatos)

#SETDEFAULT

contatos = {
        "alicesgrc@gmail.com\n": {"nome": "Alice Cardoso", "idade": 10, "telefone": "9608-3772\n"},
        "beatrizsdgrc@gmail.com": {"nome": "Beatriz Cardoso", "idade": 10, "telefone": "97117-1061"}
}

contatos.setdefault("nome", "Alexandre")#ele adicionou um chqave:valor que ele nao encontrou no dict.
print(contatos)

contatos.setdefault("nome", "Fernando")# ele nao adiciona pq ja existe uma chave nome no dict.
print(contatos)

contatos.update({"beatrizsdgrc@gmail.com":{"nome":"Biruta"}})# altera algo ja existente

print(contatos)
#primeiro ele procura se existe, caso nao exista ele add
contatos.update({"cefsiqueira@gmail.com":{"nome": "Carla Cardoso", "idade": 40, "telefone": "99955-3027"}})
print(contatos)

print(contatos.values())#imprime os valores  nao as chaves

resultado = "cefsiqueira@gmail.com" in contatos
print(resultado)

del contatos["cefsiqueira@gmail.com"]["telefone"] # apagou o telefone!
print(contatos)