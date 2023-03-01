opcao = -1

while opcao != 0 :

    opcao = int(input('Digite 1 para saque ou 2 para extrato ou 0 para sair: '))

    if opcao == 1:
        print('Dinheiro retirado com sucesso')
    
    elif opcao == 2:

        print('Veja o seu extrato')

else:
    print('Obrigado por utilizar o sistema!')