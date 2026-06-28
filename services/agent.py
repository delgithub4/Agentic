from manager import AgentManager
from router import Router
from tools import ToolBox
from planner import Planner
from memory import Memory

from agents.researcher import ResearchAgent
from agents.writer import WriterAgent
from agents.reviewer import ReviewerAgent


class Agent:

    def __init__(self):

        self.router = Router()
        self.tools = ToolBox()
        self.planner = Planner()
        self.memory = Memory()

        self.manager = AgentManager()

    def run(self, task):

    decision = self.router.decide(task)

    if decision == "calculator":

        expression = task.replace("calculate", "").strip()

        return self.tools.calculator(expression)

    if decision == "time":

        return self.tools.current_time()

    if decision == "date":

        return self.tools.current_date()

    self.memory.save(task)

    plan = self.planner.create_plan(task)

    researcher = self.manager.get("research")

    writer = self.manager.get("writer")
    
    reviewer = self.manager.get("reviewer")
    
    research = researcher.research(task)
    
    draft = writer.write(research)
    
    final = reviewer.review(draft)

    return {
        "task": task,
        "plan": plan,
        "response": final
    }

