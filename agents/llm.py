from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="qwen2.5:7b",
    temperature = 0.1
)

def ask_llm(prompt):

    response = llm.invoke(prompt)

    return response