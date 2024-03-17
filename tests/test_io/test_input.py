import unittest
from app.io.input import read_from_file_builtin, read_from_file_pandas

class TestInput(unittest.TestCase):
    data_source = 'data/'

    def test_read_from_file_builtin(self):
        expected = "Test text"
        with open(TestInput.data_source + "test.txt", "w") as file:
            file.write(expected)
        result = read_from_file_builtin(TestInput.data_source + "test.txt")
        self.assertEqual(result, expected)
