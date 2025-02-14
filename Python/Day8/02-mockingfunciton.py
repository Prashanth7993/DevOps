# import requests

# from typing import Dict
# from unittest.mock import patch
# import unittest

# def get_data(url: str) -> Dict[str, str]:
#     response = requests.get(url)
#     return response.json


# class Testgetdata(unittest.TestCase):

#     @patch('request.get')
#     def test_Get_Data(self,mock_get: patch) -> None:
#         mock_response = mock_get.return_value
#         mock_response.json.return_valye = {'key','value'}

#         result = get_data('http://example.com/api')
#         self.assertEqual(reuslt,{'key','value'})
#         mock_get.assert_called_once_with('http://example.com/api')


# if __name__ == '__main__':
#     unittest.main()


import requests
from typing import Dict
from unittest.mock import patch
import unittest

def get_data(url: str) -> Dict[str, str]:
    response = requests.get(url)
    return response.json()  # Fixed missing parentheses

class TestGetData(unittest.TestCase):

    @patch('requests.get')  # Fixed incorrect patch path
    def test_Get_Data(self, mock_get: patch) -> None:
        # Mock API response
        mock_response = mock_get.return_value
        mock_response.json.return_value = {'key': 'value'}  # Fixed format

        result = get_data('http://example.com/api')

        # Corrected variable name
        self.assertEqual(result, {'key': 'value'})
        mock_get.assert_called_once_with('http://example.com/api')

if __name__ == '__main__':
    unittest.main()
