def calculator(a, b, sign):
    if sign == "+":
        return a + b
    elif sign == "-":
        return a - b
    elif sign == "*":
        return a * b
    elif sign == "/":
        if b != 0:
            return a / b
        else:
            return "Ділити на 0 неможливо"
    else:
        return "Некоректна дія"

a = float(input("Перше число: "))
b = float(input("Друге число: "))
sign = input("Дія (+ - * /): ")

result = calculator(a, b, sign)
print("Відповідь:", result)