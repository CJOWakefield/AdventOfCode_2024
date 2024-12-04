import numpy as np
import re

def data(path):
    return open('day_3.txt').read()

def part_a(lines):
    # Approach: use re to find all correct formats, and then isolate integer strings. Convert and then return sum.
    matches = re.findall('(?:mul\\(([0-9]{1,3}),([0-9]{1,3})\\))', lines)
    return sum([int(match[0]) * int(match[1]) for match in matches])

def part_b(lines):
    # Approach: Same as part a but also filter for do() / don't(). Then use boolean to track do/don't inversion for next match.
    matches = re.findall("(don't\\(\\))|(do\\(\\))|(?:mul\\(([0-9]{1,3}),([0-9]{1,3})\\))", lines)
    res, valid = 0, True
    for match in matches:
        if match[0] == "don't()":
            valid = False
        elif match[1] == "do()":
            valid = True
        elif valid:
            res += int(match[2]) * int(match[3])
    return res

if __name__ == '__main__':
    lines = data('day_3.txt')
    print(part_a(lines))
    # print(re.findall("(don't\\(\\))|(do\\(\\))|(?:mul\\(([0-9]{1,3}),([0-9]{1,3})\\))", lines))
