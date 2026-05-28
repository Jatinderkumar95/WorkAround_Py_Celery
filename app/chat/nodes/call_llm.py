from app.chat.graphstate.agent_state import AgentState
from app.chat.llms.chatopenai import build_llm


def call_model(state: AgentState):
    """The agent node that reads history and generates actions."""
    response = build_llm({},"").invoke(state["messages"])
    return {"messages": [response]}