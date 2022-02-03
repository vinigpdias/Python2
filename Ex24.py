from turtle import clear


def main() :
    a = [0,1,2,3]

    a[0] = int(input("Nota 1: "))
    a[1] = int(input("Nota 2: "))
    a[2] = int(input("Nota 3: "))
    a[3] = int(input("Nota 4: "))

    print((a[0] + a[1] + a[2] + a[3]) / 4)

main()
