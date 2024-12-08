from collections import defaultdict, deque

def data(path):
    # Return rules and test cases as individual lists
    rules, cases = open(path).read().strip().split('\n\n')
    return rules.split('\n'), cases.split('\n')

def part_a(rules, cases):
    count = 0
    # Approach: Dict of set of values that must come before the key. Check following values in each case to check rules hold. Add valid results.
    rule_dict = defaultdict(set)
    for rule in rules:
        first, second = rule.split('|')
        rule_dict[int(second)].add(int(first))

    for case in cases:
        is_valid = True
        values = [int(val) for val in case.split(',')]
        # print(case, values)
        for i, val in enumerate(values):
            for j, sub_char in enumerate(values):
                if i<j and sub_char in rule_dict[val]:
                    is_valid = False
        if is_valid:
            count += values[len(values)//2]

    return count

def part_b(rules, cases):
    # Implement first function but additional else statement that filters values and rearranges depending on remaining rule involved values.
    count = 0
    before, after = defaultdict(set), defaultdict(set)
    for rule in rules:
        first, second = rule.split('|')
        before[int(second)].add(int(first))
        after[int(first)].add(int(second))

    for case in cases:
        is_valid = True
        values = [int(val) for val in case.split(',')]
        for i, val in enumerate(values):
            for j, sub_char in enumerate(values):
                if i<j and sub_char in before[val]:
                    is_valid = False

        if not is_valid:
            res = []
            queue = deque([])
            # Calculate overlapping values with rules and store how many relative rules to consider in case.
            overlaps = {val: len(before[val] & set(values)) for val in values}
            for val in values:
                # If a value has overlaps[val] == 0, then no values need to go before it any longer, and can be added to the queue to append and rule test itself.
                if overlaps[val] == 0:
                    queue.append(val)
            # Iterate through the queue, identify remaining values to rule check.
            while queue:
                curr = queue.popleft()
                res.append(curr)
                for sub_char in after[curr]:
                    if sub_char in overlaps:
                        overlaps[sub_char] -= 1
                        if overlaps[sub_char] == 0:
                            queue.append(sub_char)
            count += res[len(res)//2]
    return count

# Notes: Tricky day this one. Solution not overly intuitive. First approach for part one sound but small error with the rule_dict lead to lots of wasted time (first, second in wrong positions.)
#        Second part intuition not immediately apparent. Hint needed then implemented by self. Reasonable amount of thought required but worked out logic successfully. No real tech knowledge gaps.

if __name__ == '__main__':
    rules, cases = data('day_5.txt')
    print(part_b(rules, cases))
