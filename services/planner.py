class Planner:

    def create_plan(self, task):

        return {
            "goal": task,
            "steps": [
                "Understand the request",
                "Select the appropriate agent/tool",
                "Execute the task",
                "Review the result",
                "Return the response"
            ]
        }

