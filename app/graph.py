from langgraph.graph import StateGraph, END
from app.llm.agents.state import AgentState
from app.llm.agents.neuroscientist import neuroscience_agent
from app.llm.agents.sociologist import sociology_agent
from app.llm.agents.psychologist import psychology_agent
from app.llm.agents.evo_bio import evobio_agent
from app.llm.agents.arbiter import arbiter_agent
from app.utils.get_prompt import argument_prompt, rebuttal_prompt
from langgraph.checkpoint.memory import InMemorySaver

def start(state: AgentState) -> AgentState:
    print(f"The debate has started based on this moral question: {state['input_dilemma']}")
    return {}


def neuroscience_arg(state: AgentState) -> AgentState:
    response= neuroscience_agent.neuroscience_opinion(node= "argument", state= state, node_prompt= argument_prompt)
    print("\n🧠 Neuroscience [ARGUMENT]:")
    print(response["messages"][0].content)
    return response

def sociology_arg(state: AgentState) -> AgentState:
    response= sociology_agent.sociologist_opinion(node= "argument", state=state, node_prompt= argument_prompt)
    print("\n🏛️ Sociology [ARGUMENT]:")
    print(response["messages"][0].content)
    return response

def psychology_arg(state: AgentState) -> AgentState:
    response= psychology_agent.psychologist_opinion(node= "argument",state=state, node_prompt= argument_prompt)
    print("\n🗣️ Psychology [ARGUMENT]:")
    print(response["messages"][0].content)
    return response

def evobio_arg(state: AgentState) -> AgentState:
    response= evobio_agent.evobio_opinion(node= "argument", state=state, node_prompt= argument_prompt)
    print("\n🐒 Evobio [ARGUMENT]:")
    print(response["messages"][0].content)
    return response

def neuroscience_rebut(state: AgentState) -> AgentState:
    argument_messages = [
        msg for msg in state["messages"]
        if msg.additional_kwargs.get("step") == "argument" and msg.name != "Neuroscience"
    ]
    combined_arguments = "\n\n".join(
        f"{msg.name}: {msg.content}" for msg in argument_messages
    )
    rebuttal= rebuttal_prompt.format(combined_arguments= combined_arguments)
    response= neuroscience_agent.neuroscience_opinion(node_prompt= rebuttal, state=state, node="rebuttal")
    print("\n🧠 Neuroscience [REBUTTAL]:")
    print(response["messages"][0].content)

    return response

def psychology_rebut(state: AgentState) -> AgentState:
    argument_messages = [
        msg for msg in state["messages"]
        if msg.additional_kwargs.get("step") == "argument" and msg.name != "Psychology"
    ]
    combined_arguments = "\n\n".join(
        f"{msg.name}: {msg.content}" for msg in argument_messages
    )
    rebuttal= rebuttal_prompt.format(combined_arguments= combined_arguments)
    response= psychology_agent.psychologist_opinion(node_prompt= rebuttal,state=state, node="rebuttal")
    print("\n🗣️ Psychology [REBUTTAL]:")
    print(response["messages"][0].content)
    return response

def sociology_rebut(state: AgentState) -> AgentState:
    argument_messages = [
        msg for msg in state["messages"]
        if msg.additional_kwargs.get("step") == "argument" and msg.name != "Sociology"
    ]
    combined_arguments = "\n\n".join(
        f"{msg.name}: {msg.content}" for msg in argument_messages
    )
    rebuttal= rebuttal_prompt.format(combined_arguments= combined_arguments)
    response= sociology_agent.sociologist_opinion(node_prompt= rebuttal, state=state, node="rebuttal")
    print("\n🏛️ Sociology [REBUTTAL]:")
    print(response["messages"][0].content)
    return response

def evobio_rebut(state: AgentState) -> AgentState:
    argument_messages = [
        msg for msg in state["messages"]
        if msg.additional_kwargs.get("step") == "argument" and msg.name != "EvoBio"
    ]
    combined_arguments = "\n\n".join(
        f"{msg.name}: {msg.content}" for msg in argument_messages
    )
    rebuttal= rebuttal_prompt.format(combined_arguments= combined_arguments)
    response= evobio_agent.evobio_opinion(node_prompt= rebuttal, state=state,  node="rebuttal")
    print("\n🐒 Evobio [REBUTTAL]:")
    print(response["messages"][0].content)
    return response



def arbiter_node(state: AgentState) -> dict:
    debate_messages = [
        msg for msg in state["messages"]
        if msg.additional_kwargs.get("step") in ["argument", "rebuttal"]
    ]
    debate_history = "\n\n".join([
        f"[{msg.additional_kwargs['step']}] {msg.name}: {msg.content}"
        for msg in debate_messages
    ])

    response=arbiter_agent.arbiter_opinion(state=state, debate_history=debate_history)
    print("\n⚖️  Arbiter's Final Conclusion:")
    print(response["final_conclusion"])
    return response



workflow = StateGraph(AgentState)
workflow.add_node("start", start)
workflow.add_node("neuro_arg", neuroscience_arg)
workflow.add_node("socio_arg", sociology_arg)
workflow.add_node("psych_arg", psychology_arg)
workflow.add_node("evobio_arg", evobio_arg)

workflow.add_node("neuro_rebut", neuroscience_rebut)
workflow.add_node("socio_rebut", sociology_rebut)
workflow.add_node("psych_rebut", psychology_rebut)
workflow.add_node("evobio_rebut", evobio_rebut)
workflow.add_node("arbiter", arbiter_node)
workflow.set_entry_point("start")
workflow.add_edge("start", "neuro_arg")
workflow.add_edge("start", "socio_arg")
workflow.add_edge("start", "psych_arg")
workflow.add_edge("start", "evobio_arg")

all_arg_nodes = ["neuro_arg", "socio_arg", "psych_arg", "evobio_arg"]
all_rebut_nodes = ["neuro_rebut", "socio_rebut", "psych_rebut", "evobio_rebut"]

for arg_node in all_arg_nodes:
    for rebut_node in all_rebut_nodes:
        workflow.add_edge(arg_node, rebut_node)

workflow.add_edge("neuro_rebut", "arbiter")
workflow.add_edge("socio_rebut", "arbiter")
workflow.add_edge("psych_rebut", "arbiter")
workflow.add_edge("evobio_rebut", "arbiter")
workflow.add_edge("arbiter", END)

checkpointer = InMemorySaver()

graph = workflow.compile(checkpointer=checkpointer)

print("LangGraph architecture compiled successfully!")

