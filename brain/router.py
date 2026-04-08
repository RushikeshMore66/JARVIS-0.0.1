def route(prompt:str):
    prompt = prompt.lower()

    if  any(word in prompt for word in ["internet","search","web","google"]):
        return "cloud"

    if any(word in prompt for word in ["open","launch","start","run","close","click"]):
        return "action"
    
    return "local"
    