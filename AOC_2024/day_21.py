from collections import defaultdict, deque
import numpy as np
import time
import functools

def data(path):
    return [line.strip() for line in open(path).readlines()]

# Notes: If '<<^', always split with the ^/v

# Approach ideas: BFS on keypad and direction pad to find the shortest path for each key pairing

# def code_output(code, number_input=False):
#     # Produce relevant robot input for set of order code
#     numberpad = {'0': (1, 0), '1': (0, 1), '2': (1, 1), '3': (2, 1), '4': (0, 2), '5': (1, 2), '6': (2, 2), '7': (0, 3), '8': (1, 3), '9': (2, 3), 'A': (2, 0)}
#     directions = {'<': (0, 0), 'v': (1, 0), '>': (2, 0), '^': (1, 1), 'A': (2, 1)}
#     pad = numberpad if number_input else directions
#     inputs, curr = [], 'A'
#     for input_val in code:
#         d_n1_x, d_n1_y = pad[input_val][0] - pad[curr][0], pad[input_val][1] - pad[curr][1]
#         if not number_input:
#             dir_x = '<' if np.sign(d_n1_x) == -1 else '>'
#             dir_y = 'v' if np.sign(d_n1_y) == -1 else '^'
#             # # Cases: '>> always in duos and first. Double < always split by dy.
#             if dir_x == '<' and np.abs(d_n1_x) > 1 and np.abs(d_n1_y) > 0:
#                 controls = [dir_x + dir_y + dir_x] + [['A']]
#             else:
#                 controls = [dir_x * abs(d_n1_x)] + [dir_y * abs(d_n1_y)] + [['A']]
#         else:
#             controls = [abs(d_n1_x) * ['<'] if np.sign(d_n1_x) == -1 else abs(d_n1_x) * ['>']] + [abs(d_n1_y) * ['v'] if np.sign(d_n1_y) == -1 else abs(d_n1_y) * ['^']] + [['A']]
#         for val in controls: inputs.extend(val)
#         curr = input_val
#     return inputs


def button_path(curr, target):
    (num_y, num_x), (dir_y, dir_x) = [divmod('789456123_0A<v>'.find(char), 3) for char in (curr, target)]
    res = '>' * (dir_x - num_x) + 'v' * (dir_y - num_y) + '0' * (num_y - dir_y) + '<' * (num_x - dir_x)
    return res if (3, 0) in [(num_y, dir_x), (dir_y, num_x)] else res[::-1]

@functools.cache
def input_path(input, depth):
    if depth < 0:
        return len(input)+1
    return sum(input_path(button_path(curr, target), depth-1) for (curr, target) in zip('A' + input, input + 'A'))

def output(codes, depth):
    res = []
    for code in codes:
        input = code[:3]
        min_path = input_path(input, depth)
        res.append(int(input) * min_path)
    return sum(res)

# Notes: Hardest day by far. Only day that I've really needed to pick through a solution bit by bit to reach my own. In the end, the logic isn't too unintuitive but
# always a small disparity off the correct solution due to some undetermined ordering quirks. Spent ages tinkering and hardcoding to test how button ordering affected things, but still no luck.
# Overall, solution online neat and tidy - more educational than anything this day. One of those ones where you see a solution and wonder how you reach it yourself.

if __name__ == '__main__':
    codes = data('day_21.txt')
    print(f'Part a ---- {output(codes, 2)}')
    print(f'Part b ---- {output(codes, 25)}')
