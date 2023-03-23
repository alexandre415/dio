#trabalhando com funcoes
def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome):
    print(f"O meu nome é: {nome}")

def exibir_mensagem_3(nome="Anonimo"):
    print(f"O meu nome é: {nome}")

exibir_mensagem()
exibir_mensagem_2(nome="Alexandre")
exibir_mensagem_3()
exibir_mensagem_3(nome="Alexandre")