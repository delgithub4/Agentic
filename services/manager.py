from agents.researcher import ResearchAgent
from agents.writer import WriterAgent
from agents.reviewer import ReviewerAgent


class AgentManager:

    def __init__(self):

        self.agents = {
            "research": ResearchAgent(),
            "writer": WriterAgent(),
            "reviewer": ReviewerAgent()
        }

    def get(self, name):

        return self.agents.get(name)

