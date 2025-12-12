from calc import Calculator

def main():
    calc = Calculator()

    while True:
        try:
            num_1 = float(input("Введіть перше число: ").replace(",", "."))
            num_2 = float(input("Введіть друге число: ").replace(",", "."))
        except ValueError:
            print("Будь ласка, введіть коректне число!")
            continue

        operator = input("Оберіть операцію (+, -, *, /) або x для виходу: ")

        if operator.lower() == "x":
            print("Вихід із програми...")
            break

        match operator:
            case "+":
                result = calc.add(num_1, num_2)
            case "-":
                result = calc.subtract(num_1, num_2)
            case "*":
                result = calc.multiply(num_1, num_2)
            case "/":
                result = calc.divide(num_1, num_2)
            case _:
                result = "Невірний оператор!"

        print("Результат:", result)
        print()

main()