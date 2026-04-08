from langchain_community.llms import Ollama
from config import LOCALE_MODEL

llm = Ollama(model=LOCALE_MODEL)

def ask_local_llm(prompt:str):
    response = llm.invoke(prompt)
    return response
