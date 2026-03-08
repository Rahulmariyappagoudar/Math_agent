def parse_problem(question):

    topic = "general"

    if "derivative" in question.lower() or "d/dx" in question.lower():
        topic = "calculus"

    if "matrix" in question.lower():
        topic = "linear_algebra"

    if "integral" in question.lower():
        topic = "calculus"

    return {
        "problem_text": question,
        "topic": topic,
        "variables": [],
        "constraints": [],
        "needs_clarification": False
    }