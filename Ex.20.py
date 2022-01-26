#Série de números de uma PA (4,7,10,13,16,19...)

n = int
a = int
b = int
c = int
i = int
s = int

n = int(input("Digite o intervalo da PA que deseja: "))
a = 4

for i in range(1,n):
    a = a + 3
    print(a)
    