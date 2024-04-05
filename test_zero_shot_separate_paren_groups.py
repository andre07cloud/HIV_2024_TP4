import unittest
from poly_llm.to_test.separate_paren_groups import separate_paren_groups

class TestSeperateParenthesisGroups(unittest.TestCase):
    def test_empty_input(self):
        s = ""
        expected = []
        actual = separate_paren_groups(s)
        self.assertListEqual(expected, actual)

    def test_single_group(self):
        s = "(hello)"
        expected = ["(hello)"]
        actual = separate_paren_groups(s)
        self.assertListEqual(expected, actual)

    def test_multiple_groups(self):
        s = "(hi) (world)"
        expected = ["(hi)", "(world)"]
        actual = separate_paren_groups(s)
        self.assertListEqual(expected, actual)

    def test_nested_groups(self):
        s = "((outer) (inner))"
        expected = ["((outer) (inner))"]
        actual = separate_paren_groups(s)
        self.assertListEqual(expected, actual)

    def test_complex_example(self):
        s = "(a)(b(c)d)(efgh)"
        expected = ["(a)", "(b(c)d)", "(efgh)"]
        actual = separate_paren_groups(s)
        self.assertListEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()