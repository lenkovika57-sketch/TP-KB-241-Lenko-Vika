
def calculator(a, b, sign):
    match sign:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b != 0:
                return a / b
            else:
                return "Ділити на 0 неможливо"
        case _:
            return "Некоректна дія"

while True:
    print("\nКалькулятор")
    command = input("Введіть 'x' щоб вийти або Enter щоб продовжити: ").strip().lower()
    if command == "x":
        print("Програма завершена.")
        break

    a = float(input("Перше число: "))
    b = float(input("Друге число: "))
    sign = input("Дія (+ - * /): ")

    result = calculator(a, b, sign)
    print("Відповідь:", result)