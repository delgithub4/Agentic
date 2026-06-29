class TaskRepository:

    def __init__(self):

        self.tasks = []

    def save(self, task):

        self.tasks.append(task)

    def pending(self):

        return self.tasks
