from collections import deque

def data(path):
    lines = open(path).readlines()
    for pos, line in enumerate(lines):
        if len(line.strip()) == 0:
            cutoff = pos
    grid, path = lines[:cutoff], lines[cutoff+1:]
    return [[char for char in line.strip()] for line in grid], ''.join([path_line.strip() for path_line in path])

def robot_pos(grid):
    for i, line in enumerate(grid):
        for j, char in enumerate(line):
            if char == '@':
                return (i, j)

def calculate(grid):
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                res += (i * 100) + j
    return res

def part_a(grid, path):
    i, j = robot_pos(grid)
    moves = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}
    for move in path:
        dx, dy = i + moves[move][0], j + moves[move][1]
        if grid[dx][dy] == '#':
            continue
        elif grid[dx][dy] == '.':
            grid[i][j], grid[dx][dy] = grid[dx][dy], grid[i][j]
            i, j = dx, dy
        else:
            dx_2, dy_2 = dx + moves[move][0], dy + moves[move][1]
            while grid[dx_2][dy_2] == 'O':
                dx_2 += moves[move][0]
                dy_2 += moves[move][1]
            if grid[dx_2][dy_2] == '.':
                grid[dx][dy], grid[dx_2][dy_2] = '.', 'O'
            else:
                continue
            grid[i][j], grid[dx][dy] = grid[dx][dy], grid[i][j]
            i, j = dx, dy

    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                res += (i * 100) + j
    return res

def grid_adjusted(path):
    grid, path = open('day_15.txt').read().split('\n\n')
    robot_pos = grid.index('@')
    return [[('[' if i % 2 == 0 else ']') if line[i // 2] == 'O' else line[i // 2] for i in range(len(line) * 2)] for line in grid.split()], ''.join(path.split()), robot_pos

# Realised here that mixing i, j and x, y was not so readable.
def part_b(path):
    # Approach: Same idea as part_a, but needs some adjustments due to grid shift. Plan to split vertical and horizontal moves.
    moves = {'<': -1, '>': 1, '^': -1, 'v': 1}
    grid, path, robot_pos = grid_adjusted('day_15.txt')
    x, y = robot_pos % (len(grid[0]) // 2), robot_pos // (len(grid[0]) // 2)
    grid[y][x], grid[y][x+1] = '.', '.'
    for move in path:
        if move in ['>', '<']:
            x1 = x + (moves[move])
            while grid[y][x1] in ['[', ']']: x1 += moves[move]
            if grid[y][x1] == '.':
                for x2 in range(x1, x, -moves[move]): grid[y][x2] = grid[y][x2 - moves[move]]
                x += moves[move]
        else:
            boxes = [{(x, y)}]
            while boxes[-1]:
                boxes.append(set())
                for box in boxes[-2]:
                    if grid[box[1] + moves[move]][box[0]] == '#': break
                    if grid[box[1] + moves[move]][box[0]] == '[':
                        boxes[-1] |= {(box[0], box[1] + moves[move]), (box[0] + 1, box[1] + moves[move])}
                    elif grid[box[1] + moves[move]][box[0]] == ']':
                        boxes[-1] |= {(box[0], box[1] + moves[move]), (box[0] - 1, box[1] + moves[move])}
                else: continue
                break
            else:
                for row in list(reversed(boxes)):
                    for box in row:
                        grid[box[1] + moves[move]][box[0]], grid[box[1]][box[0]] = grid[box[1]][box[0]], '.'
                y += moves[move]

    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '[':
                res += (100 * i) + j
    return res

# Notes: Part a was a breeze. Honestly, part b was a struggle. Inuitively, the triangular shift of boxes when overlapping a big hump. After multiple hours of attempts, read up on other
# solutions online and reimplemented by self. Need to revisit logic on this one. Cool puzzle overall.

if __name__ == '__main__':
    grid, path = data('day_15.txt')
    print(f'Part a ---- {part_a(grid, path)}')
    print(f'Part b ---- {part_b("day_15.txt")}')
