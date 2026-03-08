from agents.parser_agent import parse_problem
from agents.router_agent import route_problem

question = "Find derivative of x^2 + 3x"

parsed = parse_problem(question)

route = route_problem(parsed)

print("Parsed Problem:")
print(parsed)

print("\nRoute Selected:")
print(route)