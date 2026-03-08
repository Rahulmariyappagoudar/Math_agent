from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="qwen2.5:7b",
    temperature=0
)


def generate_explanation(problem, solution):

    prompt = f"""
Explain the solution clearly for a JEE student.

Problem:
{problem}

Solution:
{solution}

Explain in 5 steps only.
"""

    response = llm.invoke(
        prompt,
        config={
            "max_tokens": 200
        }
    )

    return response