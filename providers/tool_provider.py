class ToolProvider:

    def available(self):

        return []

    async def invoke(
        self,
        tool,
        payload,
    ):

        return {
            "tool": tool,
            "payload": payload,
        }
