from brain.planner import plan_task
from actions.executor import run_action


def execute_plan(task: str):
    plan = plan_task(task)

    print("🧠 Plan Generated:")
    print(plan)

    steps = plan.split("\n")

    results = []

    for step in steps:
        if step.strip():
            print(f"⚡ Executing step: {step}")

            result = run_action(step)
            results.append(result)

    return "\n".join(results)