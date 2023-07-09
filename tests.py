import unittest
from unittest.mock import patch
import main

class TestYourScript(unittest.TestCase):
    @patch('builtins.input')
    def test_fetch_code_file_exit(self, input_mock):
        input_mock.return_value = 'exit'
        result = main.fetch_code_file('exit')
        self.assertEqual(result, (None, None, None, None))

    @patch('main.format_prompt', return_value=('fake_prompt', 'fake_question'))
    @patch('builtins.input', return_value='1')
    def test_fetch_code_file_select_first(self, format_prompt_mock, input_mock):
        result = main.fetch_code_file('test_dir')
        self.assertEqual(result[1].split('/')[-1], 'hello_world.cpp')
        self.assertEqual(result[3], 'C++')

    @patch('builtins.input', return_value='What does this function do?')
    def test_format_prompt(self, input_mock):
        selected_file = 'test.py'
        result_prompt, result_question = main.format_prompt(selected_file)
        self.assertEqual(result_question, 'What does this function do?')
        self.assertIsInstance(result_prompt, main.PromptTemplate)

if __name__ == '__main__':
    unittest.main()
