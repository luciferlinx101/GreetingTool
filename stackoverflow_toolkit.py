from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from search_question_tool import BrowseStackOverflowTool


class StackOverflowToolkit(BaseToolkit, ABC):
    name: str = "StackOverflow Toolkit"
    description: str = "StackOverflow Tool kit contains all tools related to StackOverflow"

    def get_tools(self) -> List[BaseTool]:
        return [BrowseStackOverflowTool()]

    def get_env_keys(self) -> List[str]:
        return ["FROM"]