from fastapi import APIRouter, Depends
from app.graph import graph
from app.llm.agents.state import AgentState
from app.schemas.schemas import DebateInput, MessageOutput, DebateResponse
import uuid

router = APIRouter()

@router.post("/run_debate", response_model=DebateResponse)
async def run_debate(request: DebateInput):
    config = {"configurable": {"thread_id": str(uuid.uuid4())}}
    initial_state = AgentState(
        messages=[],
        input_dilemma=request.input
    )


    result= graph.invoke(initial_state, config)

    message_outputs = []
    for msg in result.get("messages", []):
        message_outputs.append(MessageOutput(
            name=msg.name,
            step=msg.additional_kwargs.get("step", "unknown"),
            content=msg.content
        ))

    return DebateResponse(
        messages=message_outputs,
        final_conclusion=result.get("final_conclusion", "No conclusion reached")
    )