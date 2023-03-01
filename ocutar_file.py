import ctypes

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttibutesW('ocultar.txt', atributo_ocultar)

if retorno:
    print('arquivo foi ocultado')
else:
    print('Arquivo nao foi ocultado')