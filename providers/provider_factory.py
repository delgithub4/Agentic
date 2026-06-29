from providers.agent_provider import AgentProvider
from providers.tool_provider import ToolProvider
from providers.workflow_provider import WorkflowProvider
from providers.planner_provider import PlannerProvider


class ProviderFactory:

    _instances = {}

    @classmethod
    def agent(cls):

        if "agent" not in cls._instances:
            cls._instances["agent"] = AgentProvider()

        return cls._instances["agent"]

    @classmethod
    def tools(cls):

        if "tools" not in cls._instances:
            cls._instances["tools"] = ToolProvider()

        return cls._instances["tools"]

    @classmethod
    def planner(cls):

        if "planner" not in cls._instances:
            cls._instances["planner"] = PlannerProvider()

        return cls._instances["planner"]

    @classmethod
    def workflow(cls):

        if "workflow" not in cls._instances:
            cls._instances["workflow"] = WorkflowProvider()

        return cls._instances["workflow"]
