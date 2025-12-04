#region Input

input = open("input.txt")

line_one = input.readline().strip()
instructions_length = len(line_one)

instructions = "."*(instructions_length+2) + "." + line_one + "."
for line in input.readlines():
    instructions += "." + line.strip() + "."

instructions += "."*(instructions_length+2)

input.close()

example_instructions_array = [
"..@@.@@@@.",
"@@@.@.@.@@",
"@@@@@.@.@@",
"@.@@@@..@.",
"@@.@@@@.@@",
".@@@@@@@.@",
".@.@.@.@@@",
"@.@@@.@@@@",
".@@@@@@@@.",
"@.@.@@@.@.",
]

example_instructions = "."*12
for line in example_instructions_array:
    example_instructions += "." + line.strip() + "."

example_instructions += "."*12

#endregion


#region Solution


def solution(string: str, length: int, depth=1) -> int:
    grid = list(string)
    length += 2

    sum: int = 0

    string_length: int = len(string)
    height: int = string_length // length

    neighbors = [
        ".", ".", ".", #0 1 2
        ".", ".", ".", #3 4 5
        ".", ".", "."  #6 7 8
    ]

    all_done = False
    while depth != 0 and not all_done:
        all_done = True
        for y in range(1, height - 1):
            for x in range(1, length - 1):
                position: int = x+y*length
                if grid[position] == ".":
                    continue

                neighbors = [
                    grid[position-1-length], grid[position-length], grid[position+1-length],
                    grid[position-1]       , grid[position]       , grid[position+1]       ,
                    grid[position-1+length], grid[position+length], grid[position+1+length],
                ]
                if neighbors.count("@") <= 4:
                    sum += 1
                    grid[position] = "."
                    all_done = False

        depth -= 1
    return sum

# Example
print(solution(example_instructions, length = 10))
print(solution(example_instructions, length = 10, depth=-1))


# Part 1
print(solution(instructions, length=instructions_length))

# Part 2
print(solution(instructions, length=instructions_length, depth=-1))

#endregion