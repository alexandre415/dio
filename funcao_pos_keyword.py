#É OBRIGATORIO  por posição antes da barra, e depois dela pode ser por posição ou keyword
def criar_carro(modelo, ano, placa, / , marca, motor, combustivel): 
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0 Turbo", combustivel="Gasolina")
#VÁLIDO

#criar_carro(modelo="Palio", ano=1999, placa="ABC-4567", marca="Fiat", motor="1.0 Turbo", combustivel="Gasolina")# inválido

#def keyword_only(*, modelo, ano, placa, marca)
#def keyword_and_positional(modelo, ano, / , * , placa, marca)