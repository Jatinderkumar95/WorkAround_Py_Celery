from app.chat.tools.check_weather_tool import check_weather
from app.chat.tools.send_sms_tool import send_sms
from langgraph.prebuilt import ToolNode

tools = [check_weather, send_sms]
tool_node = ToolNode(tools)