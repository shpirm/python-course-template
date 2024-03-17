import unittest
from app.io.output import output_to_console, write_to_file_builtin

class TestOutput(unittest.TestCase):
    data_source = 'data/'

    def test_write_to_file_builtin(self):
        expected = "Test text"
        write_to_file_builtin(TestOutput.data_source + "test_output.txt", expected)

        with open(TestOutput.data_source + "test_output.txt", "r") as file:
            content = file.read()

        self.assertEqual(content, expected + "\n")
