from langgraph.graph import StateGraph,END,START
from typing import TypedDict
from brain.router import route
from brain.llm import ask_local_llm

class AgentState(TypedDict):
    input: str
    output: str

def router_node(state:AgentState):
    decision = route(state["input"])
    return {"decision":decision}

def local_node(state:AgentState):
    response = ask_local_llm(state["input"])
    return {"output":response}

def cloud_node(state: AgentState):
    return {"output": "🌐 Cloud feature coming soon."}

def action_node(state: AgentState):
    return {"output": "🛠️ Action execution coming next phase."}

def build_graph():
    builder=StateGraph(AgentState)
    
    builder.add_node("router",router_node)
    builder.add_node("local",local_node)
    builder.add_node("cloud",cloud_node)
    builder.add_node("action",action_node)
    
    builder.set_entry_point("router")
    builder.add_conditional_edges("router",
                                lambda x:x["decision"],
                                {
                                    "local":"local",
                                    "cloud":"cloud",
                                    "action":"action"
                                })
    builder.set_finish_point("local")
    builder.set_finish_point("cloud")
    builder.set_finish_point("action")
    
    return builder.compile()