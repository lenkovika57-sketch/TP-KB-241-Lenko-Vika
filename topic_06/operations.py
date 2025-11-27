from functions import log

def get_numbers():
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    log(f"Введені числа: a={a}, b={b}")
    return a, b

def get_operation():
    operation = input("Оберіть операцію (+, -, *, /): ")
    log(f"Вибрана операція: {operation}")
    return operation