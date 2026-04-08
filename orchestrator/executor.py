from brain.planner import plan_task
from actions.executor import run_action


class ExecutionManager:
    def execute_plan(self, task: str) -> str:
        plan = plan_task(task)

        print("🧠 Plan Generated:")
        print(plan)

        steps = [line.strip() for line in plan.split("\n") if line.strip()]
        results = []

        for step in steps:
            print(f"⚡ Executing step: {step}")
            result = run_action(step)
            results.append(result)

        return "\n".join(results) if results else "No executable steps generated."


_manager = ExecutionManager()


def execute_plan(task: str):
    return _manager.execute_plan(task)