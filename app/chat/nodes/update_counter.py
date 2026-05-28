from app.chat.graphstate.agent_state import AgentState


def update_counters(state: AgentState):
    """
    Middleware tracking: Runs immediately after tools execute successfully 
    to accurately log usage.
    """
    last_message = state["messages"][-1]
    
    # Check what tool was just run in the history
    new_sms_deduction = 0
    new_tool_calls = 0
    
    if isinstance(last_message, ToolMessage):
        new_tool_calls = 1
        # If it was an SMS tool, deduct a credit
        if state["messages"][-2].tool_calls[0]["name"] == "send_sms":
            new_sms_deduction = 1

    return {
        "total_tool_calls": state.get("total_tool_calls", 0) + new_tool_calls,
        "sms_credits": state.get("sms_credits", 0) - new_sms_deduction
    }