from providers.provider_factory import ProviderFactory


class ToolManager:

    def __init__(self):

        self.provider = ProviderFactory.tools()

    async def execute(
        self,
        tool,
        payload,
    ):

        return await self.provider.invoke(
            tool,
            payload,
        )
