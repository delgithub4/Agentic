from planner import Planner
from memory import Memory


class Agent:

    def __init__(self):

        self.planner = Planner()
        self.memory = Memory()

    def run(self, task):

        plan = self.planner.create_plan(task)

        self.memory.save(task)

        return {
            "task": task,
            "plan": plan
        }
