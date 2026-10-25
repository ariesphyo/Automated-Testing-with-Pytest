import pytest

from src.student_manager import Student, StudentManager


@pytest.fixture
def empty_manager():
    return StudentManager()


@pytest.fixture
def sample_student():
    return Student("S001", "Ada Lovelace", "ada@example.com")


@pytest.fixture
def populated_manager():
    manager = StudentManager()
    students = [
        ("S001", "Ada Lovelace", "ada@example.com", 95),
        ("S002", "Grace Hopper", "grace@example.com", 75),
        ("S003", "Katherine Johnson", "katherine@example.com", 55),
    ]
    for student_id, name, email, score in students:
        student = manager.add_student(student_id, name, email)
        student.add_grade("MATH101", score)
    return manager


@pytest.fixture
def valid_registration_data():
    return {
        "username": "ada_lovelace",
        "email": "ada@example.com",
        "password": "Strong1!Pass",
        "age": 25,
    }
