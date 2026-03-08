from rag.retriever import retrieve_math_rules
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="qwen2.5:7b")


def solve_math_problem(problem):

    retrieval = retrieve_math_rules(problem)

    # Normalize retrieved rules
    if isinstance(retrieval, dict):
        docs = retrieval.get("rules", [])
    else:
        docs = retrieval

    # Convert to string safely
    context = "\n\n".join(str(d) for d in docs)

    prompt = f"""
You are a math solver.

Problem:
{problem}

Relevant math rules:
{context}

Solve the problem and return the correct final answer.
"""

    response = llm.invoke(prompt)

    return response