from abc import ABC, abstractmethod


class ToolInterface(ABC):

    @abstractmethod
    async def invoke(
        self,
        tool,
        payload,
    ):
        ...
