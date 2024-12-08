def data(path):
    rows = open(path).read().split('\n')[:-1]
    equations = [row.split(': ') for row in rows]
    return [(int(eq[0]), [int(val) for val in eq[1].split(' ')]) for eq in equations]


def part_a(rows):

    for row in rows:
        target, vals = row[0], row[1]


# if __name__ == '__main__':
#     rows = data('day_7.txt')
#     print(rows)

ex = 2000
vals = [2, 500, 500, 2]

adds, multips = [], []
for i in range(1, len(vals)):
    adds.append(vals[i] + vals[i-1])
    multips.append(vals[i] * vals[i-1])

print(adds, multips)
