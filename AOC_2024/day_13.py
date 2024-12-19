import re
from collections import deque
import time
import scipy

def data(path):
    lines = open(path).read()
    rules = re.findall(r'[+=](\w+)', lines)
    return [list(map(int, rule)) for rule in [rules[i:i+6] for i in range(0, len(rules), 6)]]

def part_a(games):
    # Approach: Queue for each game, add all successful button combinations to list. Search list for lowest cost.
    res = 0
    for game in games:
        paths = []
        seen = set()
        a_x, a_y, b_x, b_y, x_target, y_target = game
        # Start queue with first two options: a press and b press.
        to_search = deque()
        to_search.extendleft([(a_x, a_y, 3), (b_x, b_y, 1)])
        while to_search:
            x, y, cost = to_search.popleft()
            if (x > x_target or y > y_target):
                continue
            elif (x == x_target and y == y_target):
                paths.append((x, y, cost))
            else:
                if (x, y) not in seen:
                    to_search.extendleft([(x+a_x, y+a_y, cost+3), (x+b_x, y+b_y, cost+1)])
                    seen.add((x, y))
        if paths:
            res += min([path[2] for path in paths])
    return res

def part_b(games):
    # Approach: A strategy no longer viable due to exponential time complexity.
    res = 0
    offset = 10000000000000
    for game in games:
        a_x, a_y, b_x, b_y, x_target, y_target = game
        x_target += offset
        y_target += offset
        a_press = ((x_target * b_y) - (y_target * b_x)) / ((a_x * b_y) - (a_y * b_x))
        b_press = (x_target - (a_x * a_press)) / b_x
        if a_press % 1 == b_press % 1 == 0:
            res += int(a_press * 3 + b_press)
    return res

# Notes: Part a easy. Approach not optimal though and not viable for part b. Took some thought but eventually landed on it being a linear restraint problem. Implement constraint based
# optimisation to find solution. Assert for integer values. Attempted via scipy but no success (I suspect due to rounding issues?)

if __name__ == '__main__':
    games = data('day_13.txt')
    print(f'Part a ---- {part_a(games)}')
    print(f'Part b ---- {part_b(games)}')
