i = int
n = int
c = int
s = int
a = int

a = [0,1,2,3,4,5,6,7,8,9,10]


n = int(input("digite o total de números: "))
for i in range(0,n):
    a[i] = int(input("Insira a Nota: "))

s = 0
for i in range(0,n):
    s = s + a[i]

    print(s/n) 
   