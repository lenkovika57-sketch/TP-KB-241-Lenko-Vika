import pytest
from lab_02 import load_students, add_student, find_student, remove_student

def test_add_student():
    students = []
    add_student(students, "Diana", "093678427", "diana56@mail.com", "Chernihiv")
    assert len(students) == 1
    assert students[0]["name"] == "Diana"
    assert students[0]["phone"] == "093678427"
    assert students[0]["email"] == "diana56@mail.com"
    assert students[0]["address"] == "Chernihiv"

def test_find_student_found():
    students = [{"name": "Olena", "phone": "0965573212", "email": "olena50@mail.com", "address": "Chernihiv"}]
    student = find_student(students, "Olena")
    assert student is not None
    assert student["phone"] == "0965573212"

def test_find_student_not_found():
    students = [{"name": "Olena", "phone": "0965573212", "email": "olena50@mail.com", "address": "Chernihiv"}]
    student = find_student(students, "Masha")
    assert student is None

def test_remove_student_found():
    students = [{"name": "Masha", "phone": "0954312366", "email": "masha00@mail.com", "address": "Chernihiv"}]
    result = remove_student(students, "Masha")
    assert result is True
    assert len(students) == 0

def test_remove_student_not_found():
    students = [{"name": "Masha", "phone": "0954312366", "email": "masha00@mail.com", "address": "Chernihiv"}]
    result = remove_student(students, "Olena")
    assert result is False
    assert len(students) == 1

def test_load_students(tmp_path):
    csv_file = tmp_path / "test.csv"
    csv_file.write_text("name,phone,email,address\nEugene,0509803455,eugene67@mail.com,Chernihiv\nDiana,093678427,diana56@mail.com,Chernihiv\n", encoding="utf-8")
    
    students = load_students(str(csv_file))
    assert len(students) == 2
    assert students[0]["name"] == "Eugene"
    assert students[0]["phone"] == "0509803455"
    assert students[1]["name"] == "Diana"
    assert students[1]["phone"] == "093678427"