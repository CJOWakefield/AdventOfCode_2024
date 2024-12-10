from collections import deque, defaultdict

def data(path):
    lines = [line.strip() for line in open(path).readlines()]
    grid = [[char for char in line] for line in lines]
    return [list(map(int, list(line))) for line in grid]

# Helper function - valid position
def is_valid(grid, i, j):
    if (0 <= i < len(grid)) and (0 <= j < len(grid[0])):
        return True
    return False

def start_points(grid):
    starts = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                starts.append((i, j))
    return starts

def part_a(map):
    # Approach: Find all 0's as starting points. Add all to queue. BFS through queue to find any valid paths.
    starts = start_points(map)
    adjacents = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # Search nodes
    res = defaultdict(set)
    for start in starts:
        rem_positions = deque()
        rem_positions.append((start[0], start[1]))
        while rem_positions:
            i, j = rem_positions.popleft()
            if map[i][j] == 9:
                res[(start[0], start[1])].add((i, j))
                continue
            else:
                for adj in adjacents:
                    next_pos = (i+adj[0], j+adj[1])
                    if is_valid(map, next_pos[0], next_pos[1]) and (map[next_pos[0]][next_pos[1]] == map[i][j] + 1):
                        rem_positions.append((next_pos[0], next_pos[1]))
    total = 0
    for key in res:
        total += len(res[key])
    return total


def part_b(map):
    # Approach: Same as part a but can just use one queue for all nodes.
    adjacents = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    to_search = deque()
    for start in start_points(map):
        to_search.append(start)

    res = 0
    while to_search:
        i, j = to_search.popleft()
        if map[i][j] == 9:
            res += 1
            continue
        for adj in adjacents:
            next_pos = (i+adj[0], j+adj[1])
            if is_valid(map, next_pos[0], next_pos[1]) and (map[next_pos[0]][next_pos[1]] == map[i][j] + 1):
                to_search.append((next_pos[0], next_pos[1]))
    return res

# Notes: Easiest day so far. Accidentally implemented the algo for part b in first attempt for part a. Overall, no issues at all. Finished in about 15 mins.

if __name__ == '__main__':
    map = data('day_10.txt')
    print(f'Part a ---- {part_a(map)}')
    print(f'Part b ---- {part_b(map)}')
