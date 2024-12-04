import pandas as pd
import numpy as np
from collections import Counter

def data(path):
    data = pd.read_csv(path, sep=" ", header=None)
    list1, list2 = sorted(list(data[0])), sorted(list(data[3]))
    return list1, list2


def part_a(list1, list2):
    # Simple approach, equivalent length list so zip between values and return list of absolute differences, which can then be summed.
    return np.array([np.abs(x-y) for x, y in zip(list1, list2)]).sum()


def part_b(list1, list2):
    # Approach: Counter to store value occurences in list2, iterate list1 and aggregate count accordingly.
    counts = Counter(list2)
    count = 0
    for num in list1:
        if num in counts.keys():
            count += num * counts[num]
    return count


if __name__ == '__main__':
    list1, list2 = data('day_1.txt')
    print(f'Part a: {part_a(list1, list2)}')
    print(f'Part b: {part_b(list1, list2)}')
