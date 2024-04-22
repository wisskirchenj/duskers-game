import unittest
from io import StringIO
from unittest.mock import patch, MagicMock

from duskers.menu import Menu, LOOP, EXIT


class TestMenu(unittest.TestCase):

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_initialized_with_valid_parameters(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_input.side_effect = ['1']
        menu_actions = {'1': lambda: print('Action 1') or EXIT, '2': lambda: print('Action 2') or EXIT}
        menu = Menu('', menu_actions)
        self.assertEqual(menu.text, '')
        self.assertEqual(menu.menu_actions, menu_actions)
        self.assertEqual(menu.invalid_message, 'Invalid input\n')
        self.assertFalse(menu.case_sensitive)
        menu.run_once()
        self.assertEqual(mock_stdout.getvalue(), '\nAction 1\n')

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_user_invalid_input_loops(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_input.side_effect = ['0', '1']
        menu_actions = {'1': lambda: print('Action 1') or EXIT,
                        '2': lambda: print('Action 2') or EXIT}
        menu = Menu('', menu_actions)
        menu.run_once()
        self.assertEqual(mock_stdout.getvalue(), '\nInvalid input\n\nAction 1\n')

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_user_loops_until_leave_key(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_input.side_effect = ['1', '1', '2']
        menu_actions = {'1': lambda: print('Action 1') or LOOP,
                        '2': lambda: print('Action 2') or EXIT}
        menu = Menu('', menu_actions)
        menu.loop()
        self.assertEqual(mock_stdout.getvalue(), '\nAction 1\n\nAction 1\n\nAction 2\n')
