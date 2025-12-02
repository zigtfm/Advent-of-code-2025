
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


def solution_simple_part1() -> int:
    sum = 0

    for x in instructions:
        for i in range(x[0], x[1]+1):
            i_len = int_len(i)
            if i_len % 2 == 1: continue

            half_len = i_len // 2
            left_part = i // 10**half_len
            right_part = i % 10**half_len
            if left_part == right_part:
                sum += i

    return sum

# Slow solution
#print(solution_re(r'(.+)\1')) # 32976912643
#print(solution_re(r'(.+)(\1)+')) # 54446379122

assert(32976912643 == solution_simple_part1)

#endregion