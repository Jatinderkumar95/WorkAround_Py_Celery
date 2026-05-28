from app.chat.graphstate.agent_state import AgentState


def handle_block(state: AgentState):
    """
    Interceptors node: Injects a physical barrier system message back 
    to the agent explaining *why* its action was blocked.
    """
    last_message = state["messages"][-1]
    tool_messages = []
    
    # Inject a failure message for each tool invocation the model attempted
    for tool_call in last_message.tool_calls:
        tool_messages.append(
            ToolMessage(
                content="Error: Tool execution blocked by system guardrails (Quota exceeded). Provide an alternative resolution or inform the user.",
                tool_call_id=tool_call["id"]
            )
        )
        
    return {"messages": tool_messages}