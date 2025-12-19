import heapq
from puzzle import get_successors, is_goal, heuristic

#A* Search Algorithm
def astar(initial_state):
    pq = []
    heapq.heappush(pq, (heuristic(initial_state), 0, initial_state, []))

    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if is_goal(state):
            return path

        if state not in visited:
            visited.add(state)

            for next_state, action in get_successors(state):
                new_g = g + 1
                new_f = new_g + heuristic(next_state)
                heapq.heappush(pq, (new_f, new_g, next_state, path + [action]))

    return None
