import unittest
from my_app import app


class AppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index_view_should_return_hello_world(self):
        response = self.app.get("/")
        self.assertIn(b"hello world", response.data)

    def test_alive_view_should_return_alive_string(self):
        response = self.app.get("/alive")
        self.assertIn(b"alive!", response.data)
