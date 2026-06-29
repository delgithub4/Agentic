from enum import Enum


class AgentStatus(str, Enum):

    IDLE = "idle"

    RUNNING = "running"

    COMPLETED = "completed"

    FAILED = "failed"
