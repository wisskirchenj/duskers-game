import unittest
from io import StringIO
from unittest.mock import patch, MagicMock

from duskers.menu import Menu


class TestMenu(unittest.TestCase):

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_initialized_with_valid_parameters(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_input.side_effect = ['1']
        menu_actions = {'1': lambda: print('Action 1'), '2': lambda: print('Action 2')}
        menu = Menu('Choose an action:', menu_actions, leave_menu_key='q')
        self.assertEqual(menu.text, 'Choose an action:')
        self.assertEqual(menu.menu_actions, menu_actions)
        self.assertEqual(menu.invalid_message, 'Invalid input\n')
        self.assertEqual(menu.case_sensitive, False)
        self.assertEqual(menu.leave_menu_key, 'q')
        menu.run_once()
        self.assertEqual(mock_stdout.getvalue(), 'Choose an action:\nAction 1\n')

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_user_invalid_input_loops(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_input.side_effect = ['0', '1']
        menu_actions = {'1': lambda: print('Action 1'), '2': lambda: print('Action 2')}
        menu = Menu('Choose an action:', menu_actions, leave_menu_key='2')
        menu.run_once()
        self.assertEqual(mock_stdout.getvalue(), 'Choose an action:\nInvalid input\n\nChoose an action:\nAction 1\n')

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_user_loops_until_leave_key(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_input.side_effect = ['1', '1', '2']
        menu_actions = {'1': lambda: print('Action 1'), '2': lambda: print('Action 2')}
        menu = Menu('Choose an action:', menu_actions, leave_menu_key='2')
        menu.loop()
        self.assertEqual(mock_stdout.getvalue(), 'Choose an action:\nAction 1\nChoose an action:\nAction 1\nChoose an action:\nAction 2\n')

