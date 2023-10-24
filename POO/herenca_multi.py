class Veiculo:
    
    def __init__(self,cor, placa, numero_de_rodas) -> None:
        
        self.cor = cor 
        self.placa = placa
        self.numero_de_rodas = numero_de_rodas

    def ligar_motor(self):
        print("Ligando motor...")

    def __str__(self):
        return self.cor
    
    
class Motocicleta(Veiculo):
    pass
class Carro(Veiculo):
    pass
class Caminhao(Veiculo):

    def __init__(self, cor, placa, numero_de_rodas, carregado) -> None:
        super().__init__(cor, placa, numero_de_rodas)
        self.carregado = carregado

    def esta_carregado(self):

        print(f"{'Sim' if self.carregado else 'Não'} esta carregado")
       

moto = Motocicleta("preta", "abc-1234", 2)
moto.ligar_motor()

carro = Carro("Branco", "xde-3000", 4)
carro.ligar_motor()

caminhao = Caminhao("roxo", "dsf-92183", 8, False)

caminhao.esta_carregado()
print(caminhao)
