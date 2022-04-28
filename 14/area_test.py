import unittest
from areas import rectangle, triangle, trapezoid

class AreasTestCase(unittest.TestCase):
    def setUp(self):
        self.a = 4
        self.b = 6

    def test_rectangle_with_correct_values(self):
        result = rectangle(self.a, self.b)
        self.assertEqual(result, 24)

    def test_rectangle_with_incorrect_values(self):
        # r = rectangle(4, 'ssss') -- bo dostajemy błąd za wcześnie

        # self.assertRaises(ValueError, rectangle, 4, '***') -- to też zadziała

        with self.assertRaises(ValueError):
            rectangle(4, 'jakiś tekst')

    def test_triangle_with_correct_values(self):
        result = triangle(self.a, self.b)
        self.assertEqual(result, 12)

    def test_triangle_with_incorrect_values(self):
        with self.assertRaises(ValueError):
            triangle('@','a')

    # test raise error

    def test_trapezoid_with_correct_values(self):
        r = trapezoid(self.a, self.b, 5)
        self.assertEqual(r, 25)

    def test_trapezoid_with_incorrect_values(self):
        with self.assertRaises(ValueError):
            trapezoid(4,'@','a')


    # test raise error


    def tearDown(self):
        del self.a
        del self.b

if __name__ == '__main__':
    unittest.main()
