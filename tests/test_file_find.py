from way3 import (
    get_current_dir,
    get_files_in_directory,
    get_directory_structure,
    get_directory_folder_list,
    get_directory_file_list,
)

import unittest
import os


class TestFileFind(unittest.TestCase):
    def test_result(self):
        result = get_current_dir(__file__)
        self.assertIn("way3/tests", result, "result fail: expected file")

    def test_get_files_in_directory(self):
        current_directory = "tests"  # 当前目录
        files = get_files_in_directory(current_directory)
        self.assertIn(
            "tests/test_file_find.py", files, "result fail: expected test_file_find.py"
        )
        self.assertEqual(len(files) > 1, True, "result fail: expected > 3")

    def test_directory_structure(self):
        # 示例：获取当前文件夹的目录结构
        directory_structure = get_directory_structure(os.getcwd() + "/tests")
        self.assertIn(
            "dirs",
            list(directory_structure[get_current_dir(__file__)].keys()),
            "result fail: expected dirs",
        )
        self.assertEqual(
            list,
            type(directory_structure[get_current_dir(__file__)]["dirs"]),
            "result fail: expected dirs",
        )
        self.assertIn(
            "files",
            list(directory_structure[get_current_dir(__file__)].keys()),
            "result fail: expected files",
        )
        self.assertEqual(
            list,
            type(directory_structure[get_current_dir(__file__)]["files"]),
            "result fail: expected files",
        )

    def test_get_directory_folder_list(self):
        directory_list = get_directory_folder_list(os.getcwd())
        self.assertIn(
            "tests", directory_list, "result fail: not find tests in directory_list"
        )

    def test_get_directory_file_list(self):
        file_list = get_directory_file_list(os.getcwd())
        self.assertIn(
            "LICENSE", file_list, "result fail: not find LICENSE in file_list"
        )
