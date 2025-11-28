import csv
from sys import argv

def load_students(file_name):
    students = []
    try:
        with open(file_name, "r", newline='', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({
                    "name": row["name"].strip(),
                    "phone": row["phone"].strip(),
                    "email": row["email"].strip(),
                    "address": row["address"].strip()
                })
    except FileNotFoundError:
        print("Файл не знайдено, створюємо порожній довідник...")
    return students

def save_students(file_name, students):
    fieldnames = ["name", "phone", "email", "address"]
    with open(file_name, "w", newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

def add_student(students, name, phone, email, address):
    new_student = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    students.append(new_student)
    return new_student

def find_student(students, name):
    for student in students:
        if student["name"].lower() == name.lower():
            return student
    return None

def remove_student(students, name):
    for student in students:
        if student["name"].lower() == name.lower():
            students.remove(student)
            return True
    return False

def print_menu():
    print("\n--- Телефонний довідник студентів ---")
    print("1. Показати всіх студентів")
    print("2. Додати студента")
    print("3. Знайти студента")
    print("4. Видалити студента")
    print("5. Вийти (і зберегти у CSV)")

def main():
    if len(argv) < 2:
        print("Ви повинні передати CSV файл як параметр командного рядка!")
        print("Наприклад: python lab_02.py lab_02.csv")
        return

    file_name = argv[1]
    students = load_students(file_name)

    while True:
        print_menu()
        choice = input("Ваш вибір: ")

        if choice == "1":
            print("\nСписок студентів:")
            for s in students:
                print(s)

        elif choice == "2":
            name = input("Ім'я: ")
            phone = input("Телефон: ")
            email = input("Email: ")
            address = input("Адреса: ")
            add_student(students, name, phone, email, address)
            print("Студента додано.")

        elif choice == "3":
            name = input("Введіть ім'я для пошуку: ")
            student = find_student(students, name)
            if student:
                print("Знайдено:", student)
            else:
                print("Студента не знайдено.")

        elif choice == "4":
            name = input("Ім'я студента для видалення: ")
            if remove_student(students, name):
                print("Студента видалено.")
            else:
                print("Студента не знайдено.")

        elif choice == "5":
            save_students(file_name, students)
            print("Дані збережено. Вихід.")
            break

        else:
            print("Невірний вибір. Спробуйте ще.")

if __name__ == "__main__":
    main()