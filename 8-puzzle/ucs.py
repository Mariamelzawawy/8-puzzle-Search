import heapq
from puzzle import get_successors, is_goal

#Unifrom Cost Search Algorithm 
def ucs(initial_state):
   

    pq = []
    heapq.heappush(pq, (0, initial_state, []))

    visited = set()

    while pq:
        cost, state, path = heapq.heappop(pq)

        if is_goal(state):
            return path

        if state not in visited:
            visited.add(state)

            for next_state, action in get_successors(state):
                heapq.heappush(pq, (cost + 1, next_state, path + [action]))

    return None
