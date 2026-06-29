class AgentTask:

    async def run(
        self,
        objective,
    ):

        return {
            "objective": objective,
            "status": "completed",
        }
