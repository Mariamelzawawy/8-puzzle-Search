import time
from puzzle import is_goal, get_successors
from bfs import bfs
from dfs import dfs
from ucs import ucs
from ids import ids
from Astar import astar
from Hillclimbing import hill_climbing

initial_state = (1,2,3,4,0,6,7,5,8)


def run_algorithm(name, func, optimal_length):
    nodes_expanded = [0] 

    
    def wrapper(state):
        start = time.time()
        solution = func(state, counter=nodes_expanded)
        end = time.time()
        time_ms = (end - start) * 1000

        if solution is None:
            steps = "-"
            path_cost = "-"
            is_optimal = "No"
        else:
            steps = len(solution)
            path_cost = steps
            is_optimal = "Yes" if steps == optimal_length else "No"

        return {
            "Steps": steps,
            "Time(ms)": round(time_ms, 2),
            "Nodes Expanded": nodes_expanded[0],
            "Space Used": nodes_expanded[0],  
            "Path Cost": path_cost,
            "Optimal": is_optimal
        }

    return wrapper(initial_state)

def bfs_counter(state, counter=None):
    from collections import deque
    queue = deque()
    queue.append((state, []))
    visited = set()
    visited.add(state)

    while queue:
        current, path = queue.popleft()
        if counter: counter[0] += 1

        if is_goal(current):
            return path

        for next_state, action in get_successors(current):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [action]))
    return None

def dfs_counter(state, counter=None, limit=50):
    stack = [(state, [], 0)]
    visited = set()
    visited.add(state)

    while stack:
        current, path, depth = stack.pop()
        if counter: counter[0] += 1

        if is_goal(current):
            return path

        if depth < limit:
            for next_state, action in get_successors(current):
                if next_state not in visited:
                    visited.add(next_state)
                    stack.append((next_state, path + [action], depth + 1))
    return None

def ucs_counter(state, counter=None):
    import heapq
    pq = []
    heapq.heappush(pq, (0, state, []))
    visited = set()

    while pq:
        cost, current, path = heapq.heappop(pq)
        if counter: counter[0] += 1

        if is_goal(current):
            return path

        if current not in visited:
            visited.add(current)
            for next_state, action in get_successors(current):
                heapq.heappush(pq, (cost + 1, next_state, path + [action]))
    return None

def ids_counter(state, counter=None, max_depth=50):
    def dls(s, path, depth, limit):
        if counter: counter[0] += 1
        if is_goal(s):
            return path
        if depth == limit:
            return None
        for next_state, action in get_successors(s):
            if next_state not in visited:
                visited.add(next_state)
                result = dls(next_state, path + [action], depth + 1, limit)
                if result:
                    return result
        return None

    for depth in range(max_depth):
        visited = set()
        visited.add(state)
        result = dls(state, [], 0, depth)
        if result:
            return result
    return None

def astar_counter(state, counter=None):
    import heapq
    from puzzle import heuristic
    pq = []
    heapq.heappush(pq, (heuristic(state), 0, state, []))
    visited = set()

    while pq:
        f, g, current, path = heapq.heappop(pq)
        if counter: counter[0] += 1

        if is_goal(current):
            return path

        if current not in visited:
            visited.add(current)
            for next_state, action in get_successors(current):
                new_g = g + 1
                new_f = new_g + heuristic(next_state)
                heapq.heappush(pq, (new_f, new_g, next_state, path + [action]))
    return None

def hill_climbing_counter(state, counter=None):
    from puzzle import heuristic
    current = state
    path = []

    while True:
        if counter: counter[0] += 1
        if is_goal(current):
            return path

        neighbors = get_successors(current)
        if not neighbors:
            return None

        next_state, action = min(neighbors, key=lambda x: heuristic(x[0]))
        if heuristic(next_state) >= heuristic(current):
            return None

        current = next_state
        path.append(action)


optimal_solution_length = len(bfs_counter(initial_state, counter=[0]))


algorithms = {
    "BFS": bfs_counter,
    "DFS": dfs_counter,
    "UCS": ucs_counter,
    "IDS": ids_counter,
    "A*": astar_counter,
    "Hill Climbing": hill_climbing_counter
}

# Run all
results = {}
for name, func in algorithms.items():
    print(f"Running {name}...")
    results[name] = run_algorithm(name, func, optimal_solution_length)

# Print table
print("\nPerformance Table:")
header = ["Algorithm", "Steps", "Time(ms)", "Nodes Expanded", "Space Used", "Path Cost", "Optimal"]
print("{:<15} {:<6} {:<10} {:<15} {:<10} {:<10} {:<8}".format(*header))
for name, metrics in results.items():
    print("{:<15} {:<6} {:<10} {:<15} {:<10} {:<10} {:<8}".format(
        name, metrics["Steps"], metrics["Time(ms)"], metrics["Nodes Expanded"],
        metrics["Space Used"], metrics["Path Cost"], metrics["Optimal"]
    ))



