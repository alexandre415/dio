class bicicleta:
    
    def __init__(self, cor, modelo, ano, valor):
        
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("blim blim...")

    def correr(self):

        print("vrrummm....")

    def parar(self):
        print("Bicicleta parando..")
        print("Bicicleta parada!")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' 
    for chave, valor in self.__dict__.items()])}"


b1 = bicicleta("azul", "mountain bike", 2023, 5000)

b1.buzinar()
b1.correr()
b1.parar()

print(b1.ano, b1.cor, b1.modelo, b1.valor)