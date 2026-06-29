class TaskHelper:

    @staticmethod
    def completed(tasks):

        return [
            task
            for task in tasks
            if task.get("status") == "completed"
        ]
