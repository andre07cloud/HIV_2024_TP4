import unittest
from poly_llm.to_test.closest_integer import closest_integer

class TestClosestInteger(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(closest_integer("10"), 10)
        self.assertEqual(closest_integer("15.3"), 15)
        self.assertEqual(closest_integer("14.5"), 15)
        self.assertEqual(closest_integer("-14.5"), -15)

    def test_edge_cases(self):
        self.assertEqual(closest_integer(".4"), 0)
        self.assertEqual(closest_integer("-.4"), 0)
        self.assertEqual(closest_integer("1."), 1)
        self.assertEqual(closest_integer("-1."), -1)

    def test_invalid_values(self):
        with self.assertRaises(ValueError):
            _ = closest_integer("not a number")

if __name__ == "__main__":
    unittest.main()