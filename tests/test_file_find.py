from way3 import get_current_dir

import unittest


class TestFileFind(unittest.TestCase):
    def test_result(self):
        result = get_current_dir(__file__)
        print(result)
        self.assertIn("way3/tests", result, "result fail: expected file")
