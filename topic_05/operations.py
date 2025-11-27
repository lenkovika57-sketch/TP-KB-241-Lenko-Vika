def get_numbers():
    a = float(input("Введіть перше число: "))
    b = float(input("Введіть друге число: "))
    return a, b

def get_operation():
    print("Оберіть операцію: +  -  *  /")
    return input("Введіть операцію: ")