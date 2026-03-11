from typing import TypedDict, Annotated, List
from langchain_core.messages import BaseMessage


class AgentState(TypedDict):
    
    # conversation history
    messages: Annotated[List[BaseMessage], "conversation history"]

    # current task plan
    plan: Annotated[List[str], "current task plan"]

    # tool outputs
    tool_results: Annotated[List[dict], "tool call outputs"]

    # reasoning loop count
    iteration: Annotated[int, "reasoning loop count"]

    # status
    status: Annotated[str, "running | done | error"]
