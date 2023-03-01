import socket
#UDP PROTOCOLO DE DATAGRAMAQ DO USUARIO
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente socket criado com sucesso!!")

host = 'localhost'
porta = 5433
mensagem = 'Olá servidor firmeza?'

try:
    print('Cliente : '+ mensagem)
    s.sendto(mensagem.encode(), (host, 5432))# como se empacotasse e enviasse em pacotes UDP

    dados, servidor = s.recvfrom(4096)#4096 bytes de resposta
    dados = dados.decode() # desempacota os dados recebidos
    print('Cliente: ' + dados)
finally:
    print('Cliente: fechando a conexao')
    s.close()