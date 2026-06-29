from providers.provider_factory import ProviderFactory


class PlanningManager:

    def __init__(self):

        self.provider = ProviderFactory.planner()

    async def create_plan(
        self,
        objective,
    ):

        return await self.provider.plan(
            objective,
        )
