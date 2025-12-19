from collections import deque
from puzzle import get_successors,is_goal

#BREADTH FIRST SEARCH ALGORITHM 
def bfs(initial_state):
    queue = deque()
    queue.append((initial_state, []))

    visited = set()
    visited.add(initial_state)

    while queue:
        state, path = queue.popleft()

        if is_goal(state):
            return path

        for next_state, action in get_successors(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [action]))

    return None
