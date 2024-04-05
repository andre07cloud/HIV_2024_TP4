import unittest
from math import inf, nan
from poly_llm.to_test.closest_integer import closest_integer

class TestClosestInteger(unittest.TestCase):
    """Tests for `closest_integer`."""

    @staticmethod
    def _get_expected_result(input_str):
        try:
            input_float = float(input_str)
            result = int(input_float + 0.5 * abs(input_float)/input_float) \
                if input_float != 0 else 0
        except ValueError as e:
            raise AssertionError('Invalid input string format', e)
        
        return result

    def test_positive_integers(self):
        self._test_helper(['1', '7896'], expected=[1, 7896])

    def test_negative_integers(self):
        self._test_helper(['-1', '-7896'], expected=[-1, -7896])

    def test_floats_within_range(self):
        inputs=['1.1', '1.5', '1.9']
        expected=[1, 2, 2]
        self._test_helper(inputs, expected)

    def test_large_numbers(self):
        large_number='9'+'0'*300+'1.'+'.'*300+'1'
        self._test_helper([large_number], expected=[int(large_number)+1])

    def test_invalid_strings(self):
        with self.assertRaisesRegex(AssertionError, "Invalid input"):
            closest_integer('abc')
            
    def test_edge_cases(self):
        edge_case_tests={
          'inf': inf,
           '-inf': -inf,
              'nan': nan}
        for key in edge_case_tests:
            with self.subTest():
                actual_res = closest_integer(key)
                assert isnan(actual_res), f'"{key}" case failed!'
                
    def _test_helper(self, inputs, expected):
      for idx, val in enumerate(inputs):
          with self.subTest(val=val):
              actual_output = closest_integer(val)
              expected_output = expected[idx]
              error_msg = f'Expected {expected_output}, but got {actual_output}'
              self.assertEqual(actual_output, expected_output, msg=error_msg)
              
if __name__=='__main__':
    unittest.main()