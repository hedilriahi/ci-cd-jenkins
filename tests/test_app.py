import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        """Set up the test client."""
        self.client = app.test_client()
        self.client.testing = True

    def test_home_endpoint(self):
        """Test the '/' endpoint."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello, DevOps World!"})

if __name__ == '__main__':
    unittest.main()
