from agents.parser_agent import parse_problem

question = "Find derivative of x^2 + 3x"

parsed = parse_problem(question)

print(parsed)