from collections import deque, defaultdict

def data(path):
    return [tuple(map(int, line.strip().split(','))) for line in open(path).readlines()]

def is_valid(input_dim, x, y):
    if 0 <= x < input_dim and 0 <= y < input_dim:
        return True
    return False

def maze_search(bytes):
    seen = set()
    to_search = deque([(0, 0, 0)])
    adjacents = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while to_search:
        x, y, steps = to_search.popleft()
        if (x, y) == (70, 70):
            return steps
        if (x, y) in seen:
            continue
        for adj in adjacents:
            dx, dy = x + adj[0], y + adj[1]
            if is_valid(71, dx, dy) and (dx, dy) not in seen and (dx, dy) not in bytes:
                to_search.append((dx, dy, steps+1))
        seen.add((x, y))
    return None

def part_a(bytes):
    return maze_search(bytes[:1024])

def part_b(bytes):
    # Approach: Attempted out of curiosity to track each path from part_a and incrementally remove a path if the consequent byte blocked one of the required nodes. No luck. So in the end,
    # landed on binary search as the best option. Reformatted part_a into a helper function to tidy up.
    left, right = 1024, len(bytes)-1
    while right - left > 1:
        mp = (left + right) // 2
        if maze_search(bytes[:mp]):
            left = mp
        else:
            right = mp-1
    return bytes[right]

# Notes: Lots of mazes and BFS/DFS this year. No real struggles today. Few small bug fixes but overall smooth sailing. Basically the same as day 16 so revisited solution and made more concise today.

if __name__ == '__main__':
    bytes = data('day_18.txt')
    print(f'Part a ---- {maze_search(bytes[:1024])}')
    print(f'Part b ---- {part_b(bytes)}')
