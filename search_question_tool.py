from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type


class BrowseStackOverflowSchema(BaseModel):
    query: str = Field(..., description="Query to search StackOverflow with (your coding problem)"),
    k: int = Field(..., description="Maximum number of answers allowed in response")

class BrowseStackOverflowTool(BaseTool):
    """
    Browse StackOverflow Tool
    """
    name: str = "Browse StackOverflow Tool"
    args_schema: Type[BaseModel] = BrowseStackOverflowSchema
    description: str = "Browses StackOverflow for an answer to your coding question"

    def _execute(self, query: str = None, k: int = 5):
        answer_list = []
        response = f"""
            Query: {query}
            Top {k} answers: {answer_list}
        """
        return response
