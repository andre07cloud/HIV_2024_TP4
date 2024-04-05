import unittest
from poly_llm.to_test.find_closest_elements import find_closest_elements

class TestFindClosestElements(unittest.TestCase):
    def test_simple_case(self):
        actual = find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        expected = (2.0, 2.2)
        self.assertEqual(actual, expected)
    
    def test_equal_values(self):
        actual = find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        expected = (2.0, 2.0)
        self.assertEqual(actual, expected)
    
    def test_large_numbers(self):
        actual = find_closest_elements([1e6, 1e7, 1e8, 1e9, 1e10, 1e9+1])
        expected = (1e9, 1e9+1)
        self.assertEqual(actual, expected)
    
    def test_small_numbers(self):
        actual = find_closest_elements([1e-6, 1e-7, 1e-8, 1e-9, 1e-10, 1e-9-1])
        expected = (1e-9, 1e-9-1)
        self.assertEqual(actual, expected)
        
if __name__ == '__main__':
    unittest.main()