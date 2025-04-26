import unittest
import json
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_world(self):
        """Test the root endpoint"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello World!')

    def test_test1_success(self):
        """Test the /test1 endpoint"""
        response = self.app.get('/test1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['message'], 'success')

    def test_test2_error(self):
        """Test the /test2 endpoint"""
        response = self.app.get('/test2')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['message'], 'error')

    def test_test3_timeout(self):
        """Test the /test3 endpoint"""
        response = self.app.get('/test3')
        self.assertEqual(response.status_code, 500)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['message'], 'timeout')


if __name__ == '__main__':
    unittest.main() 