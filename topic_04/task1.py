def get_number(prompt):
    "Функція запиту числа з обробкою винятків."
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Помилка: потрібно ввести число!")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    "Функція ділення з обробкою ділення на нуль."
    try:
        return a / b
    except ZeroDivisionError:
        print("Помилка: ділити на нуль не можна!")
        return None

def calculator():
    print("Калькулятор")
    print("Для виходу введіть: exit")

    while True:
        operation = input("\nВведіть операцію: ")

        if operation.lower() == "exit":
            print(" Завершено.")
            break

        if operation not in ['+', '-', '*', '/']:
            print("Невідома операція! Спробуйте ще раз.")
            continue

        num1 = get_number("Введіть перше число: ")
        num2 = get_number("Введіть друге число: ")

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)

        if result is not None:
            print(f"Результат: {result}")

calculator()