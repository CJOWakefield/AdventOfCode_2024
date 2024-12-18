import numpy as np

def data(path):
    with open(path) as f:
        lines = [line.rstrip().split() for line in f]
    return lines

def is_safe(row):
    diffs = [a - b for a, b in zip(row, row[1:])]
    valid_direction = all(i > 0 for i in diffs) or all(i < 0 for i in diffs)
    valid_range = all(0 < abs(i) <= 3 for i in diffs)
    return True if valid_direction and valid_range else False

def part_a(lines):
    # Approach: Split each line into diffs between values. Check for same sign, and valid range of diffs. If not, false boolean and do not increment count.
    count = 0
    for row in lines:
        row = [int(val) for val in row]
        if is_safe(row):
            count += 1
    return count

def part_b(lines):
    # Approach: Simple implementation of safety feature. If failed initially, attempt with each position omitted. If success, we can increment.
    count = 0
    for row in lines:
        row = [int(val) for val in row]
        if is_safe(row):
            count += 1
        else:
            for i in range(len(row)):
                row_adjusted = row[:i] + row[i+1:]
                if is_safe(row_adjusted):
                    count += 1
                    break
    return count

if __name__ == '__main__':
    lines = data('day_2.txt')
    print(f'Part a ---- {part_a(lines)}')
    print(f'Part b ---- {part_b(lines)}')

# First attempt -- successful part 1. Part 2, less success.
# Second attempt -- adjust format slightly, implement is_safe function for more concise evaluation. Success in part 2.
# Conclusion -- Small selection of edge cases produced failure of first attempt. Solution reached, just a few adjustments required.
