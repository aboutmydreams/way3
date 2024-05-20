import os
import shutil
import unittest
from io import StringIO
from unittest.mock import patch
from way3 import tree


class TestTreeFunction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.makedirs("test_dir/sub_dir1")
        os.makedirs("test_dir/sub_dir2")
        with open("test_dir/file1.txt", "w") as f:
            f.write("file1")
        with open("test_dir/file2.txt", "w") as f:
            f.write("file2")
        with open("test_dir/sub_dir1/file3.txt", "w") as f:
            f.write("file3")

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree("test_dir")

    @patch("sys.stdout", new_callable=StringIO)
    def test_tree_basic(self, mock_stdout):
        tree("test_dir")
        output = mock_stdout.getvalue().strip()
        expected_output = "\n".join(
            [
                "|-- file1.txt",
                "|-- file2.txt",
                "|-- sub_dir1",
                "|   |-- file3.txt",
                "|-- sub_dir2",
            ]
        )
        self.assertEqual(output, expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_tree_full_path(self, mock_stdout):
        tree("test_dir", full_path=True)
        output = mock_stdout.getvalue().strip()
        expected_output = "\n".join(
            [
                f"|-- {os.path.join('test_dir', 'file1.txt')}",
                f"|-- {os.path.join('test_dir', 'file2.txt')}",
                f"|-- {os.path.join('test_dir', 'sub_dir1')}",
                f"|   |-- {os.path.join('test_dir', 'sub_dir1', 'file3.txt')}",
                f"|-- {os.path.join('test_dir', 'sub_dir2')}",
            ]
        )
        self.assertEqual(output, expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_tree_show_permissions(self, mock_stdout):
        tree("test_dir", show_permissions=True)
        output = mock_stdout.getvalue().strip()
        self.assertIn("|-- ", output)
        self.assertIn(" file1.txt", output)
        self.assertIn(" sub_dir1", output)
