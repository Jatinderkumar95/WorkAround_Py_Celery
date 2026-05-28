from langchain_core.tools import tool

@tool
def send_sms(recipient: str, message: str) -> str:
    """Send an SMS notification to a user. This costs 1 credit."""
    # Simulating an expensive write operation
    return f"SMS successfully sent to {recipient}."