import json
import os

MEMORY_FILE = "memory/problem_memory.json"

def save_interaction(problem, solution, feedback=None):

    record = {
        "problem": problem,
        "solution": solution,
        "feedback": feedback
    }

    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            json.dump([], f)

    with open(MEMORY_FILE, "r") as f:
        data = json.load(f)

    data.append(record)

    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_memory():

    if not os.path.exists(MEMORY_FILE):
        return []

    with open(MEMORY_FILE, "r") as f:
        return json.load(f)