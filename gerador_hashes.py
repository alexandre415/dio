import hashlib

string = input(' Digite o texto a ser criado a hash: ')
#resultado  = hashlib.md5(b'Python Security') #o b transforma a str em bytes
resultado  = hashlib.md5(string.encode('utf-8')) #caso nao coloque encode, sera gerado um erro.

print('O hash da string é: ', resultado.hexdigest())

# existe o padrao md5, sha1, sha256 e sha512