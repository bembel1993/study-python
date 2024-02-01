from math import sqrt

a = int(input("Введите число:\n "))

if a % 2 != 0:
    print(a)
    print("Нечетное\n")
elif a % 2 == 0:
    print(a)
    print("Четное")