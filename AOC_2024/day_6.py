import time
import copy

def data(path):
    lines = open(path).read().split('\n')
    return [[char for char in line] for line in lines][:-1]

def find_guard(maze):
    for i, row in enumerate(maze):
        if '^' in row:
            for j, val in enumerate(row):
                if val == '^':
                    return i, j, maze[i][j]

def exit_maze(row, col, state, maze):
    if (row == 0 and state == '^') or (row == len(maze)-1 and state == 'v') or (col == 0 and state == '<') or (col == len(maze[0])-1 and state == '>'):
        return True
    return False

def part_a(maze):
    # Approach: Simple, identify start position. 3 cases. If facing obstacle, alter state not position. Otherwise, alter position, not state. Check if position seen before.
    rotate = {'v': ['<', (1, 0)],
              '<': ['^', (0, -1)],
              '^': ['>', (-1, 0)],
              '>': ['v', (0, 1)]}

    row, col, state = find_guard(maze)
    seen = set()
    while not exit_maze(row, col, state, maze):
        next_row, next_col = row + rotate[state][1][0], col + rotate[state][1][1]
        # print(f'Current ---- {(row, col, state)}')
        if maze[next_row][next_col] == '#':
            state = rotate[state][0]
            # print(f'Turns 90 degrees to: {state}')
        elif (row, col) not in seen:
            seen.add((row, col))
            row, col = next_row, next_col
            # print(f'Now at {row, col, state}')
        else:
            row, col = next_row, next_col
            # print(f'Now at {row, col, state}')
    # Note - Include final position before exiting maze, as invalid position will not be added.
    return seen

def terminal_maze(maze, start_pos):
    rotate = {'v': ['<', (1, 0)],
              '<': ['^', (0, -1)],
              '^': ['>', (-1, 0)],
              '>': ['v', (0, 1)]}

    row, col, state = start_pos[0], start_pos[1], start_pos[2]
    seen = set()
    while not exit_maze(row, col, state, maze):
        next_row, next_col = row + rotate[state][1][0], col + rotate[state][1][1]
        if (row, col, state) in seen:
            return True
        elif maze[next_row][next_col] == '#':
            state = rotate[state][0]
        else:
            seen.add((row, col, state))
            row, col = next_row, next_col
    return False

def part_b(maze):
    # Approach: Repeat above process, for each step in route, check whether replacement with obstacle leads to previously seen position and state in the route.
    terminal_loops = 0
    rotate = {'v': ['<', (1, 0)],
              '<': ['^', (0, -1)],
              '^': ['>', (-1, 0)],
              '>': ['v', (0, 1)]}

    start_pos = find_guard(maze)
    count = 0
    positions = part_a(maze)
    for position in positions:
        temp_maze = copy.deepcopy(maze)
        temp_maze[position[0]][position[1]] = '#'
        if terminal_maze(temp_maze, start_pos):
            count += 1
            print(f'Loop found --- {count}')
    return count

# Frustrating challenge, not for the right reasons. Basically solved immediately, however multiple teething issues with small bugs
# e.g. incorrect data loading resulting in extra '[]' at end of dataset, causing out of index errors. unexplained error with loading guard start position for each iteration in part_b.

# Overall though, logic and approach perfect. Some room for improvement in terms of efficiency (takes between 10-15s to return part_b).

if __name__ == '__main__':
    map = data('day_6.txt')
    print(f'Guard position: {find_guard(map)}')
    print(part_b(map))
