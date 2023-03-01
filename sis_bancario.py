menu = """

Digite uma das opções abaixo:

[d] - Depósito
[s] - Saque
[e] - Extrato
[q] - Sair

"""
limite = 500
numero_saque = 0
LIMITE_SAQUE = 3
saldo = 0.0
extrato = ''

while True:


    opcao = input(menu)
    
    if opcao == 'd':

            deposito = float(input(print( 'Deseja depositar qual valor ?')))
        
            if deposito > 0:
                # extrato = extrato.append(float(deposito)) para futura lista
                saldo += float(deposito)
                extrato = f'\nDeposito de {deposito:.2f} realizado com sucesso'
        
            else:
        
                print('O valor precisa ser maior que 0') 

    elif opcao == 's':

            numero_saque+=1
            valor_saque = float(input(print('Qual o valor você deseja sacar?')))
            
            if valor_saque < 0:
                print('Operação invalida')

            elif numero_saque>3:
                print('Você atingiu o seu limite máximo de saque!')
                break

            elif saldo == 0 or saldo<valor_saque:

                print('Saldo insuficiente.')

            elif saldo > 0:
                
                if valor_saque>limite:

                    print('Valor excede o limite de saque')
                
                else:
                    
                    saldo = saldo - valor_saque
                
                    print(f'Após o saque de {valor_saque:.2f} o seu saldo é {saldo:.2f}')


    
    elif opcao == 'e':
        print('#########################################')
        print('Nao tem saldo'if not extrato else extrato)
        print(f' Você possue R$:{saldo:.2f} em sua conta')

    elif opcao == 'q':
        
        print('Sair')
        break