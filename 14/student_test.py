import unittest
from student import Student
#testujemy email klasy studenta

class StudentTestCase(unittest.TestCase):

    @classmethod #dla całej klasy
    def setUpClass(cls):
        print('-----setUpClass------\n')

    def setUp(self): #przed każdym przypadkiem testowym
        self.student = Student('Anna','Kowalska',4.6,None)

    def test_student_email_created(self):
        student = Student('anna','kowalska',4.6,None)
        self.assertEqual(student.email,'anna.kowalska@university.com')

    def test_student_email_updated(self):
        student = Student('anna','kowalska',4.6,None)
        self.assertEqual(student.email,'anna.kowalska@university.com')

        student.last = 'smith'
        self.assertEqual(student.email,'anna.smith@university.com')

    def test_student_grant_scholarship(self):
        studentB = Student('Bartosz','Bowro',3.0,None)

        self.student.grant_scholarship()
        self.assertTrue(self.student.scholarship)

        studentB.grant_scholarship()
        self.assertFalse(studentB.scholarship)


if __name__ == '__main__':
    unittest.main()