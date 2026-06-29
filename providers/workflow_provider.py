class WorkflowProvider:

    async def execute(self, workflow):

        return {
            "workflow": workflow,
            "status": "completed",
        }
