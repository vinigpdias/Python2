#Algoritmo Fatorial

n = int
p = int
i = int

p = int(input("digite o número a ser fatorado: "))
n = int(input("digite até qual intervalo: "))


for i in range(1,n):
    p = p * i
    print(p)
    