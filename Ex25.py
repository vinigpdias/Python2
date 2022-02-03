def main():
    a = [0,1,2,3,4,5,6,7,8,9]
    i = int
    soma = int

    for i in range(1,4):
        a[i] = int(input("Nota: "))
    soma = 0
    for i in range(1,4):
        soma = soma + a[i]

    print(soma/3)

main()
