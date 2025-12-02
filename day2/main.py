
#region Input

input = open("input.txt")

instructions = input.read().split(",")

instructions = list(map(
    lambda x: list(map(int, x.split("-"))),
    instructions
))

input.close()

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


# Slow solution
print(solution_re(r'(.+)\1'))
print(solution_re(r'(.+)(\1)+'))


#endregion