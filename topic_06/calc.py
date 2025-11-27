from functions import add, sub, mul, div, log
from operations import get_numbers, get_operation

operation = get_operation()
a, b = get_numbers()

if operation == "+":
    result = add(a, b)
elif operation == "-":
    result = sub(a, b)
elif operation == "*":
    result = mul(a, b)
elif operation == "/":
    result = div(a, b)
else:
    result = "Невідома операція!"
    log(f"Помилка: введена невідома операція '{operation}'")

print("Результат:", result)
log(f"Фінальний результат: {result}")