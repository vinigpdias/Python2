#altoritimo fatorial com função

from math import factorial
from tkinter.tix import REAL
from turtle import clear


print(factorial(10))

i = int
result = int(input("digite o número a ser fatorado: "))
n = int(input("digite até qual intervalo: "))

for i in range(1,n):
    result = result * i
    print(result)
