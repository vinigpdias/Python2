#variáreis
from asyncore import read


i = int
n = int
c = int
s = int

n = int(input("digite o total de números: "))
s = 0

for i in range(1,n):
    print("Digite o ", i, "º:")
    c = read()
    s = s + c
    #print(s)
    #print(i)