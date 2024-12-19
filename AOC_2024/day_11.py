import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

def data(path):
    return list(map(int, open(path).readline().strip().split()))

def part_a(line):
    for _ in range(25):
        ammended = []
        for i, val in enumerate(line):
            if val == 0:
                ammended.append(val+1)
            elif len(str(val))%2 == 0:
                char_split = len(str(val))//2
                left, right = str(val)[:char_split], str(val)[char_split:]
                ammended.extend([int(left), int(right)])
            else:
                ammended.append(val * 2024)
        line = ammended
        print(f'Iteration {_} complete.')
    return ammended

# Time complexity increases exponentially -> part_a not viable. Need to cache seen expansions recursively.
def stone_split(seen, val, depth):
    if depth == 0:
        return 1
    if val in seen[depth]:
        return seen[depth][val]
    if val == 0:
        seen[depth][val] = stone_split(seen, 1, depth-1)
    elif len(str(val)) % 2 == 0:
        val_str = str(val)
        seen[depth][val] = stone_split(seen, int(val_str[:len(val_str)//2]), depth-1) + stone_split(seen, int(val_str[len(val_str)//2:]), depth-1)
    else:
        seen[depth][val] = stone_split(seen, val * 2024, depth-1)
    return seen[depth][val]

def part_b(line):
    seen = [{} for _ in range(76)]
    for i in range(76):
        _ = [stone_split(seen, val, i) for val in line]
    return sum([stone_split(seen, val, i) for val in line])

# Notes: Part a simple as usual. Part b, fairly straightforward with a little bit of work on teething issues. Overall, nice refresher on recursion.

if __name__ == '__main__':
    line = data('day_11.txt')
    print(f'Part a ---- {len(part_a(line))}')
    print(f'Part b ---- {part_b(line)}')
