from tools import ToolBox
from planner import Planner
from memory import Memory

from agents.researcher import ResearchAgent
from agents.writer import WriterAgent
from agents.reviewer import ReviewerAgent


class Agent:

    def __init__(self):

        self.tools = ToolBox()
        self.planner = Planner()
        self.memory = Memory()

        self.researcher = ResearchAgent()
        self.writer = WriterAgent()
        self.reviewer = ReviewerAgent()

    def run(self, task):

        task_lower = task.lower()

    if task_lower.startswith("calculate"):

        expression = task.replace("calculate", "").strip()

        return self.tools.calculator(expression)

    if "time" in task_lower:

        return self.tools.current_time()

    if "date" in task_lower:

        return self.tools.current_date()
        
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
