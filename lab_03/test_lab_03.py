import unittest
from student import Student
from student_list import StudentList


class TestStudent(unittest.TestCase):

    def test_create_student(self):
        student = Student(
            "Viktoriia Lenko",
            "0664455667",
            "vikalenko8@gmail.com",
            "Chernihiv"
        )
        self.assertEqual(student.name, "Viktoriia Lenko")
        self.assertEqual(student.phone, "0664455667")
        self.assertEqual(student.email, "vikalenko8@gmail.com")
        self.assertEqual(student.address, "Chernihiv")


class TestStudentList(unittest.TestCase):

    def setUp(self):
        self.student_list = StudentList()
        self.student = Student(
            "Viktoriia Lenko",
            "0664455667",
            "vikalenko8@gmail.com",
            "Chernihiv"
        )

    def test_add_student(self):
        self.student_list.add_student(self.student)
        self.assertEqual(len(self.student_list.students), 1)

    def test_find_student(self):
        self.student_list.add_student(self.student)
        found = self.student_list.find_student("Viktoriia Lenko")
        self.assertIsNotNone(found)

    def test_remove_student(self):
        self.student_list.add_student(self.student)
        result = self.student_list.remove_student("Viktoriia Lenko")
        self.assertTrue(result)
        self.assertEqual(len(self.student_list.students), 0)

    def test_update_student(self):
        self.student_list.add_student(self.student)
        result = self.student_list.update_student(
            "Viktoriia Lenko",
            phone="0999999999",
            email="new@gmail.com",
            address="Kyiv"
        )
        self.assertTrue(result)
        self.assertEqual(self.student.phone, "0999999999")
        self.assertEqual(self.student.email, "new@gmail.com")
        self.assertEqual(self.student.address, "Kyiv")

    def test_update_non_existing_student(self):
        result = self.student_list.update_student("Unknown")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()