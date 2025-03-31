import unittest
from unittest.mock import patch, mock_open
import pandas as pd

from app.io.input import file_read, pandas_read

class TestInputFunctions(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='file contents')
    def test_file_read(self, mock_file):
        self.assertEqual(file_read('test.txt'), 'file contents')

    @patch('builtins.open', new_callable=mock_open, read_data='')
    def test_file_read_empty_file(self, mock_file):
        self.assertEqual(file_read('test2.txt'), '')

    def test_file_read_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            file_read('&2728hshus8qqjsij826982_nonexistent.txt')

    @patch('pandas.read_csv')
    def test_pandas_read(self, mock_read_csv):
        mock_df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
        mock_read_csv.return_value = mock_df
        self.assertTrue(pandas_read('data.csv').equals(mock_df))

    @patch('pandas.read_csv')
    def test_pandas_read_empty_file(self, mock_read_csv):
        mock_df = pd.DataFrame()
        mock_read_csv.return_value = mock_df
        self.assertTrue(pandas_read('empty.csv').equals(mock_df))

    def test_pandas_read_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            pandas_read('&2728hshus8qqjsij826982_nonexistent.csv')


if __name__ == '__main__':
    unittest.main()