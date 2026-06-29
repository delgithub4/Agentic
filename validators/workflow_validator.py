class WorkflowValidator:

    @staticmethod
    def validate(workflow):

        if not workflow:

            raise ValueError(
                "Workflow is required."
            )

        return True
