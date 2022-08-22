import unittest
import app
from unittest.mock import patch

class TestFunction(unittest.TestCase):
    def setUp(self) -> None:
        ...

    def test_check_document_existance(self):
        result = app.check_document_existance("11-2")
        self.assertEqual(result, True)

    @patch('builtins.input', return_value='11-2')
    def test_get_doc_owner_name(self, mock_input):
        result = app.get_doc_owner_name()
        self.assertEqual(result, "Геннадий Покемонов")

    def test_add_new_shelf(self):
        result = list(app.add_new_shelf(4))
        self.assertEqual(result, [4, True])

    @patch('builtins.input', return_value='11-2')
    def test_delete_doc(self, mock_input):
        result = list(app.delete_doc())
        self.assertEqual(result, ['11-2', True])

    @patch('builtins.input', return_value='11-2')
    def test_get_doc_shelf(self, mock_input):
        result = app.get_doc_shelf()
        self.assertEqual(result, "1")

    @patch('builtins.input', side_effect=[500, 'invoice', 'Batman', '4'])
    def test_add_new_doc(self, mock_input):
        result = app.add_new_doc()
        self.assertEqual(result, "4")