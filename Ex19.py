from timeit import repeat


i = int
a = int
b = int
d = int
resto = int

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

repeat
while resto != 0:
    resto = a % b
    a = b
    b = resto
    print("MDC: ", a)

