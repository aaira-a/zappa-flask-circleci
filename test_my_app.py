import unittest
from my_app import app
from my_app import scheduled


class AppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index_view_should_return_hello_world(self):
        response = self.app.get("/")
        self.assertIn(b"hello world", response.data)

    def test_status_view_should_return_post_data(self):
        response = self.app.post("/status",
                                 data={"name": "bob", "status": "alive"})
        self.assertIn(b"hi bob, it's alive!", response.data)

    def test_scheduled_view_should_return_scheduled_string(self):
        response = self.app.get("/scheduled")
        self.assertIn(b"schedule triggered on", response.data)

    def test_scheduled_direct_call_should_return_scheduled_string(self):
        self.assertIn("schedule triggered on", scheduled())
