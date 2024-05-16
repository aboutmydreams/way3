from way3 import get_current_dir, get_files_in_directory

import unittest


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
