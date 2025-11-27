from functions import add, sub, mul, div
from operations import get_numbers, get_operation

op = get_operation()
a, b = get_numbers()

if op == "+":
    print("Результат:", add(a, b))
elif op == "-":
    print("Результат:", sub(a, b))
elif op == "*":
    print("Результат:", mul(a, b))
elif op == "/":
    print("Результат:", div(a, b))
else:
    print("Невідома операція!")