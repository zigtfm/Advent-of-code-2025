#region Input

def init_input_1(path: str) -> dict:
    input = open(path)

    output = [list(x.strip()) for x in input.readlines()]

    input.close()

    return output

def init_input_2(path: str) -> dict:
    input = open(path)

    output = [[int(y) for y in list(x.strip().replace(".","0").replace("S","1").replace("^", "2"))] for x in input.readlines()]
    for line in output:
        for i in range(len(line)):
            if line[i] == 2: line[i] = -1


    input.close()

    return output

#endregion


#region Solution

def solution_1(input: dict, display: bool=False) -> int:
    count = 0
    # Start
    input[1][input[0].index("S")] = "|"

    # Draw lines
    for y in range(1, len(input) - 1):
        for x in range(len(input[y])):
            if input[y][x] == "|":
                match input[y+1][x]:
                    case ".":
                        input[y+1][x] = "|"
                    case "^":
                        count += 1
                        input[y+1][x-1] = "|"
                        input[y+1][x+1] = "|"


    if display:
        for line in input:
            print("".join(line))

    return count

def solution_2(input: dict, display: bool=False) -> int:
    # Start
    input[1][input[0].index(1)] = 1

    # Draw lines
    for y in range(1, len(input) - 1):
        for x in range(len(input[y])):
            value = input[y][x]
            if value > 0:
                next_value = input[y+1][x]
                # Straight
                if next_value >= 0:
                    input[y+1][x] += value

                # Split
                else:
                    input[y+1][x-1] += value
                    input[y+1][x+1] += value

    if display:
        for line in input:
            string_line = [(" " if x < 10 else "") + str(x) for x in line]
            print(("".join(string_line)).replace("-1", "^").replace("0", " "))

    return sum(input[-1])


print(solution_1(init_input_1("input_example.txt"), display=False))
print(solution_2(init_input_2("input_example.txt"), display=True))

print(solution_1(init_input_1("input.txt")))
print(solution_2(init_input_2("input.txt")))

#endregion


#region Performance

import timeit

def perf_test():
    print("Part 1")

    input_1 = init_input_1("input.txt")
    print(f"Parse input\t{timeit.timeit((lambda:init_input_1("input.txt")),number=3)/3:9f}s")
    print(f"Solve\t\t{timeit.timeit((lambda:solution_1(input_1)),number=3)/3:9f}s")

    print("Part 2")

    input_2 = init_input_2("input.txt")
    print(f"Parse input\t{timeit.timeit((lambda:init_input_2("input.txt")),number=3)/3:9f}s")
    print(f"Solve\t\t{timeit.timeit((lambda:solution_2(input_2)),number=3)/3:9f}s")


perf_test()

#endregion