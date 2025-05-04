import yaml
from app.llm.llm_services import llm
from app.llm.agents.state import AgentState
from langchain.schema import SystemMessage, HumanMessage, AIMessage

class ArbiterAgent:
    def __init__(self):
        self.model = llm
        self.prompt = self.get_prompt("ARBITER_PROMPT")

    def get_prompt(self, name):
        with open("app/prompts/prompt.yml", "r", encoding="utf-8") as file:
            config = yaml.safe_load(file)
            return config[name]["prompt"]

    def arbiter_opinion(self, state: AgentState, debate_history) -> AgentState:
        moral_question= state["input_dilemma"]
        messages= [SystemMessage(content= self.prompt.format(debate_history= debate_history)), HumanMessage(content= moral_question)]
        messages.extend(state["messages"])
        response = self.model.invoke(messages)
        return {"final_conclusion": response.content}

arbiter_agent = ArbiterAgent()