def data(path):
    return open(path).read().split('\n')[:-1]

# Helper functions
def valid_position(lines, x, y):
    if (x < 0) or (y < 0) or (len(lines) <= x) or (len(lines[0]) <= y):
        return None
    return lines[x][y]

def part_a(lines):
    # Approach: For each X, check valid adjacent squares consecutively spell target. If not, break and continue, else iterate.
    count, adjacent = 0, [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            if lines[row][col] == 'X':
                # Check each potential direction of adjacents - e.g. diagonals, rows, cols
                for pos in adjacent:
                    valid = True
                    for i in range(3):
                        dx = row + (i+1) * pos[0]
                        dy = col + (i+1) * pos[1]
                        # Assert that each character falls correctly (sequentially) for the target word.
                        if valid_position(lines, dx, dy) != ['M', 'A', 'S'][i]:
                            valid = False
                            break
                    if valid:
                        count += 1
    return count

def part_b(lines):
    # Approach: No increased complexity, just different format. Check corners of A to find valid results.
    count = 0
    for row in range(len(lines)):
        for col in range(len(lines[0])):
            if valid_position(lines, row, col) == 'A':
                # Check first set of corners -> top left, bottom right
                c1 = valid_position(lines, row-1, col-1)
                c2 = valid_position(lines, row+1, col+1)
                if (c1 == 'M' or c1 == 'S') and (c2 == 'M' or c2 =='S') and (c1 != c2):
                    # Check second set of corners -> top right, bottom left
                    c3 = valid_position(lines, row-1, col+1)
                    c4 = valid_position(lines, row+1, col-1)
                    if (c3 == 'M' or c3 == 'S') and (c4 == 'M' or c4 =='S') and (c3 != c4):
                        count += 1
    return count

if __name__ == '__main__':
    lines = data('day_4.txt')
    print(f'Part a ---- {part_a(lines)}')
    print(f'Part b ---- {part_b(lines)}')
