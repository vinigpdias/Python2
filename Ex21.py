#Algoritmo Fatorial

n = int
p = int
i = int

n = int(input("digite o número a ser fatorado: "))
p = 4

for i in range(1,n):
    p = p * i
    print(p)
    