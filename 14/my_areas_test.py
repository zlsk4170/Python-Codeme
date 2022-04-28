import unittest
from areas import rectangle, triangle, is_account_active, trapezoid

class AreasTestCase(unittest.TestCase):
    def setUp(self): #tutaj wpisujemy sobie parametry z jakimi chcemy przetestować, robimy to aby nie robić tego ręcznie
        self.a = 4
        self.b = 6
        self.h = 2

    def test_rectangle_with_correct_values(self):
        result = rectangle(self.a,self.b)
        self.assertEqual(result,24)

    def test_rectangle_with_incorrect_values(self):
        # result = rectangle(self.a,'aaa') #tego nie możemy zrobić bo dostajemy błąd za wcześnie
        # self.assertRaises(ValueError,rectangle, 4, "afasd") #mówimy że oczekujemy Value Error na metordzie rectangle z parametrami

        with self.assertRaises(ValueError): #oczekując na assertRaises zrób:
            rectangle(4,'aaaa')

    def test_triangle(self):
        result = triangle(self.a,self.b)
        self.assertEqual(result,12)
        self.assertNotEqual(result,13)
#musimy uruchamiać testy na końcu, bo gdy zrobimy to w danym miejscu w kodzie to wykona to tylko dla fragmentu kodu

    def test_dummy(self):
        state = is_account_active()
        self.assertNotEqual(10,11)
        self.assertTrue(state)

#TDD Test-driven development - najpierw piszemy test, a potem dopiero do tego właściwy kod
    def test_trapezoid(self):
        result = trapezoid(self.a,self.b,self.h)
        self.assertEqual(result,10)


    def tearDown(self): #usuwamy te atrybuty
        del self.a
        del self.b
        del self.h

if __name__ == "__main__":
    unittest.main()