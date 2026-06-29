class ToolTask:

    async def run(
        self,
        tool,
    ):

        return {
            "tool": tool,
            "status": "completed",
        }
