import unittest
from app.io.output import output_to_console, write_to_file_builtin

class TestOutput(unittest.TestCase):
    data_source = 'data/'

    def test_write_to_file_builtin(self):
        expected = "Test text"
        test_filename = TestOutput.data_source + "test_output.txt"

        write_to_file_builtin(test_filename, expected)

        with open(test_filename, "r") as file:
            content = file.read()

        self.assertEqual(content, expected + "\n")
