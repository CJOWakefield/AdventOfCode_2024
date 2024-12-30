import re

def data(path):
    nums = list(map(int, re.findall(r'\d+', open('day_17.txt').read())))
    return nums[:3], nums[3:]

def part_a(registers, instructions):
    input_pos = 0
    output = [0, 1, 2, 3] + registers
    while input_pos < len(instructions):
        opcode, operand = instructions[input_pos:input_pos+2]
        if opcode == 0: output[-3] >>= output[operand]
        elif opcode == 1: output[-2] ^= operand
        elif opcode == 2: output[-2] = output[operand] % 8
        elif opcode == 3:
            if output[-3]: input_pos = operand - 2
        elif opcode == 4: output[-2] ^= output[-1]
        elif opcode == 5: yield output[operand] % 8
        elif opcode == 6: output[-2] = output[-3] >> output[operand]
        else: output[-1] = output[-3] >> output[operand]

        input_pos += 2
    return output

def recursive_search(instructions, target, prev_reg_a=0):
    if not target:
        return prev_reg_a

    for a in range(1 << 10):
        prev_instr = prev_reg_a % 128
        a_shift = a // 8
        next_instr = next(part_a([a, 0, 0], instructions))
        if prev_instr == a_shift and next_instr == target[-1]:
            res = recursive_search(instructions, target[:-1], (prev_reg_a << 3) | (a % 8))
            if res is not None:
                return res

# Notes: Havent't used generators a lot, only real quirk in part_a was working out the logic of the different opcodes and then obtaining the output from the generator. All the bit logic here and adjustments was tricky,
# but eventually reached the correct solution. Did lean on some hints from the subreddit here. Note to self to recap this one. Interesting program though.

if __name__ == '__main__':
    registers, instructions = data('day_17.txt')
    print(f'Part a ---- {",".join(list(map(str, part_a(registers, instructions))))}')
    target = instructions
    print(f'Part b ---- {recursive_search(instructions, target)}')
