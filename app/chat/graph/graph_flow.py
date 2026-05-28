from app.chat.graphstate.agent_state import AgentState
from app.chat.guardrails import guardrail_router, handle_block
from app.chat.nodes.call_llm import call_model
from app.chat.nodes.update_counter import update_counters
from langgraph.graph import END, START, StateGraph
from app.chat.tools import tool_node

workflow = StateGraph(AgentState)

workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)
workflow.add_node("handle_block", handle_block)
workflow.add_node("counter", update_counters)

workflow.add_edge(START, "agent")

# Guardrail routing happens immediately after the agent chooses an action
workflow.add_conditional_edges(
    "agent",
    guardrail_router,
    {
        "tools": "tools",
        "handle_block": "handle_block",
        END: END
    }
)

# After tools or block handlers run, track metrics and return to the agent
workflow.add_edge("tools", "counter")
workflow.add_edge("counter", "agent")
workflow.add_edge("handle_block", "agent")

app = workflow.compile()