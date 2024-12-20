from collections import deque, defaultdict
from itertools import combinations

def data(path):
    grid = open(path).read().split('\n')[:-1]
    start, end = ''.join(grid).index('S'), ''.join(grid).index('E')
    grid = [[char for char in line.strip()] for line in grid]
    return grid, (start % (len(grid[0])), start // (len(grid[0]))), (end % len(grid[0]), end // len(grid[0]))

def is_valid(grid, x, y):
    if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
        return True
    return False

def grid_solve(grid, start, end):
    seen = set()
    to_search = deque([(start[0], start[1], 0, [])])
    adjacents = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while to_search:
        x, y, steps, route = to_search.popleft()
        if (x, y) == end:
            route.append((x, y))
            return steps, route
        if (x, y) in seen:
            continue
        for adj in adjacents:
            dx, dy = x + adj[0], y + adj[1]
            new_route = route.copy()
            if is_valid(grid, dx, dy) and (dx, dy) not in seen and grid[dy][dx] != '#':
                new_route.append((x, y))
                to_search.append((dx, dy, steps+1, new_route))
        seen.add((x, y))
    return None

def part_a(grid, route, skip):
    res = 0
    adjacents = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # route_costs = route_convert(route)
    for pos in route:
        x, y = pos[0], pos[1]
        for adj in adjacents:
            dx, dy = x + skip * adj[0], y + skip * adj[1]
            if is_valid(grid, dx, dy) and (dx, dy) in route.keys():
                # print(f'Pos: {pos} at index {i} can cheat to reach {(dx, dy)} at index {route.index((dx, dy))}')
                base_cost = route[(dx, dy)] - route[(x, y)]
                new_cost = abs(x-dx) + abs(y-dy)
                if (base_cost - new_cost) >= 100:
                    res += 1
    return res

def route_convert(route):
    res = defaultdict(int)
    for i, pos in enumerate(route):
        res[pos] = i
    return res

def part_b(route, skip=20):
    res = 0
    # route_costs = route_convert(route)
    for curr, next in combinations(route.keys(), 2):
        base_cost = route[next] - route[curr]
        new_cost = abs(curr[0]-next[0]) + abs(curr[1]-next[1])
        # Resulting point close enough to skip and saves enough time
        if new_cost <= skip and (base_cost - new_cost) >= 100:
            res += 1
    return res

# Notes: Honestly, pretty frustrating one. Lots of ideas for approaches but first few way too time intensive. BFS while retaining skips way too long. BFS along route with walls only until reaching a further
# point along the path showed promise but moved on due to several teething bugs. Eventually took that idea but removed the BFS part, simply tracking for each position, all then nearby positions using the skip
# that could now be accessed, and determining the difference in path length as a result. Time comp for B somewhat high but not too bad.

if __name__ == '__main__':
    grid, start, end = data('day_20.txt')
    cost, route = grid_solve(grid, start, end)
    route = route_convert(route)
    print(f'Part a ---- {part_a(grid, route, skip=2)}')
    print(f'Part b ---- {part_b(route, skip=20)}')
