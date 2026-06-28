class Router:

    def decide(self, task):

        task = task.lower()

        if "calculate" in task:
            return "calculator"

        if "time" in task:
            return "time"

        if "date" in task:
            return "date"

        if "write" in task:
            return "writer"

        if "research" in task:
            return "research"

        return "general"

