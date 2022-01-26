i = int
a = int
b = int 
menor = int
mdc = int

a = int(input("Digite um número para a: "))
b = int(input("Digite um número para b: "))

if a > b:
    menor = a

    if not (a > b):
        menor = b

for i in range(2, menor):
    if a % i == 0 and b % i == 0:
        mdc = i
        print ("MDC: ", mdc)
    
    #else:
    #    print("Não há MDC para os números digitados!")