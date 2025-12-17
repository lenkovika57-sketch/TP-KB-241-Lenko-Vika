from student import Student
from student_list import StudentList
from file_utils import FileUtils


def show_menu():
    print("\n--- Student Phone Book ---")
    print("1. Show all students")
    print("2. Add student")
    print("3. Remove student")
    print("4. Update student")
    print("5. Exit")


def main():
    filename = "lab_03.csv"

    student_list = StudentList()
    student_list.students = FileUtils.load_from_csv(filename)

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            students = student_list.get_all_students()
            if not students:
                print("Student list is empty.")
            else:
                for student in students:
                    print(student)

        elif choice == "2":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")

            student = Student(name, phone, email, address)
            student_list.add_student(student)
            print("Student added successfully.")

        elif choice == "3":
            name = input("Enter name to remove: ")
            if student_list.remove_student(name):
                print("Student removed.")
            else:
                print("Student not found.")

        elif choice == "4":
            name = input("Enter name to update: ")
            phone = input("New phone (leave empty to skip): ")
            email = input("New email (leave empty to skip): ")
            address = input("New address (leave empty to skip): ")

            updated = student_list.update_student(
                name,
                phone if phone else None,
                email if email else None,
                address if address else None
            )

            if updated:
                print("Student updated.")
            else:
                print("Student not found.")

        elif choice == "5":
            FileUtils.save_to_csv(filename, student_list.get_all_students())
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()