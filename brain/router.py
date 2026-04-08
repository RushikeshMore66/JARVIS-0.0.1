def route(prompt:str):

    if "internet" in prompt or "search" in prompt:
        return "cloud"
    
    return "local"
    