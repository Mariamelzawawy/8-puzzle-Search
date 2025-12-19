from puzzle import get_successors,is_goal, heuristic

#Hill Climbing Algorithm
def hill_climbing(initial_state):
    current = initial_state
    path = []

    while True:
        if is_goal(current):
            return path

        neighbors = get_successors(current)
        if not neighbors:
            return None

        next_state, action = min(
            neighbors, key=lambda x: heuristic(x[0])
        )

        if heuristic(next_state) >= heuristic(current):
            return None

        current = next_state
        path.append(action)
