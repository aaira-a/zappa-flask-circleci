import unittest

import json
import os
import shutil

from envvar_helper import add_aws_envvar


class EnvVarHelperTests(unittest.TestCase):

    def setUp(self):
        shutil.copy2("test.init.json", "undertest.json")

    def tearDown(self):
        os.remove("undertest.json")

    def test_add_envvars(self):
        add_aws_envvar("stage1", "key4", "value4", "undertest.json")
        add_aws_envvar("stage1", "key5", "value5", "undertest.json")

        with open("undertest.json", "r") as f1:
            actual = json.load(f1)

        with open("test.expected.json", "r") as f2:
            expected = json.load(f2)

        self.assertDictEqual(expected, actual)
