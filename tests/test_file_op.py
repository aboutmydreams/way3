from way3 import (
    create_file,
    delete_file,
    read_file,
    read_line,
    insert_to_file,
    modify_line,
    replace_string_in_file,
    replace_string_in_line,
    delete_line,
)

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

    def test_read_file(self):
        file_content = "Hello\nWorld!"
        create_file("./test.txt", file_content)
        info = read_file("test.txt")
        self.assertEqual(info.content, file_content)
        self.assertEqual(info.length, len(file_content))
        self.assertEqual(info.lines, 2)
        self.assertEqual(info.file_type, ".txt")
        delete_file("test.txt")

    def test_read_line(self):
        file_content = "Hello\nWorld!"
        create_file("./test.txt", file_content)
        line = read_line("test.txt", 1)
        self.assertEqual(line, "Hello\n")
        line = read_line("test.txt", 2)
        self.assertEqual(line, "World!")
        delete_file("test.txt")

    def test_insert_to_file(self):
        file_content = "Hello\nWorld!"
        create_file("./test.txt", file_content)
        insert_to_file("./test.txt", "Python\n", 1)
        with open("./test.txt", "r") as f:
            lines = f.readlines()
        self.assertEqual(lines[1], "Python\n")
        delete_file("test.txt")

    def test_modify_line(self):
        file_content = "Hello\nWorld!"
        create_file("./test.txt", file_content)
        modify_line("./test.txt", "Python\n", 0)
        with open("./test.txt", "r") as f:
            lines = f.readlines()
        self.assertEqual(lines[0], "Python\n")
        delete_file("test.txt")

    def test_replace_string_in_file(self):
        file_content = "Hello, Python!"
        create_file("./test.txt", file_content)
        replace_string_in_file("./test.txt", "Python", "World")
        with open("./test.txt", "r") as f:
            file_content = f.read()
        self.assertEqual(file_content, "Hello, World!")
        delete_file("test.txt")

    def test_replace_string_in_line(self):
        file_content = "Hello,\nPython!"
        create_file("./test.txt", file_content)
        replace_string_in_line("./test.txt", 1, "Python", "World")
        with open("./test.txt", "r") as f:
            lines = f.readlines()
        self.assertEqual(lines[1], "World!")
        delete_file("test.txt")

    def test_delete_line(self):
        file_content = "Hello,\nPython!"
        create_file("./test.txt", file_content)
        delete_line("./test.txt", 1)
        with open("./test.txt", "r") as f:
            lines = f.readlines()
        self.assertEqual(len(lines), 1)
        delete_file("test.txt")
