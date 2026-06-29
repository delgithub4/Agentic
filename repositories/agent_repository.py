class AgentRepository:

    def __init__(self):

        self.agents = []

    def save(self, agent):

        self.agents.append(agent)

    def all(self):

        return self.agents
