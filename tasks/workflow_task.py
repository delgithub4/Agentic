class WorkflowTask:

    async def run(
        self,
        workflow,
    ):

        return {
            "workflow": workflow,
            "status": "completed",
        }
