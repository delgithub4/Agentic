class AgentValidator:

    @staticmethod
    def validate(name):

        if not name:

            raise ValueError(
                "Agent name is required."
            )

        return True
