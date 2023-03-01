import hashlib

arq1 = 'a.txt'
arq2 = 'b.txt'

hash1 = hashlib.new('ripemd160')

hash1.update(open(arq1, 'rb').read())

hash2 = hashlib.new('ripemd160')

hash2.update(open(arq2, 'rb').read()) # rb é read binary ele le no formato binario

#função digest traz um resumo da saida do update acima.
if hash1.digest() != hash2.digest():

    print(f'O arquivo {arq1} é diferente do arquivo {arq2}')
    print('O hash do arquivo a.txt é: ', hash1.hexdigest())# transforma em hexa o resumo do hash1
    print('O hash do arquivo b.txt é: ', hash2.hexdigest())# transforma em hexa o resumo do hash1

else:

    print('Os arquivos sao iguais!')
    print('O hash do arquivo a.txt é: ', hash1.hexdigest())# transforma em hexa o resumo do hash1
    print('O hash do arquivo b.txt é: ', hash2.hexdigest())# transforma em hexa o resumo do hash1


