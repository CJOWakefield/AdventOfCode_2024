from collections import deque
import time

def data(path):
    lines = [line.strip() for line in open(path).readlines()]
    return [[char for char in line] for line in lines]

def is_valid(grid, i, j):
    if (0 <= i < len(grid)) and (0 <= j < len(grid[0])):
        return True
    return False

def part_a(grid):
    # Approach: Store seen index positions. Build queue and expand out until region no longer expanding. Then move onto next unseen value.
    seen = set()
    adjacent = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    next = deque()
    res = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # Check if new region or not
            if (row, col) not in seen and not next:
                next.append((row, col))
                area, perimeter = 0, 0
                while next:
                    i, j = next.popleft()
                    p = 4
                    seen.add((i, j))
                    for pos in adjacent:
                        if is_valid(grid, i+pos[0], j+pos[1]) and (grid[i+pos[0]][j+pos[1]] == grid[row][col]) and (i+pos[0], j+pos[1]) not in seen:
                            next.append((i+pos[0], j+pos[1]))
                            seen.add((i+pos[0], j+pos[1]))
                            p -= 1
                    perimeter += p
                    area += 1
                res += perimeter * area
                print(f'Group finished ---- Start pos: {(row, col)}, Perimeter: {perimeter}, Area: {area}')
    return res


if __name__ == '__main__':
    lines = data('day_12.txt')
    print(f'Part a ---- {part_a(lines)}')
