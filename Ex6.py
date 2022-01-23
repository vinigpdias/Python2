N1 = int(input("Digite o primeiro número: "))
N2 = int(input("Digire o segundo número: "))

teste_1 = (N1 > 0) and (N2 > 0)
teste_2 = (N1 % 2 == 1) and (N2 % 2 == 1)

if teste_1:
    print("Azul")

if teste_2:
    print("Laranja")

else:
    print("Roxo")