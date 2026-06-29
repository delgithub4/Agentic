from enum import Enum


class WorkflowType(str, Enum):

    LINEAR = "linear"

    PARALLEL = "parallel"

    HIERARCHICAL = "hierarchical"
