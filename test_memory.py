from agents.solver_agent import solve_math_problem
from memory.memory_store import save_interaction, get_memory

question = "What is derivative of x^2 + 3x?"

solution = solve_math_problem(question)

save_interaction(question, solution)

memory = get_memory()

print(memory)