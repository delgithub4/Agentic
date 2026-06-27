from planner import Planner
from memory import Memory

from agents.researcher import ResearchAgent
from agents.writer import WriterAgent
from agents.reviewer import ReviewerAgent


class Agent:

    def __init__(self):

        self.planner = Planner()
        self.memory = Memory()

        self.researcher = ResearchAgent()
        self.writer = WriterAgent()
        self.reviewer = ReviewerAgent()

    def run(self, task):

        self.memory.save(task)

        plan = self.planner.create_plan(task)

        research = self.researcher.research(task)

        draft = self.writer.write(research)

        final = self.reviewer.review(draft)

        return {
            "task": task,
            "plan": plan,
            "response": final
        }
