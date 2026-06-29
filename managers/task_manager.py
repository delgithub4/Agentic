class TaskManager:

    def __init__(self):

        self.tasks = []

    def add(self, task):

        self.tasks.append(task)

    def pending(self):

        return self.tasks

    def clear(self):

        self.tasks.clear()
