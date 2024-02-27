import unittest

from search_question_tool import BrowseStackOverflowTool
from stackoverflow_toolkit import StackOverflowToolkit


class StackOverflowToolkitTests(unittest.TestCase):
    def setUp(self):
        self.toolkit = StackOverflowToolkit()

    def test_get_tools_returns_list_of_tools(self):
        tools = self.toolkit.get_tools()
        self.assertIsInstance(tools, list)
        self.assertTrue(all(isinstance(tool, BrowseStackOverflowTool) for tool in tools))

    def test_get_env_keys_returns_list_of_strings(self):
        env_keys = self.toolkit.get_env_keys()
        self.assertIsInstance(env_keys, list)
        self.assertTrue(all(isinstance(key, str) for key in env_keys))

    def test_toolkit_has_name_and_description(self):
        self.assertEqual(self.toolkit.name, "StackOverflow Toolkit")
        self.assertEqual(self.toolkit.description, "StackOverflow Tool kit contains all tools related to StackOverflow")
