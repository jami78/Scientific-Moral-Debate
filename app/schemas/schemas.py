from pydantic import BaseModel
from typing import List

class DebateInput(BaseModel):
    input: str

class MessageOutput(BaseModel):
    name: str
    step: str
    content: str


class DebateResponse(BaseModel):
    messages: List[MessageOutput]
    final_conclusion: str