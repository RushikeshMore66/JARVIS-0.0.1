from brain.llm import ask_llm

def plan_task(prompt: str):
    planning_prompt = f"""
You are a planning AI.

Break this task into clear steps:

Task: {prompt}

Return steps in numbered format.
"""

    plan = ask_llm(planning_prompt)

    return plan