import unittest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestApp(unittest.TestCase):
    def test_root(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())

    def test_health(self):
        response = client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_motivate(self):
        response = client.get("/motivate")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())
