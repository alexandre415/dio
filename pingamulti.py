import os
import time

with open('hosts.txt') as file:
    
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print(ip)

        os.system('ping ' + ip)
        time.sleep(5)