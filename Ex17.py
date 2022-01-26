i = int
a = int
b = int
c = int
s = int

a = int(input("Digite um número: "))
b = int(input("Digite um segundo número: "))
c = int(input("Digite o terceiro número: "))
s = 0
   
if a > b > c:
    print("O primeiro número é o maior!", a)
if b > a > c:
    print("O segundo número é maior!", b)
if c > a > b:
    print("O terceiro número é maior!", c)