class TaskValidator:

    @staticmethod
    def validate(task):

        if not task:

            raise ValueError(
                "Task cannot be empty."
            )

        return True
