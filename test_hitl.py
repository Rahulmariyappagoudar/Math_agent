from agents.parser_agent import parse_problem
from agents.solver_agent import solve_math_problem
from agents.verifier_agent import verify_solution
from agents.hitl_agent import check_hitl

question = "Find derivative of x^2 + 3x"

parsed = parse_problem(question)

solution = solve_math_problem(question)

verification = verify_solution(question, solution)

decision = check_hitl(parsed, verification)

print("Parsed:", parsed)
print("\nVerification:", verification)
print("\nHITL Decision:", decision)