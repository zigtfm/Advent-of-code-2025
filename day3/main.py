#region Input

input = open("input.txt")

instructions = []
for line in input.readlines():
    instructions.append(line.strip())

input.close()

#endregion


#region Solution


def solution_part1(strings):
    sum = 0
    for line in strings:
        number = ""

        slice_position = None
        for i in ["9","8","7","6","5","4","3","2","1"]:
            position = line.find(i)
            if position != -1:
                number += i
                slice_position = position + 1

                for i in ["9","8","7","6","5","4","3","2","1"]:
                    position = line[slice_position:].find(i)
                    if position != -1:
                        number += i
                        break

                if len(number) == 2:
                    break
                else:
                    number = ''

        sum += int(number)

    return sum


def solution_part2(strings):
    sum = 0
    for line in strings:
        sum += int(search_2(line))

    return sum


"""
811111111111119

8111----------- +8
 1111---------- +81
  1111--------- +811
   1111-------- +8111
    1111------- +81111
     1111------ +811111
      1111----- +8111111
       1111---- +81111111
        1111--- +811111111
         1111-- +8111111111
          1111- +81111111111
           1119 +811111111119
"""

Numbers = ["9","8","7","6","5","4","3","2","1"]
def search_2(line: str, depth=12):
    furthest_position = len(line) - depth + 1
    slice_point = 0
    number = ""

    while len(number) < depth:
        for value in Numbers:
            position = line[slice_point:furthest_position].find(value)
            if position != -1:
                number += value
                slice_point += position + 1
                max_digits = len(line) - (depth - 1 - len(number)) - slice_point
                furthest_position = slice_point + max_digits
                break

    #print(number)
    return number


print(solution_part1([
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111",
]))

print(solution_part1(instructions))


print(solution_part2([
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111",
]))

print(solution_part2(instructions))

#endregion