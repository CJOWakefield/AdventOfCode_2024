import numpy as np
from collections import defaultdict

def data(path):
    return list(map(int, open(path).readlines()))


def conversion(seen, input):
    if input in seen:
        return seen[input]

    step_1 = ((input * 64) ^ input) % 16777216
    step_2 = ((step_1 // 32) ^ step_1) % 16777216
    step_3 = ((step_2 * 2048) ^ step_2) % 16777216
    return step_3

def part_a(codes):
    seen = {}
    res = []
    for code in codes:
        curr = code
        for _ in range(2000):
            new = conversion(seen, curr)
            seen[curr], curr = new, new
        res.append(curr)
    return res

# def part_b(codes):
#     seen = {}
#     sequences = []
#     for code in codes:
#         seq = []
#         curr = code
#         for _ in range(2000):
#             new = conversion(seen, curr)
#             seq.append(int(str(curr)[-1]))
#             seen[curr], curr = new, new
#         sequences.append(seq)

#     seq_changes = [[seq[i]-seq[i-1] if i > 0 else 0 for i in range(len(seq))] for seq in sequences]
#     # Note - try numpy


#     tracker = defaultdict()
#     curr_max = 0
#     for i in range(4, len(seq_changes[0])):
#         bananas = [sequences[0][i]]
#         seq = seq_changes[0][i-4:i]
#         for seq_i in range(1, len(sequences)):
#             # print(seq, bananas)
#             for j in range(4, len(seq_changes[0])):
#                 # print(seq_changes[seq_i][j-4:j])
#                 if seq_changes[seq_i][j-4:j] == seq:
#                     bananas.append(sequences[seq_i][j])
#                     continue
#                     # print(seq, bananas)
#         if sum(bananas) > curr_max:
#             curr_max = sum(bananas)
#         tracker[tuple(seq)] = bananas
#     return curr_max, tracker, sequences, seq_changes


def part_b(codes):
    cache = {}
    bananas = defaultdict(int)
    for code in codes:
        seq = np.zeros(2001, dtype='int')
        seq[0] = code % 10
        for j in range(1, 2001):
            code = conversion(cache, code)
            seq[j] = code % 10
        diffs = np.diff(seq)

        seen = set()
        for seq_idx in range(4, len(diffs)):
            sub_seq = tuple(diffs[seq_idx-3: seq_idx+1])
            if sub_seq not in seen:
                bananas[sub_seq] += seq[seq_idx+1]
                seen.add(sub_seq)
    # return dict(sorted(bananas.items(), key=lambda x: x[1]))
    return sorted(bananas.values())

# Notes: Interesting problem. Probably one of my favourites for the year. Part a simple enough. Part b struggled with some patterning issues
# before realising converting to numpy will make things more robust and easier. Took some bug fixing to prevent duplicate patterns from being recorded for each
# input code and some tinkering and research on how to cut down time complexity.

if __name__ == '__main__':
    codes = data('day_22.txt')
    print(f'Part a ---- {sum(part_a(codes))}')
    print(f'Part b ---- {max(part_b(codes))}')
