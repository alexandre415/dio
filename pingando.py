import os
print('#' * 60)
ip_ou_host = input("Digite o ip que voce deseja: ")

print('#' * 60)

os.system(f'ping -n 6 {ip_ou_host}')

print('#' * 60)