from agents.solver_agent import solve_math_problem
from agents.explainer_agent import explain_solution

question = "What is the derivative of x^2 + 3x?"

solution = solve_math_problem(question)

print("RAW SOLUTION:\n")
print(solution)

explanation = explain_solution(question, solution)

print("\nTUTOR EXPLANATION:\n")
print(explanation)