from agents.solver_agent import solve_math_problem
from agents.verifier_agent import verify_solution

question = "What is the derivative of x^2 + 3x?"

solution = solve_math_problem(question)

print("SOLUTION:\n")
print(solution)

verification = verify_solution(question, solution)

print("\nVERIFICATION:\n")
print(verification)