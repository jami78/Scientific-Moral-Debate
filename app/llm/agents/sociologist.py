import yaml
from app.llm.llm_services import llm
from app.llm.agents.state import AgentState
from langchain.schema import SystemMessage, HumanMessage, AIMessage

class SociologyAgent:
    def __init__(self):
        self.model = llm
        self.prompt = self.get_prompt("SOCIOLOGIST_PROMPT")

    def get_prompt(self, name):
        with open("app/prompts/prompt.yml", "r", encoding="utf-8") as file:
            config = yaml.safe_load(file)
            return config[name]["prompt"]

    def sociologist_opinion(self,node_prompt, state: AgentState, node:str) -> AgentState:
        moral_question= state["input_dilemma"]
        messages= [SystemMessage(content= self.prompt.format(node_prompt=node_prompt)), HumanMessage(content= moral_question)]
        messages.extend(state["messages"])
        response = self.model.invoke(messages)
        return {"messages": [
                        AIMessage(
                            content=response.content,
                            name="Sociology",
                            additional_kwargs={"step": node}
                        )
                    ]
                }

sociology_agent= SociologyAgent()