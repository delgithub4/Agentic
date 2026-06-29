from abc import ABC, abstractmethod


class WorkflowInterface(ABC):

    @abstractmethod
    async def execute(
        self,
        workflow,
    ):
        ...
