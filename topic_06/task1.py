from operator import itemgetter

students = [
    {"name": "Вікторія", "grade": 93},
    {"name": "Олена", "grade": 90},
    {"name": "Діана", "grade": 87},
    {"name": "Марія", "grade": 83}
]

print("Початковий список:")
print(students)

sorted_by_name = sorted(students, key=lambda x: x["name"])
print("\nСортування за ім’ям:")
print(sorted_by_name)

sorted_by_grade = sorted(students, key=lambda x: x["grade"])
print("\nСортування за оцінкою:")
print(sorted_by_grade)