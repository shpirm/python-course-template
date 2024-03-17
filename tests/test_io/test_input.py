import unittest
import pandas as pd
from app.io.input import read_from_file_builtin, read_from_file_pandas

class TestInput(unittest.TestCase):
    data_source = 'data/'

    def test_read_from_file_builtin(self):
        expected = "Test text"
        test_filename = TestInput.data_source + "test.txt"

        with open(test_filename, "w") as file:
            file.write(expected)
        result = read_from_file_builtin(test_filename)

        self.assertEqual(result, expected)

    def test_read_from_file_pandas(self):
        expected = "Test text"
        test_filename = TestInput.data_source + "test.csv"

        with open(test_filename, "w") as file:
            file.write(expected)
        result = read_from_file_pandas(test_filename)

        self.assertEqual(result.strip(), expected)

    def test_read_from_file_builtin_empty(self):
        test_filename = TestInput.data_source + "test_empty.txt"

        with open(test_filename, "w") as file:
            file.write("")
        result = read_from_file_builtin(test_filename)

        self.assertEqual(result, "")

    def test_read_from_file_pandas_empty_csv(self):
        test_filename = TestInput.data_source + "test_empty.csv"

        with open(test_filename, "w") as file:
            file.write("")
        try:
            result = read_from_file_pandas(test_filename)
            self.assertEqual(result.strip(), "")

        except pd.errors.EmptyDataError: # Немає стовпців = обробка помилки
            self.assertTrue(True)

    def test_read_from_file_builtin_nonexistent(self):
        with self.assertRaises(FileNotFoundError):
            read_from_file_builtin(TestInput.data_source + "nonexistent.txt")

    def test_read_from_file_pandas_nonexistent(self):
        with self.assertRaises(FileNotFoundError):
            read_from_file_pandas(TestInput.data_source + "nonexistent.csv")

