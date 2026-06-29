class ToolHelper:

    @staticmethod
    def names(tools):

        return [
            tool.get("name")
            for tool in tools
        ]
