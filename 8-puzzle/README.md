# 8-Puzzle Search Algorithms Project

## Project Overview
This project implements multiple search algorithms to solve the 8-Puzzle problem. 
The algorithms are compared based on time complexity, space usage, solution optimality, and path cost.

## Implemented Algorithms
- Uninformed Search:
  - Breadth-First Search (BFS)
  - Depth-First Search (DFS)
  - Uniform-Cost Search (UCS)
  - Iterative Deepening Search (IDS)
- Informed Search:
  - A* Search with Manhattan Distance heuristic
  - Hill Climbing

## Initial State
(1, 2, 3,
4, 0, 6,
7, 5, 8)


## Performance Comparison
| Algorithm       | Steps | Time (ms) | Nodes Expanded | Space Used | Path Cost | Optimal |
|-----------------|-------|------------|----------------|------------|-----------|---------|
| BFS             | 2     | 0.0        | 9              | 9          | 2         | Yes     |
| DFS             | 2     | 471.15     | 140143         | 140143     | 2         | Yes     |
| UCS             | 2     | 0.0        | 14             | 14         | 2         | Yes     |
| IDS             | 2     | 0.0        | 13             | 13         | 2         | Yes     |
| A*              | 2     | 0.0        | 3              | 3          | 2         | Yes     |
| Hill Climbing   | 2     | 0.0        | 3              | 3          | 2         | Yes     |

## How to Run
1. Clone the repository
2. Open in VS Code
3. Run `main.py` 
