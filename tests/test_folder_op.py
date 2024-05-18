from way3 import create_directory, rename_directory, delete_directory

import unittest
import shutil
import os


class TestDirectoryOp(unittest.TestCase):
    def test_create_directory(self):
        result = create_directory("test_dir")
        self.assertEqual(
            result,
            os.path.join(os.getcwd(), "test_dir"),
            "result fail: expected directory",
        )
        self.assertTrue(
            os.path.exists("test_dir"), "result fail: directory not created"
        )
        if os.path.exists("test_dir"):
            shutil.rmtree("test_dir")
            print("test_dir deleted.")

    def test_rename_directory(self):
        create_directory("test_dir")
        result = rename_directory("test_dir", "new_test_dir")
        self.assertEqual(
            result,
            os.path.join(os.getcwd(), "new_test_dir"),
            "result fail: expected directory",
        )
        self.assertTrue(
            os.path.exists("new_test_dir"), "result fail: directory not renamed"
        )
        if os.path.exists("new_test_dir"):
            shutil.rmtree("new_test_dir")
            print("new_test_dir deleted.")

    def test_delete_directory(self):
        create_directory("test_dir")
        result = delete_directory("test_dir")
        self.assertEqual(
            result,
            os.path.join(os.getcwd(), "test_dir"),
            "result fail: expected directory",
        )
        self.assertFalse(
            os.path.exists("test_dir"), "result fail: directory not deleted"
        )
