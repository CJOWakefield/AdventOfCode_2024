import re
import numpy as np
from collections import defaultdict

def data(path):
    return [re.findall(r'[+-]?\d+', line.strip()) for line in open(path).readlines()]

def part_a(lines, grid_width, grid_height):
    # Approach: In O(n) time, we can add v(x, y) to x0, y0 150x and subtract the excess over x_max, y_max to obtain the new co-ordinates
    quad = defaultdict(list)
    for guard in lines:
        x0, y0, dx, dy = int(guard[0]), int(guard[1]), int(guard[2]), int(guard[3])
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

if __name__ == '__main__':
    lines = data('day_14.txt')
    print(part_a(lines, 101, 103))
