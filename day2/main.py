
#region Input

input = open("input.txt")

instructions = input.read().split(",")

instructions = list(map(
    lambda x: list(map(int, x.split("-"))),
    instructions
))

input.close()

#endregion


#region Helpers

import math

def int_len(number: int) -> int:
    return int(math.log10(number)) + 1


# Excluded self, and reversed
divisors = [
    [], #0
    [],
    [1],
    [1],
    [2, 1],
    [1],
    [3, 2, 1],
    [1],
    [4, 2, 1],
    [3, 1],
    [5, 2, 1],
    [1],
    [6, 4, 3, 2, 1],
    [1],
    [7, 2, 1],
    [5, 3, 1],
    [8, 4, 2, 1],
    [1],
    [9, 6, 3, 2, 1],
    [1],
]

def split_number(n, a, b) -> int:
    return n % 10**a // 10**b

#endregion


#region Solution

import re

def solution_re(pattern: re.Pattern) -> int:
    sum = 0

    for x in instructions:
        for i in range(x[0], x[1]+1):
            str_i = str(i)

            result = re.fullmatch(pattern, str_i)
            if result != None:
                if result.string == str_i:
                    sum += i

    return sum



def solution_split_point_part1() -> int:
    sum = 0

    for x in instructions:
        for i in range(x[0], x[1]+1):
            i_len = int_len(i)
            if i_len % 2 == 1: continue

            split_point = 10**(i_len // 2)

            # Left part == Right part
            if i // split_point == i % split_point :
                sum += i

    return sum


'''
- input: 121212
Iterate
    1. is 111 = 212?
    2. is 12 = 12 = 12?
    - output: true

- input: 11111
Iterate
    1. is 1 = 1 = 1 = 1 = 1?
    - output: true

- input: 1121
Iterate
    1. is 11 = 21?
    2. is 1 = 1 = 2 = 1?
    - output: false
'''
def solution_split_point_part2() -> int:
    sum = 0

    for x in instructions:
        for i in range(x[0], x[1]+1):
            i_len = int_len(i)
            for i_divisor in divisors[i_len]:
                split_position = i_len - i_divisor
                split_point = 10**split_position
                parts_count = i_len // i_divisor
                first_part = i // split_point

                all_equal = True
                for i_part in range(1, parts_count):
                    part = split_number(
                        i,
                        (parts_count - i_part)*i_divisor,
                        (parts_count - i_part - 1)*i_divisor
                    )
                    if part != first_part:
                        all_equal = False
                        break

                if all_equal:
                    sum += i
                    break

    return sum

# Regex solution
print(solution_re(r'(.+)\1'))
print(solution_re(r'(.+)(\1)+'))

# Split point solution
print(solution_split_point_part1())
print(solution_split_point_part2())

print("Finished")

#endregion