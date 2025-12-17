from student import Student


class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Can only add Student objects")
        self.students.append(student)

    def remove_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                return True
        return False

    def find_student(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def update_student(self, name, phone=None, email=None, address=None):
        student = self.find_student(name)
        if not student:
            return False

        if phone is not None:
            student.phone = phone
        if email is not None:
            student.email = email
        if address is not None:
            student.address = address

        return True

    def get_all_students(self):
        return self.students