from way3 import create_file, delete_file

import unittest
import os


class TestFileOp(unittest.TestCase):
    def test_create_file(self):
        result = create_file("./test.txt", "test")
        with open("./test.txt", "r") as f:
            file_content = f.read()
        self.assertEqual(result[0], True, "result fail: expected file")
        self.assertEqual(file_content, "test", "result fail: expected file")
        if os.path.isfile("test.txt"):
            os.remove("test.txt")
            print("test.txt file deleted.")

    def test_delete_file(self):
        result = create_file("./test.txt", "test")
        self.assertEqual(result[0], True, "result fail: expected file")
        delete_file("./test.txt")
        self.assertEqual(
            os.path.isfile("test.txt"), False, "result fail: expected False"
        )
