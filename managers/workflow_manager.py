from providers.provider_factory import ProviderFactory


class WorkflowManager:

    def __init__(self):

        self.provider = ProviderFactory.workflow()

    async def execute(
        self,
        workflow,
    ):

        return await self.provider.execute(
            workflow,
        )
