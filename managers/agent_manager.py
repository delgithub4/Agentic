from providers.provider_factory import ProviderFactory


class AgentManager:

    def __init__(self):

        self.agent = ProviderFactory.agent()

    async def execute(
        self,
        objective,
        context=None,
    ):

        return await self.agent.execute(
            objective,
            context,
        )
