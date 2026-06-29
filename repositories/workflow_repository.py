class WorkflowRepository:

    def __init__(self):

        self.workflows = []

    def save(self, workflow):

        self.workflows.append(workflow)

    def all(self):

        return self.workflows
