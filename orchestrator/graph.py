from codecs import raw_unicode_escape_decode
from langgraph.graph import StateGraph,END,START
from typing import TypedDict
from brain.router import route
from brain.llm import ask_local_llm

class AgentState(TypedDict):
    input: str
    output: str

def process_node(state:AgentState):
    prompt = state["input"]
    
    decision = route(prompt)

    if decision == "local":
        response = {"output":ask_local_llm(prompt)}
    else:
        response = "Cloud not implemented yet"

    return response

def build_graph():
    builder=StateGraph(AgentState)
    
    builder.add_node("process",process_node)
    
    builder.set_entry_point("process")
    builder.set_finish_point("process")
    return builder.compile()