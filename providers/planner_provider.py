class PlannerProvider:

    async def plan(self, objective):

        return [
            {
                "step": 1,
                "task": objective,
            }
        ]
