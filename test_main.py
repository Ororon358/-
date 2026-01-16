import unittest
from unittest.mock import patch
from app.main import app
from fastapi.testclient import TestClient

class TestURLShortener(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    @patch('app.storage.URLStorage')
    def test_shorten_url(self, mock_storage):
        mock_storage.instance.create_short_url.return_value = "abc123"
        response = self.client.post("/shorten", json={"url": "https://test.com"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("short_url", response.json())

if __name__ == '__main__':
    unittest.main()