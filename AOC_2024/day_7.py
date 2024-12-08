import itertools
import time

def data(path):
    rows = open(path).readlines()
    equations = [row.split(': ') for row in rows]
    return [(int(eq[0]), [int(val) for val in eq[1].split(' ')]) for eq in equations]


def part_a(rows):
    # Approach: Create permuations from inputting '+' or '*' inbetween int values. Calculate result of calculating resulting permuation.
    res = 0
    for row in rows:
        target, vals = row[0], row[1]
        permutations = list(itertools.product(['*', '+'], repeat=len(vals)-1))
        for permutation in permutations:
            # Take each symbol, and execute on following index position in vals
            sum = vals[0]
            for i, symbol in enumerate(permutation):
                if sum > target:
                    break
                if symbol == '*':
                    sum *= vals[i+1]
                else:
                    sum += vals[i+1]
            if sum == target:
                res += target
                break
    return res


def part_b(rows):
    # Approach same. Introduce new operator. Only consideration at first glance is an impact on indexing from part a.
    res = 0
    for row in rows:
        target, vals = row[0], row[1]
        permutations = list(itertools.product(['*', '+', '||'], repeat=len(vals)-1))
        for permutation in permutations:
            sum = vals[0]
            for i, symbol in enumerate(permutation):
                # Retrospective implementation for efficiency - sum only increments so whenever sum > target, we can assume that equatiom won't converge.
                if sum > target:
                    break
                if symbol == '*':
                    sum *= vals[i+1]
                elif symbol == '+=':
                    sum += vals[i+1]
                else:
                    sum = int(str(sum) + str(vals[i+1]))
            if sum == target:
                res += sum
                print(res)
                break
    return res


# Recursive function
def possible_perms(vals):
    # Base case: One remaining value
    if len(vals) == 1:
        return vals
    # Logic: Perform each operand iteratively to reduce vals, then repeat recursively to obtain all outcomes.
    return (possible_perms([vals[0] + vals[1]] + vals[2:]) +
            possible_perms([vals[0] * vals[1]] + vals[2:]) +
            possible_perms([int(''.join([str(vals[0]), str(vals[1])]))] + vals[2:]))


def part_b_recursive_mapping(rows):
    sum = 0
    for row in rows:
        target, vals = row[0], row[1]
        if target in possible_perms(vals):
            sum += target
            # print(sum)
    return sum

# Notes: Easy challenge all round. Part b a simple extension of part a, with some thought lent to time complexity.
# Re-attempted part b after reading a solution using mapping and recursion. Not my first instinct for solving but
# definitely optimal in terms of both time and code efficiency.

if __name__ == '__main__':
    rows = data('day_7.txt')
    print(part_b_recursive_mapping(rows))
