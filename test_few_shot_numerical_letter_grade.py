import unittest
from poly_llm.to_test.numerical_letter_grade import numerical_letter_grade

class TestNumericalLetterGrade(unittest.TestCase):
    def test_example(self):
        actual = numerical_letter_grade([4.0, 3, 1.7, 2, 3.5])
        expected = ['A+', 'B', 'C-', 'C', 'A-']
        self.assertEqual(actual, expected)
    
    def test_single_value(self):
        actual = numerical_letter_grade([1.2])
        expected = ['D+']
        self.assertEqual(actual, expected)
    
    def test_multiple_values_below_threshold(self):
        actual = numerical_letter_grade([0.1, 0.2, 0.3, 0.4, 0.5])
        expected = ['E', 'E', 'E', 'E', 'E']
        self.assertEqual(actual, expected)
    
    def test_multiple_values_above_threshold(self):
        actual = numerical_letter_grade([4.1, 4.2, 4.3, 4.4, 4.5])
        expected = ['A+', 'A+', 'A+', 'A+', 'A+']
        self.assertEqual(actual, expected)
        
if __name__ == '__main__':
    unittest.main()