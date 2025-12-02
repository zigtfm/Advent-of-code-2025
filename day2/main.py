
#region Input

input = open("input.txt")

instructions = input.read().split(",")

instructions = list(map(
    lambda x: list(map(int, x.split("-"))),
    instructions
))

input.close()

#endregion


#region Solution Part 1

import re

sum = 0

for x in instructions:
    for i in range(x[0], x[1]+1):
        str_i = str(i)

        result = re.fullmatch(r'(.+)\1', str_i)
        if result != None:
            if result.string == str_i:
                sum += i

print(sum)

#endregion

#region Solution Part 2

import re

sum = 0

for x in instructions:
    for i in range(x[0], x[1]+1):
        str_i = str(i)

        result = re.fullmatch(r'(.+)(\1)+', str_i)
        if result != None:
            if result.string == str_i:
                sum += i


print(sum)

#endregion