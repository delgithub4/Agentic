class AgentProvider:

    async def execute(
        self,
        objective,
        context=None,
    ):

        return {
            "objective": objective,
            "status": "completed",
            "context": context,
        }
