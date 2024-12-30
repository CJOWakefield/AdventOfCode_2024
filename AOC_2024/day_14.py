import re
import numpy as np
from collections import defaultdict

def data(path):
    return [re.findall(r'[+-]?\d+', line.strip()) for line in open(path).readlines()]

def part_a(lines, grid_width, grid_height):
    # Approach: In O(n) time, we can add v(x, y) to x0, y0 150x and subtract the excess over x_max, y_max to obtain the new co-ordinates
    quad = defaultdict(list)
    for guard in lines:
        x0, y0, dx, dy = list(map(int, guard))
        x_final, y_final = x0 + (100 * dx), y0 + (100 * dy)

        while x_final < 0 or x_final >= grid_width:
            x_final -= grid_width * np.sign(x_final)
        while y_final < 0 or y_final >= grid_height:
            y_final -= grid_height * np.sign(y_final)

        if (x_final == grid_width // 2) or (y_final == grid_height // 2):
            continue
        elif (x_final < grid_width // 2) and (y_final < grid_height // 2):
            quad[1].append((x_final, y_final))
        elif (x_final > grid_width // 2) and (y_final < grid_height // 2):
            quad[2].append((x_final, y_final))
        elif (x_final < grid_width // 2) and (y_final > grid_height // 2):
            quad[3].append((x_final, y_final))
        else:
            quad[4].append((x_final, y_final))
    res = 1
    for key in quad.keys():
        res *= len(quad[key])
    return res


def part_b(lines, grid_width, grid_height):
    # Approach: Read up hint for intuition surrounding tree occurence when all guards are stationed alone.
    iter = 1
    while True:
        valid_iter = True
        grid = [['.' for _ in range(grid_width)] for _ in range(grid_height)]
        for guard in lines:
            x0, y0, dx, dy = list(map(int, guard))
            x1, y1 = (x0 + (iter * dx)) % grid_width, (y0 + (iter * dy)) % grid_height
            if grid[y1][x1] != '.':
                valid_iter = False
            else: grid[y1][x1] = 'X'

        if valid_iter: return iter, grid
        iter += 1

# Notes: Completely forgot about this until revisting for the Christmas day challenge. Part_a a breeze. Part b a breeze once I knew the intuition but didn't work it out alone.

if __name__ == '__main__':
    lines = data('day_14.txt')
    print(f'Part a ---- {part_a(lines, 101, 103)}')
    iter, grid = part_b(lines, 101, 103)
    print('\n----------------------------------\n')
    for line in grid:
        print(''.join(line))
    print('\n----------------------------------\n')
    print(f'Part b ---- {iter}')
