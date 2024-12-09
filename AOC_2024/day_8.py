from collections import defaultdict

def data(path):
    return [[char for char in line.strip()] for line in open(path).readlines()]


def char_positions(lines):
    char_pos = defaultdict(list)
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            char_pos[lines[i][j]].append((i, j))
    _, _ = char_pos.pop('.', None), char_pos.pop('\n', None)
    return char_pos


def is_valid(lines, i, j):
    if (0 <= i < len(lines)) and (0 <= j < len(lines[0])):
        return True
    return False


def part_a(lines):
    # Approach: Create dict of positions for each char. Iterate through each char, find relevant antinodes and add (i,j) to set. Return length of set.
    char_pos = char_positions(lines)
    antinodes = set()
    for char in char_pos.keys():
        for i, val in enumerate(char_pos[char]):
            for alt_val in char_pos[char][i+1:]:
                dx, dy = alt_val[0]-val[0], alt_val[1]-val[1]
                # Extend line in negative and positive axis (either side of antennae)
                x1, y1 = val[0]-dx, val[1]-dy
                x2, y2 = alt_val[0]+dx, alt_val[1]+dy
                if is_valid(lines, x1, y1):
                    antinodes.add((x1, y1))

                if is_valid(lines, x2, y2):
                    antinodes.add((x2, y2))
    return antinodes


def part_b(lines):
    # Approach: Same as part_a, introduce while loop and iterate until invalid position.
    char_pos = char_positions(lines)
    antinodes = set()
    for char in char_pos.keys():
        for i, val in enumerate(char_pos[char]):
            for alt_val in char_pos[char][i+1:]:
                dx, dy = alt_val[0]-val[0], alt_val[1]-val[1]
                # Extend line in negative and positive axis (either side of antennae)
                x1, y1 = val[0]-dx, val[1]-dy
                x2, y2 = alt_val[0]+dx, alt_val[1]+dy
                # Each antenna must now also be an anti-node
                antinodes.add(val)
                antinodes.add(alt_val)
                # Continue along path until no longer within grid
                while is_valid(lines, x1, y1):
                    antinodes.add((x1, y1))
                    x1, y1 = x1-dx, y1-dy

                while is_valid(lines, x2, y2):
                    antinodes.add((x2, y2))
                    x2, y2 = x2+dx, y2+dy
    return antinodes


# Visualiser
def show_antinodes(map, antinodes):
    for node in antinodes:
        map[node[0]][node[1]] = '#'
    return [''.join(line) for line in map]


# Notes: No issues here. Logic fairly intuitive. Only errors due to incorrect variable names but overall, challenge finished quickly.

if __name__ == '__main__':
    map = data('day_8.txt')
    print(f'Part a ---- {len(part_a(map))}')
    print(f'Part b ---- {len(part_b(map))}')

    # for line in show_antinodes(map, part_b(map)):
    #     print(line)
