import textwrap


def menu():
    menu = """\n
=============================
Digite uma das opções abaixo:

[d]\t - Depósito
[s]\t - Saque
[e]\t - Extrato
[nc]\t - Nova Conta
[lc]\t - Listar Contas
[nu]\t - Novo Usuário
[q]\t - Sair
==============================
"""
    return input(textwrap.dedent(menu))



def depositar(saldo, valor, extrato, /):
     
    if valor > 0:
                # extrato = extrato.append(float(deposito)) para futura lista
                saldo += float(valor)
                extrato = f'\nDeposito de {valor:.2f} realizado com sucesso'
        
    else:
        
                print('O valor precisa ser maior que 0') 

    return saldo, extrato

def sacar(* , saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
           print("\n Operação falhou! Você não tem saldo suficiente")

    elif excedeu_limite:
           print("\n Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
           print("\n Operação falhou! Número máximo de saque excedido.") 
    elif valor > 0:
           saldo -=valor
           extrato += f"Saque: \t\t R$ {valor:.2f}"
           numero_saques +=1
           print("\n Saque realizado com sucesso!")
    else:
        print("\n Operação Falhou! O valor informado não é válido")

    return saldo, extrato
                 
def exibir_extrato(saldo, /, *, extrato):

    print('#########################################')
    print('Nao tem saldo'if not extrato else extrato)
    print(f' Você possue R$:{saldo:.2f} em sua conta')
    print('#########################################')

def criar_usuario(usuarios):
    cpf = input("Informe o CPF do usuário(somente números)")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
          print("\n Já existe usuário com este CPF!")
          return
    
    nome = input("Informe o nome completo do usuário: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço: ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!!")

def filtrar_usuario(cpf, usuario):

    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf] 
    return usuarios_filtrados[0] if usuarios_filtrados else None
def criar_conta(agencia, numero_conta, usuarios):
     
     cpf = input("Informe o CPF do usuário(somente números)")
     usuario = filtrar_usuario(cpf, usuarios)
     if usuario:
          print("\n Conta criada com sucesso!")
          return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
     
     print("Usuário não encontrado! Fluxo de criar conta encerrado!!")

def listar_contas(contas):
     for conta in contas:
           linha = f"""\
                Agência:\t{conta["agencia"]}
                C/C:\t\t{conta[numero_contas]}
                Titular:\t{conta["usuario"]['nome']}
            """
           print("*" * 100)
           print(textwrap.dedent(linha))
           
def main():

    LIMITE_SAQUE = 3
    AGENCIA = '0001'
     
    limite = 500
    numero_saques = 0
    saldo = 0.0
    extrato = ''
    usuarios = []
    contas = []
    
    while True:
         
        opcao = menu()
    
        if opcao == "d":

            valor = float(input(print( 'Deseja depositar qual valor ?')))

            saldo, extrato = depositar(saldo, valor, extrato)
           

        elif opcao == "s":

            numero_saque+=1
            valor = float(input('Qual o valor você deseja sacar?'))
            
            saldo, extrato = sacar(
                   saldo=saldo,
                   valor=valor,
                   extrato=extrato,
                   limite=limite,
                   numero_saques=numero_saques,
                   limite_saques=LIMITE_SAQUE
            )
           
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        # print('#########################################')
        # print('Nao tem saldo'if not extrato else extrato)
        # print(f' Você possue R$:{saldo:.2f} em sua conta')
   
        elif opcao == "nu":
           
            criar_usuario(usuario)

        elif opcao == "nc":
           numero_conta = len(contas) + 1
           conta = criar_conta(AGENCIA, numero_conta, usuarios)

           if conta:
                 contas.append(conta)
        elif opcao == 'lc':
           listar_contas(contas)
    
        elif opcao == "q":
            break
        
        else:
            print("Opção inválida")
     
main()

