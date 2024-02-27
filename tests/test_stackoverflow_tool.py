import unittest

from search_question_tool import BrowseStackOverflowTool, BrowseStackOverflowSchema


class GreetingsToolTestCase(unittest.TestCase):
    def setUp(self):
        self.tool = BrowseStackOverflowTool()

    def test_tool_name(self):
        print(self.tool.name)
        self.assertEqual(self.tool.name, "Browse StackOverflow Tool")

    def test_tool_args_schema(self):
        self.assertEqual(self.tool.args_schema, BrowseStackOverflowSchema)

    def test_tool_description(self):
        self.assertEqual(self.tool.description, "Browses StackOverflow for an answer to your coding question")

    def test_execute_method(self):
        stackoverflow_input = BrowseStackOverflowSchema(query="Module not found - pygame", k=10)
        expected_output = f"""
            Query: {stackoverflow_input.query}
            Top {stackoverflow_input.k} answers: {[]}
        """
        output = self.tool._execute(query=stackoverflow_input.query, k=stackoverflow_input.k)
        self.assertEqual(output.strip(), expected_output.strip())
