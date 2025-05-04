from typing import List, Annotated
from typing_extensions import TypedDict
from operator import add 

class AgentState(TypedDict):
    input_dilemma: str
    agent_names: List[str]
    messages: Annotated[list, add]
    final_conclusion: str