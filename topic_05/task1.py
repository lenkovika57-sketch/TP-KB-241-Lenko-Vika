import random

options = ["stone", "scissor", "paper"]

user = input("Введіть свій вибір (stone / scissor / paper): ").lower()

if user not in options:
    print("Помилка! Невірне значення.")
else:
    computer = random.choice(options)
    print(f"Комп’ютер вибрав: {computer}")

    if user == computer:
        print("Нічия!")
    elif (user == "stone" and computer == "scissor") or \
         (user == "scissor" and computer == "paper") or \
         (user == "paper" and computer == "stone"):
        print("Ви перемогли!")
    else:
        print("Комп’ютер переміг!")