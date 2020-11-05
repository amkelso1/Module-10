import unittest
from class_defs import student as t


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = t.Student('Kelso', 'Alex', 'English', 4.0)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.first_name, 'Alex')
        self.assertEqual(self.student.last_name, 'Kelso')
        self.assertEqual(self.student.major, 'English')
        self.assertEqual(self.student.gpa, 4.0)

    def test_student_str(self):
        student = t.Student('Michael', 'Alex', 'CompSci', 4.0)
        assert student.last_name == 'Michael'
        assert student.first_name == 'Alex'
        assert student.major == 'CompSci'
        assert student.gpa == 4.0

    def test_object_not_created_error_last_name(self):
        self.assertEqual(str(self.student), "Kelso, Alex has major English with gpa: 4.0")

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            stud = t.Student('1234asfas', 'Alex', 'English', 4.0)

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            stud = t.Student('Potter', 'Harry', 'Spell', 4.0)

    def test_object_not_created_error_gps(self):
        with self.assertRaises(ValueError):
            stud = t.Student('Potter', 'Harry', 'Spell', 4.5)


if __name__ == '__main__':
    unittest.main()
