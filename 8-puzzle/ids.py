from puzzle import get_successors,is_goal

 
#Iterative Deepening Search
def dls(state, path, depth, limit, visited):
    if is_goal(state):
        return path

    if depth == limit:
        return None

    for next_state, action in get_successors(state):
        if next_state not in visited:
            visited.add(next_state)
            result = dls(next_state, path + [action], depth + 1, limit, visited)
            if result:
                return result
    return None


def ids(initial_state, max_depth=50):
    for depth in range(max_depth):
        visited = set()
        visited.add(initial_state)
        result = dls(initial_state, [], 0, depth, visited)
        if result:
            return result
    return None
