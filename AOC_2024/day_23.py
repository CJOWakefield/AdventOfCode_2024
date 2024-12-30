from collections import defaultdict
import itertools


def data(path):
    return [tuple(line.strip().split('-')) for line in open(path).readlines()]

def part_a(connections):
    conn_dict = defaultdict(set)
    for connection in connections:
        c1, c2 = connection
        conn_dict[c1].add(c2)
        conn_dict[c2].add(c1)

    res = []
    for key, val in [(key, val) for key, val in conn_dict.items() if key[0] == 't']:
        combinations = list(itertools.combinations(val, 2))
        for comb in combinations:
            if comb[0] in conn_dict[comb[1]]:
                res.append((key, comb[0], comb[1]))
    return len(set([tuple(sorted(trio)) for trio in res]))

def part_b(connections):
    # Approach: Queue each key in dict. Explore every connection node and check each connects then add iteratively.
    conn_dict = defaultdict(set)
    for connection in connections:
        c1, c2 = connection
        conn_dict[c1].add(c2)
        conn_dict[c2].add(c1)

    groups = set()
    to_search = [(computer, frozenset({computer})) for computer in conn_dict]
    while to_search:
        computer, group = to_search.pop()
        for unconnected in conn_dict[computer]-group:
            if all(comp in conn_dict[unconnected] for comp in group):
                new_group = group.union([unconnected])
                if new_group not in groups:
                    groups.add(new_group)
                    to_search.append((unconnected, new_group))
    return sorted(max(groups, key=len))

# Notes: Simple part_a. Part b tried some fairly straightforward logic by simply iterating through values for each key and
# checking each other value connected. Then returning the max len. Didn't reach the solution though. Substituted for a stack, incrementing individual computer groups by checking values
# as they chain on to one another. Took a while to come back and polish up but overall not a bad day.

if __name__ == '__main__':
    connections = data('day_23.txt')
    print(f'Part a ---- {part_a(connections)}')
    print(f'Part b ---- {",".join(part_b(connections))}')
