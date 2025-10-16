students = [
    {"name": "Artem", "phone": "0665234567", "email": "artem45@mail.com", "address": "Chernihiv"},
    {"name": "Bogdan", "phone": "0638834567", "email": "bogdan78@mail.com", "address": "Chernihiv"},
    {"name": "Ilya", "phone": "0931234000", "email": "ilya33@mail.com", "address": "Chernihiv"},
    {"name": "Victoria", "phone": "0667834567", "email": "vika21@mail.com", "address": "Chernihiv"}
]

def printAllList():
    print("\n=== STUDENT DIRECTORY ===")
    for elem in students:
        print(f"Name: {elem['name']}, Phone: {elem['phone']}, Email: {elem['email']}, Address: {elem['address']}")
    print("==========================\n")

def addNewElement():
    name = input("Enter student name: ")
    phone = input("Enter student phone: ")
    email = input("Enter student email: ")
    address = input("Enter student address: ")

    newItem = {"name": name, "phone": phone, "email": email, "address": address}

    insertPosition = 0
    for item in students:
        if name.lower() > item["name"].lower():
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)
    print("New student added.\n")

def deleteElement():
    name = input("Enter name to delete: ")
    deletePosition = -1
    for item in students:
        if name.lower() == item["name"].lower():
            deletePosition = students.index(item)
            break
    if deletePosition == -1:
        print("Student not found.\n")
    else:
        del students[deletePosition]
        print("Student deleted.\n")

def updateElement():
    name = input("Enter the name of the student to update: ").strip()
    found_index = -1

    for i in range(len(students)):
        if students[i]["name"].lower() == name.lower():
            found_index = i
            break

    if found_index == -1:
        print("Student not found.\n")
        return

    found = students[found_index]
    print(f"Editing {found['name']}...")

    new_name = input(f"Enter new name (press Enter to keep '{found['name']}'): ").strip() or found['name']
    new_phone = input(f"Enter new phone (press Enter to keep '{found['phone']}'): ").strip() or found['phone']
    new_email = input(f"Enter new email (press Enter to keep '{found['email']}'): ").strip() or found['email']
    new_address = input(f"Enter new address (press Enter to keep '{found['address']}'): ").strip() or found['address']

    del students[found_index]

    new_item = {
        "name": new_name,
        "phone": new_phone,
        "email": new_email,
        "address": new_address
    }
    students.insert(found_index, new_item)

    print("Student information updated (without sorting).\n")

def main():
    while True:
        choice = input("Choose action [C-create, U-update, D-delete, P-print, X-exit]: ").strip().lower()
        if choice == "c":
            addNewElement()
        elif choice == "u":
            updateElement()
        elif choice == "d":
            deleteElement()
        elif choice == "p":
            printAllList()
        elif choice == "x":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == "__main__":
    main()