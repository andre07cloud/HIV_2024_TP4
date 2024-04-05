import unittest
from poly_llm.to_test.numerical_letter_grade import numerical_letter_grade
class TestNumericalLetterGrade(unittest.TestCase):
    # Check whether it handles all possible cases correctly
    def test_numerical_letter_grade(self):
        self.assertEqual(numerical_letter_grade([4.0]), ["A+"])
        self.assertEqual(numerical_letter_grade([3.8]), ["A"])
        self.assertEqual(numerical_letter_grade([3.6]), ["A-"])
        self.assertEqual(numerical_letter_grade([3.2]), ["B+"])
        self.assertEqual(numerical_letter_grade([2.9]), ["B"])
        self.assertEqual(numerical_letter_grade([2.6]), ["B-"])
        self.assertEqual(numerical_letter_grade([2.2]), ["C+"])
        self.assertEqual(numerical_letter_grade([1.9]), ["C"])
        self.assertEqual(numerical_letter_grade([1.6]), ["C-"])
        self.assertEqual(numerical_letter_grade([1.2]), ["D+"])
        self.assertEqual(numerical_letter_grade([0.9]), ["D"])
        self.assertEqual(numerical_letter_grade([0.6]), ["D-"])
        self.assertEqual(numerical_letter_grade([0.0]), ["E"])
        
if __name__ == "__main__":
    unittest.main()