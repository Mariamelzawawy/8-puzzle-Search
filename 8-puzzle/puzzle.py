#1 - define the goal state 
GOAL_STATE = (1, 2, 3,
              4, 5, 6,
              7, 8, 0) 


# 2 - get all possible sucessors from the curent state
def get_successors(state):
    successors = []
    zero_index = state.index(0)           
    row, col = divmod(zero_index, 3)     
    moves = {
        "UP": (-1, 0),
        "DOWN": (1, 0),
        "LEFT": (0, -1),
        "RIGHT": (0, 1)
    }
    for action, (dr, dc) in moves.items():
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = list(state)
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            successors.append((tuple(new_state), action))  
    return successors

# 3 - For A* and Hill Climbing
def heuristic(state):
    goal = (1,2,3,4,5,6,7,8,0)
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal_index = goal.index(state[i])
            x1, y1 = i // 3, i % 3
            x2, y2 = goal_index // 3, goal_index % 3
            distance += abs(x1 - x2) + abs(y1 - y2)

    return distance
# 4 - check if we reached the goal 
def is_goal(state):
    return state == GOAL_STATE