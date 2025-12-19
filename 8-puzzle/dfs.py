from puzzle import get_successors,is_goal

#Depth First Search Algorithm
def dfs(initial_state, limit=50):
  

    stack = []
    stack.append((initial_state, [], 0))

    visited = set()
    visited.add(initial_state)

    while stack:
        state, path, depth = stack.pop()

        if is_goal(state):
            return path

        if depth < limit:
            for next_state, action in get_successors(state):
                if next_state not in visited:
                    visited.add(next_state)
                    stack.append((next_state, path + [action], depth + 1))

    return None
