import ipaddress

ip = '192.168.0.1'
rede = '192.168.0.0/24'

net = ipaddress.ip_network(rede, strict=False)

endereco = ipaddress.ip_address(ip)

print(endereco + 256)

print(net)
for i in net:
    print(i)