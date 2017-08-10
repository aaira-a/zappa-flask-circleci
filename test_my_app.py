import unittest
from unittest.mock import patch

import os

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

    @patch.dict(os.environ, {"ENV_VAR_1": "mocked_value"})
    def test_envvar_view_should_print_envvar_value(self):
        response = self.app.get("/envvar")
        self.assertIn(b"mocked_value", response.data)

    def test_scheduled_direct_call_should_return_scheduled_string(self):
        self.assertIn("schedule triggered on", scheduled())
