import unittest
from poly_llm.to_test.separate_paren_groups import separate_paren_groups

class TestSeparateParenGroups(unittest.TestCase):
    def test_example(self):
        actual = separate_paren_groups('( ) (( )) (( )( ))')
        expected = ['()', '(())', '(()())']
        self.assertEqual(actual, expected)
    
    def test_nested_parenthesis(self):
        actual = separate_paren_groups('(()()) ((())) () ((())()())')
        expected = ['(()())', '((()))', '()', '((())()())']
        self.assertEqual(actual, expected)
    
    def test_balanced_parenthesis(self):
        actual = separate_paren_groups('() (()) ((())) (((())))')
        expected = ['()', '(())', '((()))', '(((())))']
        self.assertEqual(actual, expected)
    
    def test_empty_string(self):
        actual = separate_paren_groups('')
        expected = []
        self.assertEqual(actual, expected)
    
    def test_only_open_parens(self):
        actual = separate_paren_groups('((((')
        expected = []
        self.assertEqual(actual, expected)
        
    def test_only_close_parens(self):
        actual = separate_paren_groups('))))')
        expected = []
        self.assertEqual(actual, expected)
        
if __name__ == '__main__':
    unittest.main()