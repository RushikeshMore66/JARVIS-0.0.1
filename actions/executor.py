from interpreter import interpreter

interpreter.auto_run = True
interpreter.system_message = """
You are JARVIS, an AI system controller.
Execute safe and efficient system commands.
Avoid destructive operations.
Be precise.
"""

def run_action(prompt:str):
    print(f"⚡ Executing: {prompt}")
    try:
        interpreter.chat(prompt)
        return "✅ Task executed successfully."
    except Exception as e:
        return f"Error: {str(e)}"