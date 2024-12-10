import numpy as np
from collections import defaultdict
import time

def data(path):
    return open(path).readline()[:-1]


def parse(line):
    # Parse the data into one list containing either a filled drive containing index or an empty drive.
    vals = []
    offset = 0
    for i in range(0, len(line)):
        if i % 2 == 0:
            vals += ([i-offset] * int(line[i]))
        else:
            vals += ('.' * int(line[i]))
            offset += 1
    return vals

def part_a(line):
    # Approach: Expand instructions to one list with all relevant values/dots. Use LR pointer to swap values from right to left where there is a space.
    parsed = parse(line)
    left, right = 0, len(parsed)-1
    while left < right:
        if parsed[left] == '.':
            if parsed[right] != '.':
                parsed[left], parsed[right] = parsed[right], parsed[left]
                left += 1
            right -= 1
        else:
            left += 1

    res = 0
    for i in range(len(parsed)):
        if parsed[i] != '.':
            res += int(parsed[i]) * i
    return res

def part_b(line):
    # Similar approach, but using a moving slider instead.
    parsed = parse(line)
    left, right, window = 0, len(parsed)-1, 1
    while left < right:
        # Adjust to ensure space at left position and int at right position.
        while parsed[left] != '.':
            left += 1
        while parsed[right] == '.':
            right -= 1
        # Adjust window until non-matching integer found
        curr_val = parsed[right]
        while parsed[right-1] == curr_val:
            right -= 1
            window += 1
        # Slide window from left until sufficient chunk of space found.
        if all(char == '.' for char in parsed[left:left+window]):
            # print(f'{parsed[left: left+window]} at index {left}:{left+window} replaced by {parsed[right:right+window]}')
            # time.sleep(2)
            parsed[left: left+window], parsed[right:right+window] = [curr_val] * window, ['.'] * window
            left += window
            window = 1
        else:
            temp_left = left
            while temp_left < right:
                if all(char == '.' for char in parsed[temp_left: temp_left+window]):
                    # print(f'{parsed[temp_left: temp_left+window]} at index {temp_left}:{temp_left+window} replaced by {parsed[right:right+window]}')
                    # time.sleep(2)
                    parsed[temp_left: temp_left+window], parsed[right:right+window] = [curr_val] * window, ['.'] * window
                    window = 1
                    break
                else:
                    temp_left += 1
            right -= window
    res = 0
    for i in range(len(parsed)):
        if parsed[i] != '.':
            res += int(parsed[i]) * i
    return res


def part_b_no_parse(line):
    # First approach promising for part b but some edge case preventing correct solution. Attempt without parsing line, passing through input backwards, adjusting when possible.
    spaces = np.array(list(map(int, list(line[1::2]))))
    line_arr = list(map(int, list(line)))
    idx_store = {}
    # Pass backwards through line, finding any suitable spaces in the spaces array and then appending to an index dictionary for each space taken by the new value
    for file in range(len(line)-1, -1, -2):
        file_size, file_idx = int(line[file]), file // 2
        free_spaces = np.argwhere(spaces[:file_idx] >= file_size)
        # If no spaces, find the index position of the file and add to idx_store
        if free_spaces.shape[0] == 0:
            start_idx = sum(line_arr[:file])
            idx_store[file_idx] = list(range(start_idx, start_idx + file_size))
        else:
            space_size, space_idx = free_spaces[0][0], free_spaces[0][0] * 2
            # Find starting index of first suitable file space from spaces array
            start_idx = sum(line_arr[:space_idx+1])
            idx_store[file_idx] = list(range(start_idx, start_idx + file_size))
            # Decrement free space if more space available than required, adjust original line
            spaces[space_size] -= file_size
            line_arr[space_idx] += file_size
            line_arr[space_idx+1] -= file_size

    res = 0
    for key in idx_store.keys():
        res += sum([idx * key for idx in idx_store[key]])
    return res

# Notes: Tricky day not in terms of approach or logic but difficulty to bug fix. Part a finished in first attempt. Part b reattempted with different approach due to small
# solution disparity caused by some unknown edge case which I was unable to identify. Slider approach worked logically but didn't want to waste time bug fixing for small edge
# case. Attempt without parsing more efficient but required more thought. Part_b_2 successfully implemented with some inspiration from online Github solution.


if __name__ == '__main__':
    line = data('day_9.txt')
    print(f'Part a ---- {part_a(line)}')
    print(f'Part b ---- {part_b_no_parse(line)}')
