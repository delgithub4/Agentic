from fastapi import APIRouter, HTTPException

from core.responses import success

from services.agent import *
from services.manager import *
from services.planner import *
from services.memory import *
from services.router import *
from services.tools import *

router = APIRouter(
    prefix="/agentic",
    tags=["Agentic"],
)


@router.get("/")
async def info():

    return success(
        message="Agentic service is running.",
        data={
            "service": "Agentic",
            "status": "ready",
        },
    )


@router.post("/run")
async def run_agent(payload: dict):

    try:

        if "run_agent" in globals():
            result = run_agent(payload)

        elif "execute" in globals():
            result = execute(payload)

        else:
            result = payload

        return success(
            message="Workflow executed successfully.",
            data=result,
        )

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc),
        )


@router.post("/plan")
async def plan(payload: dict):

    try:

        if "create_plan" in globals():
            result = create_plan(payload)

        elif "plan_task" in globals():
            result = plan_task(payload)

        else:
            result = payload

        return success(
            message="Plan generated successfully.",
            data=result,
        )

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc),
        )


@router.get("/memory")
async def memory():

    try:

        if "get_memory" in globals():
            result = get_memory()

        else:
            result = {}

        return success(
            data=result,
        )

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc),
        )
