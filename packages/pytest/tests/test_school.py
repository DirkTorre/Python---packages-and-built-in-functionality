import pytest

from source.school import Classroom, Teacher, Student, TooManyStudents


"""
Made with chatgpt using the command:

'Using pytest and the functions that come from it.
Such as fixtures, parameters, raises and mark, where necessary.
Test the following code, where ever necessary.
Test the following code and theme it Harry Potter: <the code to test>'

NOTE: It did not test for:
    - An overflow of students (11 students)
    - If the names are correct (but to be fair, that's a stupid test.)

Copilot gave this comment:

In this magical test suite:

- We create a harry_potter_teacher fixture representing Professor Snape.
- The hogwarts_students fixture provides a list of three iconic students: Harry Potter, Hermione Granger, and Ron Weasley.
- The test_add_students function tests the add_students method by adding students to the classroom.
- The test_remove_student function tests the remove_student method by removing Hermione Granger from the classroom.
Remember to cast the Alohomora spell (run pytest) to unlock the magic of testing! 🪄✨

"""

# Fixtures
@pytest.fixture
def harry_potter_teacher():
    return Teacher("Professor Snape")

@pytest.fixture
def hogwarts_students():
    return [
        Student("Harry Potter"),
        Student("Hermione Granger"),
        Student("Ron Weasley"),
    ]

# Tests
def test_add_students(harry_potter_teacher, hogwarts_students):
    classroom = Classroom(harry_potter_teacher, [], "Defense Against the Dark Arts")
    for student in hogwarts_students:
        classroom.add_students(student)
    assert len(classroom.students) == 3

def test_remove_student(harry_potter_teacher, hogwarts_students):
    classroom = Classroom(harry_potter_teacher, hogwarts_students, "Potions")
    classroom.remove_student("Hermione Granger")
    assert len(classroom.students) == 2
    assert "Hermione Granger" not in [student.name for student in classroom.students]
