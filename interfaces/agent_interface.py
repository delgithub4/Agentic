from abc import ABC, abstractmethod


class AgentInterface(ABC):

    @abstractmethod
    async def execute(
        self,
        objective,
        context=None,
    ):
        ...
