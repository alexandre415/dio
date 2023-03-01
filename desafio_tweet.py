"""T = input()

if (len(T) <=1 or len(T)<=140):
    print('tweet')
elif len(T)>140:
    print('MUTE')
month = int(input())

months_dict = {1:'january',2:'february',3:'march',4:'april',5:'may',6:'june',7:'july',8:'august',
9:'september', 10:'october',11:'november', 12: 'december'}


print(months_dict[month])"""
N = int(input())

while (N > 0):
    A, B = input().split(" ")
    if A.endswith(B): # se o numero B termina com o de A
        print("encaixa")
    else:
        print("nao encaixa")
    N -= 1
