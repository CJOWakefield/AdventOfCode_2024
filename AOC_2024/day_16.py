from collections import deque, defaultdict
import numpy as np

def data(path):
    return [[char for char in line.strip()] for line in open(path).readlines()]

def start_finish(grid):
    S = [(i, row.index('S')) if 'S' in row else 0 for i, row in enumerate(grid)]
    E = [(i, row.index('E')) if 'E' in row else 0 for i, row in enumerate(grid)]
    return next((val for val in S if val), None), next((val for val in E if val), None)

def part_a(grid):
    # Approach: Simple BFS, with directionary tracking and cost included to track path cost.
    (i, j), (target_i, target_j) = start_finish(grid)
    # Northwards, Southwards, Westwards, Eastwards
    adjacent = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    to_search = deque()
    seen = defaultdict(lambda: float('inf'))
    curr_min = float('inf')
    # Search params: row, col, previous position (E.g. direction) and total cost to reach node
    to_search.append((i, j, (0, 1), 0))
    while to_search:
        i, j, direction, cost = to_search.popleft()
        if (i, j) == (target_i, target_j):
            if cost < curr_min:
                print(f'New best found: {cost} < {curr_min}')
                curr_min = cost

        for adj in adjacent:
            # No backtracking
            dx, dy = i + adj[0], j + adj[1]
            if grid[dx][dy] != '#' and seen[(dx, dy)] >= cost:
                if direction == adj:
                    to_search.append((dx, dy, direction, cost + 1))
                else:
                    to_search.append((dx, dy, adj, cost + 1001))
                seen[(dx, dy)] = cost
    return curr_min

def part_b(grid, optimum):
    # Approach: Same idea, but DFS search. Implement dictionary for each node in queue of previous nodes. Upon successful completion, increment another dict with positions if passed on that route.
    paths = []
    (i, j), (target_i, target_j) = start_finish(grid)
    adjacent = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    to_search = deque([(i, j, (0, 1), 0, set([(i, j)]))])
    seen = defaultdict(lambda: float('inf'))

    while to_search:
        i, j, direction, cost, route = to_search.popleft()
        if (i, j) == (target_i, target_j):
            paths.append(route)
            continue
        # Ignore nodes that already exceed current optimum or could not reach endpoint within budget even with direct path
        if cost >= optimum:
            continue
        for adj in adjacent:
            dx, dy = i + adj[0], j + adj[1]
            if grid[dx][dy] == '#':
                continue
            d_cost = cost + 1 if direction == adj else cost + 1001
            if (dx, dy) not in route and seen[(dx, dy)] >= d_cost-1000:
                adjusted_route = route.copy()
                adjusted_route.add((dx, dy))
                to_search.append((dx, dy, adj, d_cost, adjusted_route))
                seen[(dx, dy)] = d_cost

    total = set()
    for path in paths:
        total.update(path)
    return len(list(total))

# Notes: Easy day but once again, some strange results that I struggled to bug fix. Implemented DFS in part_b initially (just for a refresher). Part b, kept getting the wrong answer in the right ballpark.
# Still not sure what is causing the disparity. Optimal cost obtained but for some reason not all optimal routes being found. Suspicion is that early turns are penalised.

# Secondary note after revisting: Solution finally reached. Tiny error in optimisation but line 62 originally seen[(dx, dy)] >= d_cost. Meant algo ignored routes that turned earlier but would not need to turn again upon (dx, dy) where another path would.

if __name__ == '__main__':
    grid = data('day_16.txt')
    a = part_a(grid)
    res = part_b(grid, a)
    print(f'\nPart a ---- {a}')
    print(f'Part b ---- {res}')
