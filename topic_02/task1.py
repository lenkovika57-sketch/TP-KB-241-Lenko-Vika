import math

def discr(a, b, c):
    return b * b - 4 * a * c

def quadratic_roots(a, b, c):
    D = discr(a, b, c)
    print("Дискримінант =", D)

    if D < 0:
        print("Коренів немає")
    elif D == 0:
        x = -b / (2 * a)
        print("Один корінь: x =", x)
    else:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print("Два корені: x1 =", x1, "x2 =", x2)

a = int(input("Введіть A: "))
b = int(input("Введіть B: "))
c = int(input("Введіть C: "))

quadratic_roots(a, b, c)