def salvar_carro(marca, modelo, ano, placa):
    #salva carro no banco de dados
    print(f"Carro inserido com sucesso!{marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat","147", "1971", "ABC-4321")
salvar_carro(marca="Fiat", modelo="147", ano="1972", placa="ABC-5432")
salvar_carro(**{"marca":"Fiat", "modelo": "147", "ano": "1987", "placa": "ABC-2938"})

#Com ** diz que vc esta passando um dicionario como argumento. **kwargs
#Somente um * siginifica que esta passando uma tupla.  *args