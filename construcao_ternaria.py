saldo = 500
saque = 100

status = "Sucesso" if saldo >= saque else "Saldo insuficiente"

print(f'{status} ao realizar o saque!')