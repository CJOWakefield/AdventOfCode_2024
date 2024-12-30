import itertools

def data(path):
    grids = [grid.split('\n') for grid in open(path).read().strip().split('\n\n')]
    locks, pins = [grid for grid in grids if all([char == '#' for char in grid[0]])], [grid for grid in grids if all([char == '.' for char in grid[0]])]
    return locks, pins

def part_a(locks, pins):
    lock_heights = [[sum([0 if (row[i] == '.' and j > 0) else 1 for j, row in enumerate(lock)])-1 for i in range(len(lock[0]))] for lock in locks]
    pin_heights = [[sum([0 if (row[i] == '.' and j < len(pin)-1) else 1 for j, row in enumerate(pin)])-1 for i in range(len(pin[0]))] for pin in pins]

    res = 0
    for comb in list(itertools.product(lock_heights, pin_heights)):
        overlaps = [comb[0][i] + comb[1][i] for i in range(len(comb[0]))]
        if all([True if len(overlaps) >= val else False for val in overlaps]):
            res += 1
    return res

# Notes: Incredibly easy final problem. Happy days. Completed within 15 mins.

if __name__ == '__main__':
    locks, pins = data('day_25.txt')
    print(f'Part a ---- {part_a(locks, pins)}')
