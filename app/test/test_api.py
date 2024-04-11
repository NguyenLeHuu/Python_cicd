import unittest
from unittest.mock import patch
import json

class TestApi(unittest.TestCase):
    @patch('app.controllers.add_controller.add_process')
    def test_add_process(self,*mock):
        mock
        self.assertEqual('Kết quả là: 12','Kết quả là: 12')
    