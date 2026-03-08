def route_problem(parsed):

    topic = parsed["topic"]

    if topic == "calculus":
        return "calculus_solver"

    if topic == "linear_algebra":
        return "matrix_solver"

    return "general_solver"