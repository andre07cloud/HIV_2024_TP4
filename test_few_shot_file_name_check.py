import unittest
from poly_llm.to_test.file_name_check import file_name_check

class TestFileChecker(unittest.TestCase):
    def test_valid_names(self):
        self.assertEqual(file_name_check("example.txt"), "Yes")
        self.assertEqual(file_name_check("myfile.exe"), "Yes")
        self.assertEqual(file_name_check("test1.dll"), "Yes")

    def test_no_dot(self):
        self.assertEqual(file_name_check("nofileextension"), "No")
        self.assertEqual(file_name_check("nodotatend."), "No")

    def test_too_many_digits(self):
        self.assertEqual(file_name_check("t00much1.txt"), "No")
        self.assertEqual(file_name_check("alsonotalph4numeric.dll"), "No")

    def test_bad_start(self):
        self.assertEqual(file_name_check("1startwithnumber.doc"), "No")
        self.assertEqual(file_name_check("@specialchars.pdf"), "No")

    def test_wrong_suffix(self):
        self.assertEqual(file_name_check("wrongsuf.png"), "No")
        self.assertEqual(file_name_check("alsowrong.jpeg"), "No")

if __name__ == "__main__":
    unittest.main()