from langgraph.graph import StateGraph
from typing import TypedDict

from brain.llm import ask_local_llm, analyze_screen, ask_cloud_llm, route_llm
from brain.router import route
from brain.planner import plan_task

from actions.executor import run_action
from actions.vision import capture_screen
from orchestrator.executor import execute_plan

from memory.store import store_memory, retrieve_memory


class AgentState(TypedDict):
    input: str
    output: str
    decision: str
    memory: str


def memory_node(state: AgentState):
    past = retrieve_memory(state["input"])
    return {"memory": str(past)}


def planner_node(state: AgentState):
    plan = plan_task(state["input"])
    return {"output": f"🧠 Plan:\n{plan}"}

def chat_node(state):
    provider = route_llm(state["input"])
    response = ask_cloud_llm(state["input"]) if provider == "cloud" else ask_local_llm(state["input"])
    return {"output": response}


def local_node(state: AgentState):
    context = state.get("memory", "")

    prompt = f"""
Context:
{context}

User:
{state['input']}
"""

    response = ask_local_llm(prompt)

    store_memory(state["input"] + " -> " + response)

    return {"output": response}


def action_node(state: AgentState):
    return {"output": run_action(state["input"])}


def vision_node(state: AgentState):
    path = capture_screen()
    return {"output": analyze_screen(path, state["input"])}


def cloud_node(state: AgentState):
    response = ask_cloud_llm(state["input"])
    return {"output": f"🌐 (Cloud) {response}"}


def interrupt_node(state: AgentState):
    return {"output": "Understood. I have stopped the current task."}


def autonomous_node(state):
    result = execute_plan(state["input"])
    return {"output": result}

def build_graph():
    builder = StateGraph(AgentState)

    builder.add_node("memory", memory_node)
    builder.add_node("router", lambda s: {"decision": route(s["input"])})
    builder.add_node("planner", planner_node)
    builder.add_node("chat", chat_node)
    builder.add_node("local", local_node)
    builder.add_node("action", action_node)
    builder.add_node("vision", vision_node)
    builder.add_node("cloud", cloud_node)
    builder.add_node("interrupt", interrupt_node)
    builder.add_node("autonomous", autonomous_node)

    builder.set_entry_point("memory")

    builder.add_edge("memory", "router")

    builder.add_conditional_edges(
        "router",
        lambda x: x["decision"],
        {
            "chat": "chat",
            "local": "local",
            "action": "action",
            "vision": "vision",
            "cloud": "cloud",
            "plan": "planner",
            "autonomous": "autonomous",
            "interrupt": "interrupt",
        }
    )

    builder.set_finish_point("chat")
    builder.set_finish_point("local")
    builder.set_finish_point("planner")
    builder.set_finish_point("action")
    builder.set_finish_point("vision")
    builder.set_finish_point("cloud")
    builder.set_finish_point("interrupt")
    builder.set_finish_point("autonomous")

    return builder.compile()