import unittest
from app import grade_scale

class TestGradeScale(unittest.TestCase):

    def test_A_grade(self):
        self.assertEqual(grade_scale(90), 'A')

    def test_B_grade(self):
        self.assertEqual(grade_scale(80), 'B') 

    def test_C_grade(self):
        self.assertEqual(grade_scale(70), 'C')  

    def test_D_grade(self):
        self.assertEqual(grade_scale(60), 'D')  

    def test_E_grade(self):
        self.assertEqual(grade_scale(50), 'E')  

    def test_FX_grade(self):
        self.assertEqual(grade_scale(40), 'FX')  

    def test_F_grade(self):
        self.assertEqual(grade_scale(20), 'F')  

    def test_invalid_score(self):
        self.assertEqual(grade_scale(-5), 'Invalid score')  


if __name__ == "__main__":
    unittest.main()
