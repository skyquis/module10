#This program will unit thest the student class and see if it performs input validation on first name, last name, major, and GPA values

import unittest
from class_definitions import Student as s


class MyTestCase(unittest.TestCase): #defining unit test
    def setUp(self): #standard setup
        self.student = s('Marquis', 'Skyler','Mechanical Engineering')

    def tearDown(self): #standard tear down
        del self.student

    def test_object_created_required_attributes(self): #testing that student class has created the required attributes
        self.assertEqual(self.student.last_name, 'Marquis')
        self.assertEqual(self.student.first_name, 'Skyler')
        self.assertEqual(self.student.major, 'Mechanical Engineering')

    def test_object_created_all_attributes(self): #testing that student class has created all attributes
        student = s('Marquis', 'Skyler', 'Mechanical Engineering',3.0) # this is not self.student from setUp, but local
        assert student.last_name == 'Marquis'                 # note no self here on student or assert
        assert student.first_name == 'Skyler'
        assert student.major == 'Mechanical Engineering'
        assert student.gpa == 3.0

    def test_person_str(self): #testing string method in student class
        self.assertEqual(str(self.student), 'Marquis, Skyler has major Mechanical Engineering with gpa: 0.0')

    #defining value error tests for last name, first name, major, and gpa
    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = s('123', 'Skyler', 'Mechanical Engineering')

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            p = s('Marquis', '123', 'Mechanical Engineering')

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            p = s('Marquis', 'Skyler', '123')

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            p = s('Marquis', 'Skyler', 'Mechanical Engineering',5)

if __name__ == '__main__':
    unittest.main()
