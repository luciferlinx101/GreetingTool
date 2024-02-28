from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type
from stackoverflow_api_wrapper import StackOverflowAPIWrapper

class BrowseStackOverflowSchema(BaseModel):
    query: str = Field(..., description="Query to search StackOverflow with")
    title: str = Field(..., description="String that should be contained in a title")
    tags: list = Field(..., description="Query tags, could be programming language/framework/OS")
    k: int = Field(..., description="Maximum number of answers allowed in response, default = 5")

class BrowseStackOverflowTool(BaseTool):
    """
    Browse StackOverflow Tool
    """
    name: str = "Browse StackOverflow Tool"
    args_schema: Type[BaseModel] = BrowseStackOverflowSchema
    description: str = "Browses StackOverflow for an answer to your coding question"

    def _execute(self, query: str, title: str, tags=None, k: int = 5):
        tags = [] if tags is None else tags
        client = StackOverflowAPIWrapper(k)
        return client.search_advanced(query, title, tags)
