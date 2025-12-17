import csv
from student import Student


class FileUtils:
    @staticmethod
    def load_from_csv(filename):
        students = []

        try:
            with open(filename, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    students.append(
                        Student(
                            row["name"],
                            row["phone"],
                            row["email"],
                            row["address"]
                        )
                    )
        except FileNotFoundError:
            pass

        return students

    @staticmethod
    def save_to_csv(filename, students):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["name", "phone", "email", "address"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for student in students:
                writer.writerow(student.to_dict())