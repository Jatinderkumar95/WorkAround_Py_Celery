from typing import Literal

from app.chat.graphstate.agent_state import AgentState


def guardrail_router(state: AgentState) -> Literal["tools", "handle_block", END]:
    """
    The Guardrail Boundary: Evaluates the agent's intent *before* allowing execution to progress to the ToolNode.
    """
    last_message = state["messages"][-1]
    
    # If the model didn't ask to call any tools, pass through to the end
    if not isinstance(last_message, AIMessage) or not last_message.tool_calls:
        return END

    # --- HARD LIMIT GUARDRAIL 1: Max Global Tool Calls ---
    if state.get("total_tool_calls", 0) >= 3:
        print("\n🛑 GUARDRAIL TRIGGERED: Global tool execution limit (3) reached!")
        return "handle_block"

    # --- CONTINGENT GUARDRAIL 2: Contextual Resource Limit ---
    for tool_call in last_message.tool_calls:
        if tool_call["name"] == "send_sms":
            if state.get("sms_credits", 0) <= 0:
                print("\n🛑 GUARDRAIL TRIGGERED: Out of SMS credits!")
                return "handle_block"

    # If all constraints pass, safely route to the tools
    return "tools"