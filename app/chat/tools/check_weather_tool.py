from langchain_core.tools import tool

@tool
def check_weather(location: str) -> str:
    """Fetch current weather for a specific location."""
    # Simulating a free/cheap read operation
    return f"The weather in {location} is sunny and 22°C."