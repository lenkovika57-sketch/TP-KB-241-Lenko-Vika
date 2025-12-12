class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years"

students = [
    Student("Artem", 17),
    Student("Olena", 20),
    Student("Viktoriia", 18),
    Student("Diana", 19)
]

sorted_students = sorted(students, key=lambda s: s.age)

for student in sorted_students:
    print(student)