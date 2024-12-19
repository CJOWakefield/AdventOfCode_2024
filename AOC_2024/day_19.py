from collections import defaultdict
from functools import cache

def data(path):
    towels, designs = open(path).read().split('\n\n')
    return [towel.strip() for towel in towels.split(',')], designs.strip().split('\n')

# def pattern_possible(design, towels):
#     left, right = 0, 1
#     curr_used = []
#     invalids = defaultdict(list)
#     while left < len(design):
#         # time.sleep(0.5)
#         curr = design[left:right]
#         if right == len(design) and curr not in towels:
#             # Recursively remove last used towel since it breaks pattern
#             if curr_used:
#                 invalid = curr_used.pop(-1)
#                 left = left - len(invalid)
#                 invalids[left] = invalid
#                 right = left + 1
#                 found = False
#                 while right <= len(design):
#                     curr = design[left:right]
#                     if curr in [towel for towel in towels if towel not in invalids[left]]:
#                         curr_used.append(curr)
#                         left += len(curr)
#                         right = left + 1
#                         # print(f'{curr} found between {left}:{right}')
#                         found = True
#                         break
#                     else:
#                         right += 1
#                 if found: continue
#                 else: return False
#             else:
#                 return False
#         elif curr in towels:
#             # print(f'{curr} found between {left}:{right}')
#             curr_used.append(curr)
#             left += len(curr)
#             right = left + 1
#         else:
#             right += 1
#     return True

@cache
def design_possible(rem):
    if not rem:
        return True
    for i in range(1, len(rem)+1):
        curr = rem[:i]
        if curr in towels and design_possible(rem[i:]):
            return True
    return False

def part_a(towels, designs):
    res = 0
    for design in designs:
        if design_possible(design):
            res += 1
    return res

@cache
def solutions_possible(rem):
    if not rem:
        return 1
    solutions = 0
    for i in range(1, len(rem)+1):
        curr = rem[:i]
        if curr in towels:
            solutions += solutions_possible(rem[i:])
    return solutions

def part_b(towels, designs):
    res = 0
    for design in designs:
        if solutions_possible(design):
            res += solutions_possible(design)
    return res

# Notes: Took three attempts. Recursion was first thought but decided to try a few different routes for fun. Attempted to generate all permutations and test to see if design in resulting list, but time complexity too high.
# Then attempted a ridiculously long winded recursion method but incorrect solution (only 5 off) before realising it was a pretty straightforward string split recursion.
# Finally, wittled down to correct solution, and part b probably the easiest extension of a part a so far this year.

if __name__ == '__main__':
    towels, designs = data('day_19.txt')
    print(f'Part a ---- {part_a(towels, designs)}')
    print(f'Part b ---- {part_b(towels, designs)}')
    # print(pattern_possible('wwgubwgbrgbrrwbuugbbgrrbbrwwrrwuuuwugburrrbwbb', towels))
