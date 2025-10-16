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

a = float(input("Перше число: "))
b = float(input("Друге число: "))
sign = input("Дія (+ - * /): ")

result = calculator(a, b, sign)
print("Відповідь:", result)