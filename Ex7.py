N1 = int(input("Digite o primeiro número: "))
N2 = int(input("Digite o segundo número: "))
N3 = int(input("Digite o terceiro número: "))

N = [N1,N2,N3]
print(N)

if N1 > N2 > N3:
    print("Ordem Crescente: N1 = ", N1, "N2 = ", N2, "N3 = ", N3)

if N1 > N3 > N2:
     print("Ordem Crescente: N1 = ", N1, "N3 = ", N3, "N2 = ", N2)

if N2 > N1 > N3:
     print("Ordem Crescente: N2 = ", N2, "N1 = ", N1, "N3 = ", N3)

if N2 > N3 > N1:
     print("Ordem Crescente: N2 = ", N2, "N3 = ", N3, "N1 = ", N1)

if N3 > N1 > N2:
     print("Ordem Crescente: N3 = ", N3, "N1 = ", N1, "N2 = ", N2)

if N3 > N2 > N1:
     print("Ordem Crescente: N3 = ", N3, "N2 = ", N2, "N3 = ", N3)