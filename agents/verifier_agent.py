import sympy as sp
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="qwen2.5:7b")


def verify_solution(problem, solution):

    result = {
        "correct": None,
        "confidence": "Low",
        "issues": []
    }

    try:
        x = sp.symbols("x")

        if "derivative" in problem.lower():

            expr_str = problem.split("of")[-1].strip()
            expr = sp.sympify(expr_str)

            true_answer = sp.diff(expr, x)

            # if SymPy finds correct answer
            if str(true_answer) in solution:

                result["correct"] = True
                result["confidence"] = "High"

                return format_result(result)

            else:

                result["correct"] = False
                result["confidence"] = "High"
                result["issues"].append("incorrect_derivative")

                return format_result(result)

    except Exception:
        # SymPy failed → use LLM
        pass

    # --- Domain checks ---
    if "log" in problem.lower():
        result["issues"].append("domain_requires_x>0")

    if "sqrt" in problem.lower():
        result["issues"].append("domain_requires_nonnegative")

    if "division" in solution:
        result["issues"].append("possible_division_by_zero")

    # ---- LLM fallback only if SymPy couldn't verify ----
    critic_prompt = f"""
You are a math verifier.

Problem:
{problem}

Solution:
{solution}

Check:
1. correctness
2. domain restrictions
3. edge cases

Return:

Correct: Yes/No
Confidence: High/Medium/Low
Issues:
"""

    critic_response = llm.invoke(critic_prompt)

    return critic_response


def format_result(result):

    return f"""
Verification Result:
Correct: {result['correct']}
Confidence: {result['confidence']}
Issues: {result['issues']}
"""