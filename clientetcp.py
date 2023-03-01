import socket # faz relacionamento da placa de rede e o SO
import sys # fornece acesso a algumas variaveis que tem forte interação com o interpretador

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    
    except socket.error as e:

        print('A conexao falhou!')
        print(f'Erro: {e}')
        sys.exit()

    print("socket criado com sucesso!!")

    HostAlvo = input("Digite o host a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print("Cliente com tcp conectado com sucesso!!")
        s.shutdown(2)

    except socket.error as e:
        print("Nao foi possivel conectar ao host")

        print(f"erro é {e}")
        sys.exit()

if __name__ == "__main__":
    main()