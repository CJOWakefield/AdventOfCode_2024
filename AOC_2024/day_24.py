from collections import defaultdict, deque

def data(path):
    wires, connections = open(path).read().strip().split('\n\n')
    return [tuple(wire.split(': ')) for wire in wires.split('\n')], [(comb[0].split(' '), comb[1]) for comb in [tuple(conn.split(' -> ')) for conn in connections.split('\n')]]

def part_a(wires, connections):
    # Approach: Dict for wire value store and then queue until wire values resolved.
    operations = {'AND': lambda x1, x2: x1 & x2,
                  'OR': lambda x1, x2: x1 | x2,
                  'XOR': lambda x1, x2: x1 ^ x2}

    wire_values = defaultdict(str)
    for wire, val in wires:
        wire_values[wire] = val

    to_search = deque(connections)
    while to_search:
        (x1, operator, x2), output = to_search.popleft()
        if all([wire in wire_values.keys() for wire in [x1, x2]]):
            wire_values[output] = str(operations[operator](int(wire_values[x1]), int(wire_values[x2])))
        else: to_search.append(([x1, operator, x2], output))

    binary = ''.join([val for key, val in dict(sorted(wire_values.items(), reverse=True)).items() if key[0] == 'z'])
    return int(binary, 2)

if __name__ == '__main__':
    wires, connections = data('day_24.txt')

    print(f'Part a ---- {part_a(wires, connections)}')
